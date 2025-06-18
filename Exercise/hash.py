# test hash

import hashlib
import bcrypt

data = "Hello, World!"

#md5
hash_md5 = hashlib.md5(data.encode()).hexdigest()
print(hash_md5)

#sha1
hash_sha1 = hashlib.sha1(data.encode()).hexdigest()
print(hash_sha1)


#hash mat khau
pwd = "password123"

hash_pwd = bcrypt.hashpw(pwd.encode(), bcrypt.gensalt()).decode()
print(hash_pwd)
