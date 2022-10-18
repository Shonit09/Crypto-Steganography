import rsa_key as rsaKey
import rsa_ency as rsaEncy
import rsa_decy as rsaDecy

print("\tRsa key generation\n\n")
rsaKey.main()
print("\n\tRsa key generation ended\n\n\tRsa encryption started\n\n")
rsaEncy.main()
print("\n\tRsa encryption ended\n\n\tRsa decryption started\n\n")
rsaDecy.main()
print("\n\tRsa decryption ended")