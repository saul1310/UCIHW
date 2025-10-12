/*
=========================================================
Word Frequency Counter (C Wireframe - No Library Functions)
=========================================================
Goal:
    - Read a text file
    - Ignore stop words
    - Count how often each word appears
    - Output the 25 most frequent words

Constraints:
    - No use of libraries like <string.h>, <ctype.h>, etc.
    - Implement everything manually (string operations, comparisons, etc.)
=========================================================
*/

// ========================
// Data Structures
// ========================

// Structure to hold a word and its frequency
// You will store each word and how many times it appears
struct Word {
    char word[50];  // maximum length for a word
    int count;
};

// Structure to hold all stop words
struct StopWords {
    char words[500][20]; // example: up to 500 stop words, each max 20 chars
    int total;
};

// Structure to hold all unique words found in the text in key value pairs 
struct WordList {
    struct Word words[10000]; // example: up to 10,000 unique words
    int total;
    // every time a word is encountered, search the struct for it
    // if its found, increment its pair by 1
    // if not, add a new key value pair
};


// ========================
// Function Declarations
// ========================

// Converts uppercase letters in a word to lowercase (manual ASCII conversion)
void toLower(char *word);

// Checks if a character is a letter or digit (manual ASCII check)
int isAlnum(char c);

// Loads stop words from file (read character by character)
void loadStopWords(char *filename, struct StopWords *stopWords);

// Checks if a given word is a stop word
int isStopWord(char *word, struct StopWords *stopWords);

// Reads text file, extracts words, and counts frequencies
void countWordFrequencies(char *filename, struct StopWords *stopWords, struct WordList *wordList);

// Sorts the words by frequency (descending order)
void sortByFrequency(struct WordList *wordList);
    // Since space complexity is not a huge concern for this, is probably
    // alright to not sort in place and just make and return a new struct
    
    // iterate through the structure of words


// Prints the top 25 words
void printTop25(struct WordList *wordList);
// print up to the 25th entry in the sorted list returned by sortByfrequency


// ========================
// Main Function
// ========================

int main() {
    // 1. Declare file names for input text and stop words
    //    e.g., "pride-and-prejudice.txt" and "stop_words.txt"

    // 2. Create StopWords and WordList structures

    // 3. Load stop words from stop_words.txt

    // 4. Read input file and count word frequencies

    // 5. Sort by frequency

    // 6. Print top 25 words and their counts

    // 7. End program
    return 0;
}

