import os
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

with open(os.path.join(BASE_DIR, "chave_aes.bin"), "rb") as f:
    chave_aes = f.read()

with open(os.path.join(BASE_DIR, "mensagem_cifrada.bin"), "rb") as f:
    dados = f.read()
nonce, mensagem_cifrada = dados[:12], dados[12:]

aesgcm = AESGCM(chave_aes)
pacote = aesgcm.decrypt(nonce, mensagem_cifrada, None)

mensagem, assinatura = pacote.split(b"---SIGN---")

digest = hashes.Hash(hashes.SHA256())
digest.update(mensagem)
hash_mensagem = digest.finalize()

with open(os.path.join(BASE_DIR, "public_key.pem"), "rb") as f:
    public_key = serialization.load_pem_public_key(f.read())

try:
    public_key.verify(assinatura, hash_mensagem, padding.PKCS1v15(), hashes.SHA256())
    print("Assinatura verificada com sucesso! Mensagem autêntica.")
except Exception:
    print("Assinatura inválida! Mensagem alterada ou origem desconhecida.")

print("\nMensagem decifrada:")
print(mensagem.decode())
