# import os
# os.system("c:\\sam.bat")


import subprocess

cmd = 'cmd.exe D:\\simu_app\\auto-tool\\air_test.bat'
p = subprocess.Popen("cmd.exe /c" + "D:\\simu_app\\auto-tool\\air_test.bat", stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

curline = p.stdout.readline()
while (curline != b''):
    print(curline)
    curline = p.stdout.readline()

p.wait()
print(p.returncode)