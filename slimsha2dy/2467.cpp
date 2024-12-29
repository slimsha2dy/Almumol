#include <iostream>
#include <algorithm>

using namespace std;
int n;
int arr[101010];

int	main(int argc, char **argv)
{
	ios::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);
	
	cin >> n;
	for (int i = 0; i < n; ++i) cin >> arr[i];

	int l = 0;
	int r = n-1;
	int res = 2000000001;
	int rl = 0;
	int rr = n-1;
	while (l < r) {
		int tmp = abs(arr[l] + arr[r]);
		if (tmp < res) {
			res = tmp;
			rl = l;
			rr = r;
		}
		int a = abs(arr[l+1] + arr[r]);
		int b = abs(arr[l] + arr[r-1]);
		if (a < b) {
			l++;
		}
		else {
			r--;
		}
	}
	cout << arr[rl] << ' ' << arr[rr];
}

