# -*- coding: utf-8 -*-
"""
Created on Tue May 24 13:16:17 2022

@author: jario
"""
import pyorc

# Escribimos el archivo
with open("./archivo.orc", "wb") as data:
    with pyorc.Writer(data, "struct<col0:string,col1:string,col2:int>") as writer:
        writer.write(("svr_et_1", "12.20.15.122",399))
        writer.write(("svr_et_2", "12.20.11.395",400))
        writer.write(("svr_wt_1", "12.20.12.836",500))
        writer.write(("svr_wt_2", "12.20.17.193",200))
        
print("Escribiendo archivo","---->","archivo.orc")