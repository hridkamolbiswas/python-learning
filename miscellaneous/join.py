import os


cdir = os.getcwd()
os_name = os.name

print(cdir,'\n', os_name)
if os.path.exists("text.txt"):
    print('yes')
else:
    print('No')

s = 'iam hrid'
print(s.split())
print('_'.join(s.split()))
print(':'.join(s))
