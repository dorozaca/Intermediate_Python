def palindrome(string):
    try:
        if len(string)==0:
            raise ValueError('No se puede ingresar una cadena vacia')
        return string==string[::-1]
    except ValueError as ve:
        print(ve)
        return False

try:
    palindrome(1)
        
except TypeError:
    print('Solo se pueden ingresar strings')        
