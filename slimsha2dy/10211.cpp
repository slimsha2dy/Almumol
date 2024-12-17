#include <iostream>
#include <algorithm>

using namespace std;
int n, t;
int arr[1010], dp[1010];

int	main(int argc, char **argv)
{
	ios::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);
	cin >> t;
	while (t--) {
		cin >> n;
		for (int i = 0; i < n; ++i) cin >> arr[i];
		dp[0] = arr[0];
		int res = dp[0];
		for (int i = 1; i < n; ++i) {
			dp[i] = max(0, dp[i-1]) + arr[i];
			res = max(res, dp[i]);
		}
		cout << res <<'\n';
	}
}

