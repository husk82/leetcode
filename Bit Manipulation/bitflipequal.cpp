#include <iostream>

using namespace std;

int check_possibilities(int n, int k) {
    if ((n & k) != k) {
        return -1;
    }

    int n_ones = 0, k_ones = 0;

    while (n) {
        n = n & (n -1);
        n_ones++;
    }

    
    while (k) {
        k = k & (k -1);
        k_ones++;
    }

    return n_ones - k_ones;
}

int main (void)
{
    int n, k;
    
    cout << "Enter first int: ";
    cin >> n;
    
    cout << "Enter second int: ";
    cin >> k;

    int result = check_possibilities(n, k);
    if (result == -1) cout << "Not Possible";
    else cout << "Min changes: " << result;

    return 0;
}