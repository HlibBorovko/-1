txt = '''abc abc abc abc abc abc abc abc abc abc 
         Lorem ipsum dolor sit amet, consectetur adipiscing elit,  
         sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.  
         Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut  
         aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in  
         voluptate velit esse cillum dolore eu fugiat nulla pariatur.  
         Excepteur sint occaecat cupidatat non proident,  
         sunt in culpa qui officia deserunt mollit anim id est laborum.'''
txt = txt.split()
res = {}
n = int(input())
for i in range(len(txt) - n + 1):
    tmp = ' '.join(txt[i:i + n])
    res[tmp] = res.get(tmp, 0) + 1
res = sorted([(k, v) for k, v in res.items()], key=lambda x: -x[1])
print(*res[:10], sep='\n')