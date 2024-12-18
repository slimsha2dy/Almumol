#include <climits>
#include <iostream>
#include <algorithm>

using namespace std;
int n;
pair<char, char> ch[30];

void jeon(int i) {
	if (i == ('.' - 'A')) return;
	cout << (char) (i + 'A');
	jeon(ch[i].first - 'A');
	jeon(ch[i].second - 'A');
}

void joong(int i) {
	if (i == ('.' - 'A')) return;
	joong(ch[i].first - 'A');
	cout << (char) (i + 'A');
	joong(ch[i].second - 'A');
}

void hoo(int i) {
	if (i == ('.' - 'A')) return;
	hoo(ch[i].first - 'A');
	hoo(ch[i].second - 'A');
	cout << (char) (i + 'A');
}

int	main(int argc, char **argv)
{
	ios::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);
	
	cin >> n;
	for (int i = 0; i < n; ++i) {
		char a, b, c;
		cin >> a >> b >> c;
		int idx = a - 'A';
		ch[idx]= {b, c};
	}
	jeon(0);
	cout << '\n';
	joong(0);
	cout << '\n';
	hoo(0);
	cout << '\n';
}

