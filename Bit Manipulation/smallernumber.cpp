#include <iostream>
#include <vector>

using namespace std;

vector<int> smallerNumbersThanCurrent (vector<int> nums) {

    vector<int> freq(101,0);
    for (int num: nums) {
        freq[num]++;
    }

    for (int i = 1; i < 101; i++) {
        freq[i] = freq[i] + freq[i - 1];
    }

    vector<int> result;

    for (int i=0; i < nums.size(); i++){
        int smaller = (nums[i] == 0) ? 0 : freq[nums[i] - 1];
        result.push_back(smaller);
    }

    return result;

}

int main () {
    vector<int> nums = {8, 1, 2, 2, 3};

    vector<int> result = smallerNumbersThanCurrent(nums);

    cout << "Result: " ;
    for (int i: result) cout << i << " ";

    return 0;
}