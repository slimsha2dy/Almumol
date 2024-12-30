#include <iostream>
#include <algorithm>

using namespace std;
int n, m;
int arr[2020], dp[2020][2020];

int	main(int argc, char **argv)
{
	ios::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);

	cin >> n;
	for (int i = 1; i <= n; ++i) cin >> arr[i];
	cin >> m;
	for (int j = 1; j <= n; ++j) {
		for (int i = 1; i <= j; ++i) {
			if ((i == j) || (i+1 == j && arr[i] == arr[j])) {
				dp[i][j] = 1;
				continue;
			}
			if (arr[i] == arr[j] && dp[i+1][j-1]) dp[i][j] = 1;
		}
	}
	while (m--) {
		int a, b;
		cin >> a >> b;
		cout << dp[a][b] << '\n';
	}
}

