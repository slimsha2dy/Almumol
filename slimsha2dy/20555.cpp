#include <iostream>
#include <algorithm>

using namespace std;
int n, m;
string s[10];
int dp[54][5][8];
// i번째 글자가 j일 때 k번 문자열에서 일치하는 개수

int	main(int argc, char **argv)
{
	cin.tie(0);
	cout.tie(0);
	ios::sync_with_stdio(0);

	cin >> n;
	int total = 0;
	for (int i = 0; i < n; ++i) {
		cin >> s[i];
		total += s[i].length();
	}

	for (int i = 1; i < 54; ++i) {
		for (int j = 1; j <= 4; ++j) {
			int sum = 0;
			for (int k = 1; k <= n; ++k) {
				for (int ch = 1; ch <= 4; ++ch) {
					if (s[k-1].length() == dp[i-1][ch][k]) dp[i][j][k] = s[k-1].length();
					else if (s[k-1][dp[i-1][ch][k]] - 'A' == j - 1) dp[i][j][k] = max(dp[i][j][k], dp[i-1][ch][k] + 1);
				}
				sum += dp[i][j][k];
			}
			if (total == sum) {
				cout << i << endl;
				return 0;
			}
		}
	}
}

