from main import string_work, num_to_str
# ERR5 -3 En test_num_to_str_num no se verifica la respuesta.
# No basta con verificar que sea solo un string


def test_str_work_mayus_a_minus():
    """
    verifica que la funcion funcione correctamente al intercambiar mayusculas
    por minusculas y viceversa
    """
    # recorre el rango de letras de la a a la z
    for i in range(ord('a'), ord('z')+1):
        # funciona correctamente intercambiar minusculas por mayusculas
        assert string_work(chr(i)) == chr(i).upper()
    # recorre el rango de letras de la A a la Z
    for i in range(ord('A'), ord('Z')+1):
        # funcione correctamente al intercambiar mayusculas por minusculas
        assert string_work(chr(i)) == chr(i).lower()


# verifica que la funcion funcione correctamente al ingresar un numero int
def test_str_work_num():
    for i in range(0, 100):  # recorre el rango de numeros de 0 a 99
        # retorne el error 1 cuando se ingresa un caracter invalido
        assert string_work(i) == 1


def test_str_work_caracter_invalido():
    """verifica que la funcion funcione correctamente al ingresar un caracter
    invalido, numeros o simbolos
    """
    # recorre los caracteres ascii de 33 a 47,
    # correspondientes a los simbolos y numeros
    for i in range(33, 65):
        # chr(i) retorna el simbolo o numero correspondiente al ascii i,
        # el error debe ser 2
        assert string_work(chr(i)) == 2


def test_num_to_str_num():
    # Verifica que el num_to_str lea correctamente los numeros del 1 al 99
    for i in range(1, 100):
        assert type(num_to_str(i)) == str, "El numero indicado no es aceptado"
        i += 1


def test_num_to_str_str():
    # Verifica que el num_to_str retorne el error correcto con un caracter
    assert num_to_str("abc") == 4, "El numero indicado no es aceptado"


def test_num_to_str_neg():
    # Verifica que el num_to_str retorne el error correcto con un numero
    # negativo
    assert num_to_str(-1) == 3, "El numero indicado no es aceptado"
