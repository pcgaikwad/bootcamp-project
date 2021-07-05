import hashlib
print(hashlib.algorithms_available)


#Challenge 1
hash= hashlib.md5(b"Yeah! I completed my challenge.")
print("MD5 Hash output :- ",hash.digest(), " \n")

#Challenge 2
hash1= hashlib.shake_256(b"I am completing my second challenge.")
print("shake_256 hash output :-", hash1.digest(10))

hash2 =hashlib.blake2b(b"I am completing my second challenge.")
print("blake2b hash output   :-", hash2.digest())

hash3 = hashlib.sha1(b"Yeah! I completed my second challenge.")
print("sha1 hash output      :-", hash3.digest())