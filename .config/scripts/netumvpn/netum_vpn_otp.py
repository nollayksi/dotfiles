import pyotp
from os.path import expanduser

home = expanduser("~")
secretFile = open(home + "/.config/scripts/netumvpn/secret/vpn_secrets.txt", "r")
secrets = secretFile.read().splitlines()

totp = pyotp.TOTP(secrets[0])
print(totp.now())
credFile = open(home + "/.config/scripts/netumvpn/secret/creds.txt", "w", encoding="utf8")

credFile.write("vpn.secrets.password:"+ secrets[2] + totp.now())
credFile.close()

