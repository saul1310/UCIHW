#include <iostream>  // Include the input/output library
#include <fstream>
using namespace std;
#include <map>
#include <string>


string strip(string) {
    //take in an input line
    string test ="every day, i wonder why!"
    // iterate through every character, if its in the blacklist, remove
    //return back the stripped string





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




int main() {
    createFrequencyMap();
 
    return 0;
}
