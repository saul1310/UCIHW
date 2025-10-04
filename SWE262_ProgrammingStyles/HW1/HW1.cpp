#include <iostream> 
#include <fstream>
#include <map>
#include <string>
#include <cctype> 
#include <sstream>
#include <vector>
using namespace std;


/* Returns lowercase conversion*/
string convertToLowerCase(string& input) {
    string lowerCase = "";
    lowerCase.reserve(input.size()); 

    for (size_t i = 0; i < input.size(); i++) {
        lowerCase += tolower(static_cast<unsigned char>(input[i]));
    }
    return lowerCase;
}


/* Takes in a line of text as a string, returns the line strpped of punctuation*/
string strip(const string& input) {
    string blacklist = ".,!-+=&?'";
    string rawWord = input;
    for (int i =0; i < rawWord.length();){
        if (blacklist.find(rawWord[i]) != string::npos) 
        {
            rawWord.erase(i,1);
        }
        else{
            i++;
        }
    }
    return rawWord;
}

/* Takes in a line and returns a vector of words*/
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

// establish a frequency map hashtable

map<string,int> createFrequencyMap(){
    map<string,int> frequencymap;
    // ask user for input 
    ifstream file("testwords.txt");
    if (!file.is_open()) {
        cout << "Could not open file!" << endl;
        return {};
    }
    string line;
    while (getline(file,line)){

        line = strip(line);
        line = convertToLowerCase(line);
        vector<string> words = split(line);
        for (const auto& w : words) {
            if (frequencymap.find(w) != frequencymap.end()) {
                frequencymap[w]++;
            } else {
                frequencymap[w] = 1;
            }
        }
       


        

       


    } 
    file.close();
   

   
  



  
    cout << "Word Frequency Map: " << endl;
    for (const auto& pair : frequencymap) {
        cout << pair.first << ": " << pair.second << endl;


    };
}




// convert freq map into a list going from highest frequency to lowest
// return high to low list


//main function has to run from the command line, taking in the textfile


int main() {

    createFrequencyMap();
    return 0;
}

    
