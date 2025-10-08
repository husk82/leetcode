#include <iostream>
#include <vector>

using namespace std;

bool checkCharacter(vector<int>& bits) {
    int c=0;
    for (int i = bits.size() - 2; i>=0; i--) {
        if (bits[i] == 1) c++;
        else break;
    }
    return !(c%2);
}

int main () {
    int c;
    
    cout << "Enter length of array: ";
    cin >> c;

    vector<int> bits;
    int user_input; 
    cout << "Start entering bits: ";
    for (int i = 0; i < c; i++) {  
        cin >> user_input; 
        bits.push_back(user_input);
    }

    if (checkCharacter(bits)) {
        cout << "True";
    }
    else {
        cout << "False";
    }
    
}