#include <iostream>
#include <algorithm>
#include <map>
#include <queue>

using namespace std;
int n, m;
map<int, int> d;

int rec(int i) {
	if (d.count(i) != 0) return d[i];
	if (i == 0) return d[i] = -1;
	d[i] = 2147483647;
	if ((i % 10) == 1) {
		if (rec(i / 10) != -1)
			d[i] = rec(i / 10) + 1;
	}
	if ((i % 2) == 0) {
		if (rec(i / 2) != -1)
			d[i] = min(d[i], rec(i / 2) + 1);
	}
	if (d[i] == 2147483647) d[i] = -1;
	return d[i];
}

int	main(int argc, char **argv)
{
	ios::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);

	cin >> n >> m;
	d[n] = 1;
	cout << rec(m);
}

// dp 풀이법
// d[k] = min(d[k/2], d[k/10]) + 1
// 하지만 오른쪽은 조건에 따라 달라진다
// 그런데 사실 이 조건들은 배타적이므로 더 간단한 풀이가 존재할 것 같다

