# Info
[폴짝 게임](https://boj.kr/17498)

- 난이도: 골드 5
- 분류: 다이나믹 프로그래밍

## 💡 풀이 방법 요약

DP 를 사용했습니다.

지금 위치로부터 갈 수 있는 모든 칸까지 계산한 결과와 갈 수 있는 위치의 dp 값 중 큰 값을 유지했습니다.

## 👀 실패 이유

으헝 파이썬 싫어...

일단 파이썬으로 시간초과가 발생해 pypy 로 바꿔서 풀게 되었습니다...

그래도 75퍼에서 틀렸습니다가 발생해서 기존에 dp를 계산하던 방식을 내 위치로 올 수 있는 좌표들의 최대값을 더하는 것에서

내 위치에서 갈 수 있는 좌표들을 계산하도록 바꿨더니 통과했습니다.

아마 그 사이에서 뭔가 놓쳤던 부분이 메워진 것 같아요.

## 🙂 마무리
