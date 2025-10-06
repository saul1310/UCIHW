#include <iostream> 
#include <fstream>
#include <map>
#include <string>
#include <cctype> 
#include <sstream>
#include <vector>
#include <unordered_set>
using namespace std;

/* Converts a string to lowercase */
string convertToLowerCase(string& input) {
    string lowerCase;
    lowerCase.reserve(input.size()); 
    for (char c : input) {
        lowerCase += tolower(static_cast<unsigned char>(c));
    }
    return lowerCase;
}

/* Removes punctuation from a string */
string strip(const string& input) {
    string blacklist = ".,!-+=&?'\";:()[]{}";
    string rawWord = input;
    for (size_t i = 0; i < rawWord.length();) {
        if (blacklist.find(rawWord[i]) != string::npos) {
            rawWord.erase(i, 1);
        } else {
            i++;
        }
    }
    return rawWord;
}

/* Splits a string into tokens by a delimiter */
vector<string> split(const string& s, char delimiter = ' ') {
    vector<string> tokens;
    string token;
    istringstream iss(s);

    while (getline(iss, token, delimiter)) {
        if (!token.empty()) {   
            tokens.push_back(token);
        }
    }
    return tokens;
}

/* Loads stopwords from stop_words.txt into a set */
unordered_set<string> loadStopWords() {
    unordered_set<string> stopWords;
    ifstream file("stop_words.txt");
    string line, word;

    if (file.is_open()) {
        while (getline(file, line)) {
            stringstream ss(line);
            while (getline(ss, word, ',')) {
                word = strip(word);
                word = convertToLowerCase(word);
                if (!word.empty()) {
                    stopWords.insert(word);
                }
            }
        }
        file.close();
    } else {
        cerr << "Could not open stop_words.txt.\n";
    }
    return stopWords;
}

/* Creates a frequency map while filtering out stopwords */
map<string,int> createFrequencyMap(const string& filename) {
    map<string,int> frequencymap;
    unordered_set<string> stopWords = loadStopWords();

    ifstream file(filename);
    if (!file.is_open()) {
        cout << "Could not open " << filename << "!" << endl;
        return {};
    }

    string line;
    while (getline(file, line)) {
        line = strip(line);
        line = convertToLowerCase(line);
        vector<string> words = split(line);

        for (const auto& w : words) {
            if (stopWords.find(w) == stopWords.end()) {
                frequencymap[w]++;
            }
        }
    }
    file.close();

    cout << "Word Frequency Map for " << filename << ":\n";
    for (const auto& pair : frequencymap) {
        cout << pair.first << ": " << pair.second << endl;
    }

    return frequencymap;
}


int main(int argc, char* argv[]) {
    string filename;

    if (argc > 1) {
        filename = argv[1]; // read from command line
    } else {
        cout << "Enter the name of the file to analyze: ";
        cin >> filename;
    }

    createFrequencyMap(filename);
    return 0;
}
