def string_work(string):
    """
    Convierte minusculas en mayusculas y viceversa
    """
    new_string = ""
    if isinstance(string, str):  # Vefifica que sea una cadena de texto
        if string.isalpha():  # verifica que solo contenga letras
            for i in range(len(string)):  # recorre la cadena de texto
                if string[i].islower():  # verifica que sea minuscula
                    new_string += string[i].upper()  # convierte a mayuscula
                else:  # si no es minuscula
                    new_string += string[i].lower()  # convierte a minuscula
            return new_string  # retorna la cadena de texto convertida
        else:    # si no es una cadena de texto
            return 2  # retorna codigo de error 2
    else:  # si es tipo string
        return 1  # retorna codigo de error 1


def num_to_str(num):
    """
    Convierte un numero a texto
    """
    if isinstance(num, int):  # Verifica que sea un numero entero
        if num > 0 and num < 100:  # Verifica que sea un numero entre 0 y 99
            if num == 1:
                return "Uno"
            elif num == 2:
                return "Dos"
            elif num == 3:
                return "Tres"
            elif num == 4:
                return "Cuatro"
            elif num == 5:
                return "Cinco"
            elif num == 6:
                return "Seis"
            elif num == 7:
                return "Siete"
            elif num == 8:
                return "Ocho"
            elif num == 9:
                return "Nueve"
            elif num == 10:
                return "Diez"
            elif num == 11:
                return "Once"
            elif num == 12:
                return "Doce"
            elif num == 13:
                return "Trece"
            elif num == 14:
                return "Catorce"
            elif num == 15:
                return "Quince"
            elif num == 16:
                return "Dieciséis"
            elif num == 17:
                return "Diecisiete"
            elif num == 18:
                return "Dieciocho"
            elif num == 19:
                return "Diecinueve"
            elif num == 20:
                return "Veinte"
            elif num == 21:
                return "Veintiuno"
            elif num == 22:
                return "Veintidós"
            elif num == 23:
                return "Veintitrés"
            elif num == 24:
                return "Veinticuatro"
            elif num == 25:
                return "Veinticinco"
            elif num == 26:
                return "Veintiséis"
            elif num == 27:
                return "Veintisiete"
            elif num == 28:
                return "Veintiocho"
            elif num == 29:
                return "Veintinueve"
            elif num == 30:
                return "Treinta"
            elif num == 40:
                return "Cuarenta"
            elif num == 50:
                return "Cincuenta"
            elif num == 60:
                return "Sesenta"
            elif num == 70:
                return "Setenta"
            elif num == 80:
                return "Ochenta"
            elif num == 90:
                return "Noventa"
            else:
                decenas = num // 10  # Obtiene las decenas
                unidades = num % 10  # Obtiene las unidades
                if decenas == 3:
                    return "Treinta_y_"+num_to_str(unidades)
                    # num_to_str(unidades) retorna las unidades en texto
                elif decenas == 4:
                    return "Cuarenta_y_"+num_to_str(unidades)
                elif decenas == 5:
                    return "Cincuenta_y_"+num_to_str(unidades)
                elif decenas == 6:
                    return "Sesenta_y_"+num_to_str(unidades)
                elif decenas == 7:
                    return "Setenta_y_"+num_to_str(unidades)
                elif decenas == 8:
                    return "Ochenta_y_"+num_to_str(unidades)
                elif decenas == 9:
                    return "Noventa_y_"+num_to_str(unidades)
        else:  # Si no es un numero entre 0 y 99
            return 3  # Retorna codigo de error 3
    else:  # Si no es un numero entero o es negativo
        return 4  # Retorna codigo de error 4
