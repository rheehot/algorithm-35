# 메모이제이션 사용하기 위해 db 초기화
d = [0] * 100

d[1] = 1
d[2] = 1

# 몇 번째 수를 찾고싶은가?
n = 10

# 피보나치 수열을 반복문으로 구현, 보텀업 다이나믹 프로그래밍 - 디버깅해보면 f(3)->f(4)->f(5) 순서대로 메모된다.
for i in range(3, n+1):
    d[i] = d[i - 1] + d[i - 2]

print(d[n])

