#include <iostream>  // Include the input/output library
#include <fstream>
using namespace std;
#include <map>
#include <string>
string test ="every day, i wonder why!";


string strip(const string& input) {
    string blacklist = ".,!-+=&?";
    //take in an input line
    string rawWord = input;
 
    // iterate through every character, if its in the blacklist, remove
    for (int i =0; i < rawWord.length(); i++ ) {
        if (blacklist.find(rawWord[i]) != string::npos) 
        {
            rawWord.erase(i,1);

        }


    }
    return rawWord;





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
        cout << line << endl;


    }

    file.close();
   

   
  


    // run each word through the frequency map
    return frequencymap;



};




// convert freq map into a list going from highest frequency to lowest
// return high to low list


//main function has to run from the command line, taking in the textfile


int main() {
    string test = "hey, my name is joe!";
    // createFrequencyMap();
    cout << strip(test);
 
    return 0;
}
