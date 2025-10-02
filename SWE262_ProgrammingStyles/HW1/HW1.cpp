#include <iostream>  // Include the input/output library
#include <fstream>
using namespace std;
#include <map>
#include <string>
#include <cctype> 
string test ="every day, i wonder why!";

string convertToLowerCase(string& input) {
    string lowerCase = "";
    lowerCase.reserve(input.size()); 

    for (size_t i = 0; i < input.size(); i++) {
        lowerCase += tolower(static_cast<unsigned char>(input[i]));
    }

    return lowerCase;
}

//i should change the rawWord variable name as it takes in a line
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
    



// I also need to make it convert all letters to lowercase so that it doesnt count the same word differently
// i could insert that at the return statement of strip,
// and just return the product of a function that converts it


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
    // strip of punctuation marks 


    while (getline(file,line)){

        cout << strip(line) << endl;


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

    
 
    return 0;
}

    
