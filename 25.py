# classic solution
# 3?12?14*5
for n in range(0, 10**10, 1917):
    s = str(n)
    if s[0] != '3':
        continue
    if s[-1] != '5':
        continue
    if s[2:3+1] != '12':
        continue
    if s[5:6+1] != '14':
        continue
    print(n, n//1917)

# cheat code
import fnmatch
for n in range(0, 10**10, 1917):
    if fnmatch.fnmatch(str(n), '3?12?14*5'):
        print(n, n//1917)