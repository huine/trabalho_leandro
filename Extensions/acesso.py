import hashlib as hash

def cripto(a):
    senha = hash.sha1(a).hexdigest()

    return senha
