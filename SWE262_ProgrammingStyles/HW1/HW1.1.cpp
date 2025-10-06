#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <set>
#include <vector>
#include <algorithm>
#include <cctype>

using namespace std;

// Function to convert string to lowercase
string toLower(const string& str) {
    string result = str;
    transform(result.begin(), result.end(), result.begin(), ::tolower);
    return result;
}

// Function to check if character is alphanumeric
bool isAlnum(char c) {
    return isalnum(static_cast<unsigned char>(c));
}

// Function to load stop words from file
set<string> loadStopWords(const string& filename) {
    set<string> stopWords;
    ifstream file(filename);
    
    if (!file.is_open()) {
        cerr << "Error: Could not open stop words file: " << filename << endl;
        return stopWords;
    }
    
    string line;
    while (getline(file, line)) {
        // Split by comma
        string word;
        for (char c : line) {
            if (c == ',') {
                if (!word.empty()) {
                    stopWords.insert(toLower(word));
                    word.clear();
                }
            } else {
                word += c;
            }
        }
        if (!word.empty()) {
            stopWords.insert(toLower(word));
        }
    }
    
    file.close();
    return stopWords;
}

// Function to process text file and count word frequencies
map<string, int> countWordFrequencies(const string& filename, const set<string>& stopWords) {
    map<string, int> wordFreq;
    ifstream file(filename);
    
    if (!file.is_open()) {
        cerr << "Error: Could not open input file: " << filename << endl;
        return wordFreq;
    }
    
    string word;
    char c;
    
    while (file.get(c)) {
        if (isAlnum(c)) {
            word += tolower(c);
        } else {
            if (word.length() >= 2) {
                if (stopWords.find(word) == stopWords.end()) {
                    wordFreq[word]++;
                }
            }
            word.clear();
        }
    }
    
    // Handle last word if file doesn't end with non-alphanumeric
    if (word.length() >= 2) {
        if (stopWords.find(word) == stopWords.end()) {
            wordFreq[word]++;
        }
    }
    
    file.close();
    return wordFreq;
}

int main(int argc, char* argv[]) {
    if (argc != 2) {
        cerr << "Usage: " << argv[0] << " <input_file>" << endl;
        return 1;
    }
    
    string inputFile = argv[1];
    string stopWordsFile = "stop_words.txt";
    
    // Load stop words
    set<string> stopWords = loadStopWords(stopWordsFile);
    
    // Add single letters to stop words
    for (char c = 'a'; c <= 'z'; c++) {
        stopWords.insert(string(1, c));
    }
    
    // Count word frequencies
    map<string, int> wordFreq = countWordFrequencies(inputFile, stopWords);
    
    // Convert map to vector for sorting
    vector<pair<string, int>> freqVec(wordFreq.begin(), wordFreq.end());
    
    // Sort by frequency (descending)
    sort(freqVec.begin(), freqVec.end(), 
         [](const pair<string, int>& a, const pair<string, int>& b) {
             return a.second > b.second;
         });
    
    // Print top 25 words
    int count = 0;
    for (const auto& pair : freqVec) {
        if (count >= 25) break;
        cout << pair.first << "  -  " << pair.second << endl;
        count++;
    }
    
    return 0;
}