#include <iostream>
#include <algorithm>

using namespace std;
string a, b;
int d[1010][1010];

void recur(int x, int y) {
	if (d[x][y] == 0) return;
	
	while (d[x][y] == d[x-1][y] || d[x][y] == d[x][y-1]) {
		if (d[x][y] == d[x-1][y]) x--;
		else y--;
	}
	recur(x-1, y-1);
	cout << a[x-1];
}

int	main(int argc, char **argv)
{
	ios::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);

	cin >> a >> b;
	for (int i = 1; i <= a.length(); ++i) {
		for (int j = 1; j <= b.length(); ++j) {
			if (a[i-1] == b[j-1]) d[i][j] = d[i-1][j-1] + 1;
			else d[i][j] = max(d[i-1][j], d[i][j-1]);
		}
	}

	cout << d[a.length()][b.length()] << endl;
	if (d[a.length()][b.length()] == 0) return 0;
	recur(a.length(), b.length());
}

