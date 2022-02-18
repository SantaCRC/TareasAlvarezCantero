from main import *
import pytest

def test_str_work_mayus_a_minus(): #verifica que la funcion funcione correctamente al intercambiar mayusculas por minusculas y viceversa
    for i in range(ord('a'), ord('z')+1): #recorre el rango de letras de la a a la z
        assert string_work(chr(i))==chr(i).upper() #verifica que la funcion funcione correctamente al intercambiar minusculas por mayusculas
    for i in range(ord('A'), ord('Z')+1): #recorre el rango de letras de la A a la Z
        assert string_work(chr(i))==chr(i).lower() #verifica que la funcion funcione correctamente al intercambiar mayusculas por minusculas

def test_str_work_num(): #verifica que la funcion funcione correctamente al ingresar un numero int
    for i in range(0,100): #recorre el rango de numeros de 0 a 99
        assert string_work(i)==1 #verifica que la funcion retorne correctamente el error 1 cuando se ingresa un caracter invalido

def test_str_work_caracter_invalido(): #verifica que la funcion funcione correctamente al ingresar un caracter invalido, numeros o simbolos
    for i in range (33,65): #recorre los caracteres ascii de 33 a 47, correspondientes a los simbolos y numeros
        assert string_work(chr(i))==2 #chr(i) retorna el simbolo o numero correspondiente al ascii i, el error debe ser 2

def test_num_to_str_num():
#Verifica que el num_to_str lea correctamente los numeros del 1 al 99
    for i in range (1,100):
        assert type(num_to_str(i)) == str, "El numero indicado no es aceptado por el programa"
        i+=1

def test_num_to_str_str():
#Verifica que el num_to_str retorne el error correcto con un caracter
    assert num_to_str("abc")==4, "El numero indicado no es aceptado por el programa"
    
def test_num_to_str_neg():
#Verifica que el num_to_str retorne el error correcto con un numero negativo
    assert num_to_str(-1)==3, "El numero indicado no es aceptado por el programa"
