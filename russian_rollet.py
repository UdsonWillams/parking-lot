import os, sys
import random

numeracao_tambor = [1, 2, 3, 4, 5, 6]
tambor_com_bala = random.randint(1, 6)

for tambor in numeracao_tambor:
    resposta = str(input("Quer atirar? [s/n] "))
    if resposta == "s":
        if tambor == tambor_com_bala:
            if sys.platform.startswith("win"):
                os.system('shutdown -s -t 4')
            else:
                os.system('systemctl poweroff')
    else:
        print("Saindo...")
        break
