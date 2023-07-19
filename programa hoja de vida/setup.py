# -*- coding: utf-8 -*-
from distutils.core import setup
import py2exe

setup(
    name="Hojas de vida",
    version="1.0",
    description="Programa que busca en archivos csv la informacion para rellenar hojas de vida de cada equipo",
    author="Edgar Mauricio Bello Lamprea",
    author_email="edgarmbellol@gmail.com",
    url="https://github.com/edgarmbellol/hoja-vida-equipos",
    license="Libre",
    scripts=["Hojas de vida.py"],
    console=["Hojas de vida.py"],
    options={"py2exe": {"bundle_files": 1}},
    zipfile=None,
)