# Exemplo de Interface de Linha de Comando. CLI
# Utilizando lib click

import os

import click


@click.group()
def translate():
    """Translation and localization commands."""
    pass


@translate.command()
@click.argument("lang")
def init(lang):
    """Initialize a new language."""
    if os.system(
        "pybabel extract --output-file  translations/messages.pot --input-dirs app/"
    ):
        raise RuntimeError("extract command failed")
    if os.system(
        "pybabel init -i translations/messages.pot -d translations/ -l " + lang
    ):
        raise RuntimeError("init command failed")


@translate.command()
def update():
    """Update all languages."""
    if os.system(
        "pybabel extract --output-file  translations/messages.pot --input-dirs app/"
    ):
        raise RuntimeError("extract command failed")
    if os.system(
        "pybabel update -i ./translations/messages.pot -d translations/ --previous"
    ):
        raise RuntimeError("update command failed")


@translate.command()
def compile():
    """Compile all languages."""
    if os.system("pybabel compile -d translations/"):
        raise RuntimeError("compile command failed")


if __name__ == "__main__":
    translate()
