#include <iostream>
#include <algorithm>
#include <tuple>

using namespace std;
int n, m;
tuple<int, int, int> arr[10101010];
int p[10101];

int find(int x) {
	if (p[x] == x) return x;
	return p[x] = find(p[x]);
}

void uni(int x, int y) {
	x = find(x);
	y = find(y);
	if (x == y) return;
	p[y] = x;
}

int	main(int argc, char **argv)
{
	ios::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);

	cin >> n >> m;
	for (int i = 0; i < m; ++i) {
		int a, b, c;
		cin >> a >> b >> c;
		arr[i] = {c, a, b};
	}
	sort(arr, arr+m);

	for (int i = 0; i <= n; ++i) p[i] = i;
	int ans = 0;
	for (int i = 0; i < m; ++i) {
		int a, b, c;
		tie(c, a, b) = arr[i];
		if (find(a) == find(b)) continue;
		uni(a, b);
		ans += c;
	}
	cout << ans;
}

