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

// Structure to hold all unique words found in the text
struct WordList {
    struct Word words[10000]; // example: up to 10,000 unique words
    int total;
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

// Prints the top 25 words
void printTop25(struct WordList *wordList);


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


// ========================
// Function Definitions
// ========================

// void toLower(char *word)
//     - Loop through each character
//     - If between 'A' and 'Z', add 32 to make it lowercase

// int isAlnum(char c)
//     - Return 1 if ('a' <= c <= 'z') or ('A' <= c <= 'Z') or ('0' <= c <= '9')
//     - Else return 0

// void loadStopWords(char *filename, struct StopWords *stopWords)
//     - Open stop_words.txt
//     - Read one character at a time
//     - When a comma or newline appears, end the current word and store it
//     - Increase stopWords->total

// int isStopWord(char *word, struct StopWords *stopWords)
//     - Loop through all stored stop words
//     - Compare each character manually
//     - If identical, return 1 (true)
//     - Else return 0

// void countWordFrequencies(char *filename, struct StopWords *stopWords, struct WordList *wordList)
//     - Open the text file
//     - Read character by character
//     - Build words using only alphanumeric characters
//     - Convert to lowercase
//     - When a non-alphanumeric is reached:
//         - Check if word length >= 2
//         - Check if not a stop word
//         - If word already exists, increment count
//         - Otherwise add new word to wordList

// void sortByFrequency(struct WordList *wordList)
//     - Use nested loops (manual bubble sort or selection sort)
//     - Compare counts
//     - Swap words and counts accordingly

// void printTop25(struct WordList *wordList)
//     - Print first 25 entries of wordList (word and count)
