# 作者: 王道 龙哥
# 2022年03月12日10时43分33秒

import hashlib
f = open('./test.log', 'rb')
f_md5 = hashlib.md5()
f_md5.update(f.read())

print (f_md5.hexdigest())