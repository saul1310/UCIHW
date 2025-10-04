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
        // feed the stripped line into the split function
        //that returns a vector of the spit words
        // iterate through this vector into the hashmap


       


        

        // I think the file reader should be in a different function, the map one just creates map and runs an input through it


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

    
