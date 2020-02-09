def judge(N, S):
    length = len(S)
    if N % 2 == 0 and S[:length//2] == S[length//2:]:
        return 'Yes'

    return 'No'


N = int(input())
S = input()
print(judge(N, S))