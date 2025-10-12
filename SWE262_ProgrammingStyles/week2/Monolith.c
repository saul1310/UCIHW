#include <stdio.h>

#define MAX_WORDS 10000
#define MAX_WORD_LEN 50
#define MAX_STOPWORDS 500
#define MAX_LINE_LEN 1000

// ========================
// Data Structures
// ========================

struct Word {
    char word[MAX_WORD_LEN];
    int count;
};

struct StopWords {
    char words[MAX_STOPWORDS][20];
    int total;
};

struct WordList {
    struct Word words[MAX_WORDS];
    int total;
};

// ========================
// Function Implementations
// ========================

// Converts uppercase letters to lowercase
void toLower(char *word) {
    int i = 0;
    while (word[i] != '\0') {
        if (word[i] >= 'A' && word[i] <= 'Z') {
            word[i] = word[i] - 'A' + 'a';
        }
        i++;
    }
}

// Checks if a character is a letter or digit
int isAlnum(char c) {
    if ((c >= 'a' && c <= 'z') ||
        (c >= 'A' && c <= 'Z') ||
        (c >= '0' && c <= '9')) {
        return 1;
    }
    return 0;
}

// Compares two strings manually
int compareWords(char *a, char *b) {
    int i = 0;
    while (a[i] != '\0' && b[i] != '\0') {
        if (a[i] != b[i]) return 0;
        i++;
    }
    return a[i] == b[i]; // both should end at same time
}

// Copies string manually
void copyWord(char *dest, char *src) {
    int i = 0;
    while (src[i] != '\0') {
        dest[i] = src[i];
        i++;
    }
    dest[i] = '\0';
}

// Loads stop words from file
void loadStopWords(char *filename, struct StopWords *stopWords) {
    FILE *file = fopen(filename, "r");
    if (!file) return;

    stopWords->total = 0;
    char word[20];
    int i = 0;
    char c;
    int index = 0;

    while ((c = fgetc(file)) != EOF) {
        if (c == ',' || c == '\n') {
            if (index > 0) {
                word[index] = '\0';
                toLower(word);
                copyWord(stopWords->words[stopWords->total], word);
                stopWords->total++;
                index = 0;
            }
        } else {
            if (index < 19) {
                word[index++] = c;
            }
        }
    }
    // last word
    if (index > 0) {
        word[index] = '\0';
        toLower(word);
        copyWord(stopWords->words[stopWords->total], word);
        stopWords->total++;
    }
    fclose(file);
}

// Checks if a word is a stop word
int isStopWord(char *word, struct StopWords *stopWords) {
    for (int i = 0; i < stopWords->total; i++) {
        if (compareWords(word, stopWords->words[i])) return 1;
    }
    return 0;
}

// Adds word to WordList or increments its count
void addOrIncrementWord(struct WordList *list, char *word) {
    for (int i = 0; i < list->total; i++) {
        if (compareWords(list->words[i].word, word)) {
            list->words[i].count++;
            return;
        }
    }
    // not found, add new
    copyWord(list->words[list->total].word, word);
    list->words[list->total].count = 1;
    list->total++;
}

// Reads input file and counts word frequencies
void countWordFrequencies(char *filename, struct StopWords *stopWords, struct WordList *wordList) {
    FILE *file = fopen(filename, "r");
    if (!file) return;

    wordList->total = 0;
    char word[MAX_WORD_LEN];
    int index = 0;
    char c;

    while ((c = fgetc(file)) != EOF) {
        if (isAlnum(c)) {
            if (index < MAX_WORD_LEN - 1) {
                if (c >= 'A' && c <= 'Z') c = c - 'A' + 'a';
                word[index++] = c;
            }
        } else {
            if (index >= 2) { // skip single-letter words
                word[index] = '\0';
                if (!isStopWord(word, stopWords)) {
                    addOrIncrementWord(wordList, word);
                }
            }
            index = 0;
        }
    }
    // last word
    if (index >= 2 && !isStopWord(word, stopWords)) {
        word[index] = '\0';
        addOrIncrementWord(wordList, word);
    }

    fclose(file);
}

// Sort words by frequency (descending) using simple selection sort
void sortByFrequency(struct WordList *list) {
    for (int i = 0; i < list->total - 1; i++) {
        int maxIdx = i;
        for (int j = i + 1; j < list->total; j++) {
            if (list->words[j].count > list->words[maxIdx].count) {
                maxIdx = j;
            }
        }
        // swap
        if (maxIdx != i) {
            struct Word temp = list->words[i];
            list->words[i] = list->words[maxIdx];
            list->words[maxIdx] = temp;
        }
    }
}

// Print top 25 words
void printTop25(struct WordList *list) {
    int limit = list->total < 25 ? list->total : 25;
    for (int i = 0; i < limit; i++) {
        printf("%s  -  %d\n", list->words[i].word, list->words[i].count);
    }
}

// ========================
// Main
// ========================

int main(int argc, char *argv[]) {
    if (argc < 2) {
        printf("Usage: %s <input_file>\n", argv[0]);
        return 1;
    }

    char *filename = argv[1];
    char *stopWordsFile = "stop_words.txt";

    struct StopWords stopWords;
    struct WordList wordList;

    loadStopWords(stopWordsFile, &stopWords);
    countWordFrequencies(filename, &stopWords, &wordList);
    sortByFrequency(&wordList);
    printTop25(&wordList);

    return 0;
}
