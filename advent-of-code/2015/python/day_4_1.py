import hashlib

secret = "yzbqklnj"
i = 0

while not (hashlib.md5(f"{secret}{i}".encode('utf-8')).hexdigest()).startswith("000000"):
	i += 1

print(f"Resposta -> {i}")