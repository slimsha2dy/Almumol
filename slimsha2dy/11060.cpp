#include <iostream>
#include <algorithm>

using namespace std;
int n;
int arr[1010], dp[1010];

int	main(int argc, char **argv)
{
	ios::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);

	cin >> n;
	for (int i = 0; i < n; ++i) cin >> arr[i];
	fill(dp, dp+n, 1000000000);
	dp[0] = 0;
	for (int i = 1; i < n; ++i) {
		for (int j = 1; j <= i; ++j) {
			if (arr[i-j] < j) continue;
			dp[i] = min(dp[i], dp[i-j]+1);
		}
	}
	if (dp[n-1] == 1000000000) {
		cout << -1;
		return 0;
	}
	cout << dp[n-1];
}

