#include <iostream>
#include <algorithm>

using namespace std;
long long n, m;
int arr[1010101];

bool func(long long input) {
	long long res = 0;
	for (int i = 0; i < n-1; ++i) {
		long long tmp = arr[i+1] - arr[i];
		long long st = max(input - tmp + 1, 0LL);
		res += (input + st) * (input - st + 1) / 2;
	}
	res += input * (input + 1) / 2;
	return res >= m;
}

int	main(int argc, char **argv)
{
	ios::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);

	cin >> n >> m;
	for (int i = 0; i < n; ++i) {
		cin >> arr[i];
	}

	long long st = 0;
	long long en = 2147483647;
	long long ans = 0;
	while (st <= en) {
		long long mid = (st + en) / 2;
		if (func(mid)) {
			ans = mid;
			en = mid - 1;
		} else {
			st = mid + 1;
		}
	}
	cout << ans;
}

