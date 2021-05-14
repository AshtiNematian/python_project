import hashlib
password = input("*Enter* password: ")
hash_password = hashlib.sha256(password.encode('utf8')).hexdigest()