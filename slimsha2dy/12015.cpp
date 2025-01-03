#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;
int n;
int arr[1010101];

int	main(int argc, char **argv)
{
	ios::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);

	cin >> n;
	for (int i = 0; i < n; ++i) cin >> arr[i];


	vector<int> v;
	v.push_back(arr[0]);
	for (int i = 1; i < n; ++i) {
		if (arr[i] > v.back()) v.push_back(arr[i]);
		else {
			int j = (lower_bound(v.begin(), v.end(), arr[i])) - v.begin();
			v[j] = arr[i];
		}
	}
	cout << v.size();
}

