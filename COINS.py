l = {}
def cal(N):
	if N < 12:
		return N
	elif N not in l:
		l[N] = cal(N // 2) + cal(N // 3) + cal(N // 4)
	return l[N]

for _ in range(10):
	try:
		N = int(input())
		print(cal(N))
	except:
		break

	