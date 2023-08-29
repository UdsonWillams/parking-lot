#!/usr/bin/python3

import datetime

import jwt

SECRET = "o_segredo_do_grande"


def _generate_token(seconds=30):
    exp = datetime.datetime.utcnow() + datetime.timedelta(seconds)
    token = jwt.encode({"exp": exp}, SECRET, algorithm="HS256")
    return f"Bearer {token}"


teste = _generate_token()
print(teste)
