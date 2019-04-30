import random
import os
import math
import string
import secrets
import os
import pyperclip
import sys
import time
from time import sleep
from random import randint

######MODULOS######

def declaracion():
    print("\nA little password generator for the moment")
    print("Copyright (C) 2019  warPort\n")
    print("This program is free software: you can redistribute it and/or modify")
    print("it under the terms of the GNU General Public License as published by")
    print("the Free Software Foundation, either version 3 of the License, or")
    print("(at your option) any later version.\n")
    print("This program is distributed in the hope that it will be useful,")
    print("but WITHOUT ANY WARRANTY; without even the implied warranty of")
    print("MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the")
    print("GNU General Public License for more details.\n")
    print("You should have received a copy of the GNU General Public License")
    print("along with this program.  If not, see <https://www.gnu.org/licenses/>.")

    sleep(3)
    os.system('clear')

def menu():
    global largo
    print("             H E L L O   F R I E N D   ")
    print("")
    largo = int(input("Introduzca el largo de caracteres de tu password: "))
    print("")
    global cat
    cat = input("Utilizamos el metodo A o el B? ")
    print("")
    print("")

def metodoa():
    #viene siendo npgen.py
    sec=[0,1,2,3,4,5,6,7,8,9]
    sec=sec*4
    sec+=string.ascii_letters
    i=0
    muestra=[]

    while(i!=largo):
        muestra.append(secrets.choice(sec))
        i+=1

    i=0
    os.system('clear')
    print("")
    print("              P A S S   4   P Y              ")
    print("")
    print("Metodo utilizado: ",cat.upper())
    print("Largo de contraseña: ",largo,"char")
    print("")
    print("Su nueva password es: ",end="")
    while (i<len(muestra)):
        print(muestra[i],end="")
        i+=1

    print("\n")
    print("\n")
    impA=''.join(str(e) for e in muestra)
    final01(impA,metodoa)

def metodob():
    sec = string.ascii_letters
    a=[]

    for x in range(0,largo):

        sel=randint(0,51)
        num=randint(0,9)
        bi=randint(0,1)
        #Nueva variable binaria aleatorea
        if largo%2==1 and largo==x:
            continue
        elif bi==1:
            a.append(num)
        elif bi==0:
            a.append(sec[sel])

    impB=''.join(str(v) for v in a)
    os.system('clear')
    print("")
    print("              P A S S   4   P Y              ")
    print("")
    print("Metodo utilizado: ",cat.upper())
    print("Largo de contraseña: ",largo,"char")
    print("")
    print("Su nueva password es: ",impB)
    print("\n")

    final01(impB,metodob)

    return

def final01(pcp,ret):
    while True:
        copiar=input("Desea copiar la pass al portapapeles? [Y/n]")
        if not copiar or copiar=='y' or copiar=='Y':
            pyperclip.copy(pcp)
            print("\nCopiado al portapapeles")
            input("Presione enter para seguir")
            break
        elif copiar=='n' or copiar=='N':
            break
        else: break
    os.system('clear')
    salida=input("Desea salir?[y/N]")
    if not salida or salida=='n' or salida=='N':
        mc=input("Desea cambiar de algun parametro?[y/N]\n")
        os.system('clear')
        if mc=='y' or mc=='Y':
            menu()
        elif not mc or mc=='n' or mc=='N':
            print("             H E L L O   F R I E N D   ")
            print("")
            ret()
    else:
        os.system('clear')
        sys.exit()

##########INICIO_DEL_PROGRAMA#################
os.system('clear')
declaracion()
print(" ")
print("       Bienvenido  a  Pass4PY       ")
print(" ")
print(" ")
input("          Precione Enter")
print("")
os.system('clear')
salir=True
menu()

while salir!=False:

    if cat=='A' or cat=='a':
        metodoa() #Agregar aca clausula de salida??
    elif cat=='B' or cat=='b':
        metodob()
    else: menu()
