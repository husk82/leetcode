#include <iostream>

using namespace std;

int find_kthbit(int n, int k) {
    string seq = "0";

    for (int i = 1; i < n && k > seq.length(); ++i) {
        seq += "1";
        string temp = seq;
        for (int j = temp.length() - 2; j >= 0; --j) {
            seq += temp[j] == '1' ? '0' : '1';
        }
    }

    cout << seq;

    return seq[k-1] - '0';

} 

int main () {

    int n, k;
    cout << "Enter n for binary string generation : ";
    cin >>  n;
    cout << "Enter kth bit to find: ";
    cin >> k;

    int result = find_kthbit(n, k);

    cout << "The Kth bit is: " << result;

    return 0;

}