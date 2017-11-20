import subprocess
import win32api
import asyncio
print(1111111111111111)
# asyncio.create_subprocess_shell(['python',r'H:/PyProjects/Scrapy/JdBook/JdBook/redis2mongo.py'])
# win32api.ShellExecute(0,'python','H:/PyProjects/Scrapy/JdBook/JdBook/redis2mongo.py','','',1)
r = subprocess.Popen(['python',r'H:/PyProjects/Scrapy/JdBook/JdBook/redis2mongo.py'])
# subprocess.Popen.terminate(r)
r.wait(timeout=None)
print(222222222222222222222)