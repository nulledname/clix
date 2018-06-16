# -*- coding: utf-8 -*-

from distutils.core import setup 
import py2exe 
 
setup(name="Clix", 
 version="1.0", 
 description="Asistente personal", 
 author="Luciano Joaquin Alfonso", 
 author_email="admin@pinacoidal.tk", 
 url="pinacoida.tk", 
 license="license", 
 scripts=["clix.py"], 
 console=["clix.py"], 
 options={"py2exe": {"bundle_files": 1}}, 
 zipfile=None,
)