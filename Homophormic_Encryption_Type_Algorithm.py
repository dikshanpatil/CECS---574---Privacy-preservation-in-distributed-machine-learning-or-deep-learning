import numpy as np
import seal
from seal import EncryptionParameters, SEALContext, KeyGenerator, Encryptor, Decryptor, Evaluator, Plaintext, Ciphertext

# Parameters for homomorphic encryption
parms = EncryptionParameters()
parms.set_poly_modulus("1x^4096 + 1")
parms.set_coeff_modulus(seal.coeff_modulus_128(4096))
parms.set_plain_modulus(1 << 8)
context = SEALContext(parms)
keygen = KeyGenerator(context)
public_key = keygen.public_key()
secret_key = keygen.secret_key()

encryptor = Encryptor(context, public_key)
decryptor = Decryptor(context, secret_key)
evaluator = Evaluator(context)

# Encrypt two numbers
plain1 = Plaintext()
plain1.set_coefficients([123, 0, 0, 0])  # Encodes the number 123
plain2 = Plaintext()
plain2.set_coefficients([45, 0, 0, 0])   # Encodes the number 45

encrypted1 = Ciphertext()
encrypted2 = Ciphertext()
encryptor.encrypt(plain1, encrypted1)
encryptor.encrypt(plain2, encrypted2)

# Perform multiplication and addition on encrypted numbers
result_mul = Ciphertext()
result_add = Ciphertext()
evaluator.multiply(encrypted1, encrypted2, result_mul)  # Multiply encrypted numbers
evaluator.add(encrypted1, encrypted2, result_add)      # Add encrypted numbers

# Decrypt the results
decrypted_result_mul = Plaintext()
decrypted_result_add = Plaintext()
decryptor.decrypt(result_mul, decrypted_result_mul)
decryptor.decrypt(result_add, decrypted_result_add)

print("Decrypted result (Multiplication):", decrypted_result_mul.coefficients())
print("Decrypted result (Addition):", decrypted_result_add.coefficients())
