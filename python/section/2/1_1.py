import sys
sys.stdin = open("1_1.txt", "rt")

# 파이썬스러운 코딩 방법
def isSame(st):
    upperSt = st.upper()
    if upperSt == upperSt[::-1]:
        return True
    else:
        return False

N = int(input())

for i in range(N):
    st = input()
    if isSame(st):
        print("#%d YES" %(i+1))
    else:
        print("#%d NO" %(i+1))