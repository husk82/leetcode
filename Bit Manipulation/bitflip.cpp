#include <iostream>

using namespace std;

int count_bit_flips (int start, int goal) {
    int bitFlipped = start ^ goal;
    int count = 0;
    while (bitFlipped) {
        bitFlipped = bitFlipped & (bitFlipped - 1);
        count++;
    }
    return count;
}

int main () {
    cout << "Enter start: ";
    int start;
    cin >> start;

    cout << "Enter goal: ";
    int goal;
    cin >> goal;

    cout << "Minimum bit flips: " << count_bit_flips(start, goal) ;
}

