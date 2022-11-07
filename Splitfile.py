import hashlib as hs
# import array as arr
from timeit import default_timer as timer
name = input('Enter the name of the file:\n')
#MD5
start = timer()
hash_md5 = hs.md5()
with open(name, 'rb') as file:
    buffer = file.read()
    hash_md5.update(buffer)
    chunk = 0
    while chunk != b'':
        # read only 64 bytes at a time
        chunk = file.read(32)
        hash_md5.update(chunk)
end = timer()
print('Hash of file is:', hash_md5.hexdigest())
print('The time taken for md5:', end - start)

#SHA1
start = timer()
hash_sha1 = hs.sha1()
with open(name, 'rb') as file:
    buffer = file.read()
    hash_sha1.update(buffer)
    chunk = 0
    while chunk != b'':
        # read only 64 bytes at a time
        chunk = file.read(32)
        hash_sha1.update(chunk)
end = timer()
print('Hash of file is:', hash_sha1.hexdigest())
print('The time taken for sha1:', end - start)

#SHA224
start = timer()
hash_sha224 = hs.sha224()
with open(name, 'rb') as file:
    buffer = file.read()
    hash_sha224.update(buffer)
    chunk = 0
    while chunk != b'':
        # read only 64 bytes at a time
        chunk = file.read(32)
        hash_sha1.update(chunk)
end = timer()
print('Hash of file is:', hash_sha224.hexdigest())
print('The time taken for sha224:', end - start)

#SHA256
start = timer()
hash_sha256 = hs.sha256()
with open(name, 'rb') as file:
    buffer = file.read()
    hash_sha256.update(buffer)
    chunk = 0
    while chunk != b'':
        # read only 64 bytes at a time
        chunk = file.read(32)
        hash_sha256.update(chunk)
end = timer()
print('Hash of file is:', hash_sha256.hexdigest())
print('The time taken for sha256:', end - start)

#SHA384
start = timer()
hash_sha384 = hs.sha384()
with open(name, 'rb') as file:
    buffer = file.read()
    hash_sha384.update(buffer)
    chunk = 0
    while chunk != b'':
        # read only 64 bytes at a time
        chunk = file.read(32)
        hash_sha384.update(chunk)
end = timer()
print('Hash of file is:', hash_sha384.hexdigest())
print('The time taken for sha384:', end - start)

#SHA512
start = timer()
hash_sha512 = hs.sha512()
with open(name, 'rb') as file:
    buffer = file.read()
    hash_sha1.update(buffer)
    chunk = 0
    while chunk != b'':
        # read only 64 bytes at a time
        chunk = file.read(32)
        hash_sha512.update(chunk)
end = timer()
print('Hash of file is:', hash_sha512.hexdigest())
print('The time taken for sha512:', end - start)

#Blake2b
start = timer()
hash_blake2b = hs.blake2b()
with open(name, 'rb') as file:
    buffer = file.read()
    hash_blake2b.update(buffer)
    chunk = 0
    while chunk != b'':
        # read only 64 bytes at a time
        chunk = file.read(32)
        hash_blake2b.update(chunk)
end = timer()
print('Hash of file is:', hash_blake2b.hexdigest())
print('The time taken for blake2b:', end - start)

#Blake2s
start = timer()
hash_blake2s = hs.blake2s()
with open(name, 'rb') as file:
    buffer = file.read()
    hash_blake2s.update(buffer)
    chunk = 0
    while chunk != b'':
        # read only 64 bytes at a time
        chunk = file.read(32)
        hash_blake2s.update(chunk)
end = timer()
print('Hash of file is:', hash_blake2s.hexdigest())
print('The time taken for blake2s:', end - start)
