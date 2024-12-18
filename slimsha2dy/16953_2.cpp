#include <iostream>
#include <algorithm>

using namespace std;
int n, m;

int	main(int argc, char **argv)
{
	ios::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);

	cin >> n >> m;
	int cnt = 1;
	while (m != 0) {
		if (m == n) {
			cout << cnt;
			return 0;
		}
		if ((m % 2) == 0) {
			m /= 2;
		}
		else if ((m % 10) == 1) {
			m /= 10;
		}
		else {
			cout << -1;
			return 0;
		}
		cnt++;
	}
	cout << -1;
}

// 그리디 풀이법
// 짝수면 2로 나누기, 1로 끝나면 1 떼기, 아니면 -1 출력
// 반복하다가 0이 될 경우도 -1 출력

