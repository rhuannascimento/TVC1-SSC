import os
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

with open(os.path.join(BASE_DIR, "mensagem.txt"), "rb") as f:
    mensagem = f.read()

with open(os.path.join(BASE_DIR, "private_key.pem"), "rb") as f:
    private_key = serialization.load_pem_private_key(f.read(), password=None)

digest = hashes.Hash(hashes.SHA256())
digest.update(mensagem)
hash_mensagem = digest.finalize()

assinatura = private_key.sign(hash_mensagem, padding.PKCS1v15(), hashes.SHA256())

pacote = mensagem + b"---SIGN---" + assinatura

chave_aes = AESGCM.generate_key(bit_length=128)
aesgcm = AESGCM(chave_aes)
nonce = os.urandom(12)
mensagem_cifrada = aesgcm.encrypt(nonce, pacote, None)

with open(os.path.join(BASE_DIR, "mensagem_cifrada.bin"), "wb") as f:
    f.write(nonce + mensagem_cifrada)

with open(os.path.join(BASE_DIR, "chave_aes.bin"), "wb") as f:
    f.write(chave_aes)

print("Mensagem assinada e criptografada com sucesso!")
