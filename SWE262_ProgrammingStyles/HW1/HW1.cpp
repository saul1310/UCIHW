#include <iostream>  // Include the input/output library
#include <fstream>
using namespace std;
#include <map>
#include <string>
#include <cctype> 
#include <sstream>
#include <vector>


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
    return convertToLowerCase(rawWord); 
};

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
};

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

        string stripped = strip(line);

        // while (int i = 0; i < line.length();i++){


        

        // at this part the line must be turned into individual words and then ran through themap


    } 
    file.close();
   

   
  


    // run each word through the frequency map
    return frequencymap;



};




// convert freq map into a list going from highest frequency to lowest
// return high to low list


//main function has to run from the command line, taking in the textfile


int main() {

    createFrequencyMap();
    string test = "this is a test yeah";
     vector<string> words = split(test);

    // print each word
    for (const auto& w : words) {
        cout << w << endl;
    }

    
 
    return 0;
}

    
