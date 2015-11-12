from sha import sha
import uuid
import os

senha = "123123"
salt = uuid.uuid4().hex
new_senha = sha(salt.encode() + senha.encode()).hexdigest() + ':*:' + salt
print new_senha
