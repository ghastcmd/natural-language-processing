import re

def check_email(email):
    pattern = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')

    if re.fullmatch(pattern, email):
        return True
    return False 


print(check_email("gpss@ic.ufal.br"))
print(check_email("gps.@ic."))
print(check_email("gps.ic."))
print(check_email(".@gmail.com"))
print(check_email(".A@gmail.com"))
print(check_email("nome@gmail."))
