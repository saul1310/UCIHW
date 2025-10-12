#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>

#define MAX_WORD_LEN 100

// Data structures
typedef struct {
    char **data;
    int count;
    int capacity;
} WordArray;

typedef struct {
    char *word;
    int count;
} WordFreq;

typedef struct {
    WordFreq *data;
    int count;
    int capacity;
} FreqArray;

// Helper functions
WordArray* create_word_array(int capacity) {
    WordArray *wa = malloc(sizeof(WordArray));
    wa->data = malloc(capacity * sizeof(char*));
    wa->count = 0;
    wa->capacity = capacity;
    return wa;
}

FreqArray* create_freq_array(int capacity) {
    FreqArray *fa = malloc(sizeof(FreqArray));
    fa->data = malloc(capacity * sizeof(WordFreq));
    fa->count = 0;
    fa->capacity = capacity;
    return fa;
}

void add_word(WordArray *wa, const char *word) {
    if (wa->count >= wa->capacity) {
        wa->capacity *= 2;
        wa->data = realloc(wa->data, wa->capacity * sizeof(char*));
    }
    wa->data[wa->count] = malloc(strlen(word) + 1);
    strcpy(wa->data[wa->count], word);
    wa->count++;
}

// Pipeline functions
char* read_file(const char *filename) {
    FILE *f = fopen(filename, "r");
    if (!f) {
        fprintf(stderr, "Error: could not open %s\n", filename);
        exit(1);
    }
    
    fseek(f, 0, SEEK_END);
    long len = ftell(f);
    rewind(f);
    
    char *data = malloc(len + 1);
    fread(data, 1, len, f);
    data[len] = '\0';
    fclose(f);
    
    return data;
}

WordArray* extract_words(const char *data) {
    WordArray *words = create_word_array(10000);
    char word[MAX_WORD_LEN];
    int j = 0;
    
    for (int i = 0; data[i] != '\0'; i++) {
        if (isalnum((unsigned char)data[i])) {
            if (j < MAX_WORD_LEN - 1) {
                word[j++] = tolower((unsigned char)data[i]);
            }
        } else if (j > 0) {
            word[j] = '\0';
            if (strlen(word) >= 2) {  // Only words with 2+ characters
                add_word(words, word);
            }
            j = 0;
        }
    }
    
    // Handle last word
    if (j > 0) {
        word[j] = '\0';
        if (strlen(word) >= 2) {
            add_word(words, word);
        }
    }
    
    return words;
}

WordArray* load_stop_words(const char *filename) {
    FILE *f = fopen(filename, "r");
    if (!f) {
        fprintf(stderr, "Error: could not open %s\n", filename);
        exit(1);
    }
    
    WordArray *stops = create_word_array(1000);
    char buffer[20000];
    size_t bytes = fread(buffer, 1, sizeof(buffer) - 1, f);
    buffer[bytes] = '\0';
    fclose(f);
    
    char *token = strtok(buffer, ",\n\r ");
    while (token) {
        add_word(stops, token);
        token = strtok(NULL, ",\n\r ");
    }
    
    return stops;
}

int is_stop_word(const char *word, WordArray *stops) {
    for (int i = 0; i < stops->count; i++) {
        if (strcmp(word, stops->data[i]) == 0) {
            return 1;
        }
    }
    return 0;
}

WordArray* remove_stop_words(WordArray *words, WordArray *stops) {
    WordArray *filtered = create_word_array(words->count);
    
    for (int i = 0; i < words->count; i++) {
        if (!is_stop_word(words->data[i], stops)) {
            add_word(filtered, words->data[i]);
        }
    }
    
    return filtered;
}

FreqArray* count_frequencies(WordArray *words) {
    FreqArray *freqs = create_freq_array(5000);
    
    for (int i = 0; i < words->count; i++) {
        int found = 0;
        for (int j = 0; j < freqs->count; j++) {
            if (strcmp(words->data[i], freqs->data[j].word) == 0) {
                freqs->data[j].count++;
                found = 1;
                break;
            }
        }
        
        if (!found) {
            if (freqs->count >= freqs->capacity) {
                freqs->capacity *= 2;
                freqs->data = realloc(freqs->data, freqs->capacity * sizeof(WordFreq));
            }
            freqs->data[freqs->count].word = malloc(strlen(words->data[i]) + 1);
            strcpy(freqs->data[freqs->count].word, words->data[i]);
            freqs->data[freqs->count].count = 1;
            freqs->count++;
        }
    }
    
    return freqs;
}

FreqArray* sort_by_frequency(FreqArray *freqs) {
    // Bubble sort
    for (int i = 0; i < freqs->count - 1; i++) {
        for (int j = 0; j < freqs->count - i - 1; j++) {
            if (freqs->data[j].count < freqs->data[j + 1].count) {
                WordFreq temp = freqs->data[j];
                freqs->data[j] = freqs->data[j + 1];
                freqs->data[j + 1] = temp;
            }
        }
    }
    return freqs;
}

void print_top_n(FreqArray *freqs, int n) {
    int limit = (freqs->count < n) ? freqs->count : n;
    for (int i = 0; i < limit; i++) {
        printf("%s - %d\n", freqs->data[i].word, freqs->data[i].count);
    }
}

int main(int argc, char *argv[]) {
    if (argc < 2) {
        fprintf(stderr, "Usage: %s <input_file>\n", argv[0]);
        return 1;
    }
    
    // The pipeline
    char *data = read_file(argv[1]);
    WordArray *words = extract_words(data);
    WordArray *stops = load_stop_words("stop_words.txt");
    WordArray *filtered = remove_stop_words(words, stops);
    FreqArray *freqs = count_frequencies(filtered);
    FreqArray *sorted = sort_by_frequency(freqs);
    print_top_n(sorted, 25);
    
    // Cleanup
    free(data);
    
    return 0;
}