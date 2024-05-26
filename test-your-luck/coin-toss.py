import sys
import os
file = __file__.split('\\')[:-1]
file = '\\'.join(file)
print(file)

sys.path.append(os.path.dirname(os.path.abspath(file)))

from AUTH import auth
from Table import table

with auth.Auth(file) as _auth:
    # standard authentication process
    # kindly copy paste it
    _table = table.dynamic_table_of(rows=[['Login', '1'], ['Signup', '2']], cols=['Option', 'Selection'], title="Login Table")
    table.get_console().print(_table)
    _input = '/'
    while _input not in ('1', '2'):
        os.system('cls')
        table.get_console().print(_table)
        print("Select from valid selections")
        _input = input("Enter selection: ")

    os.system('cls')

    if _input == '1':
        _id = input("Enter ID: ")
        _pass = input("Enter password: ")
        while not _auth.login({"password":_pass, "id":_id}) and _input == '1':
            __input = '/'
            while __input not in ('y', 'n'):
                os.system('cls')
                print("Unauthorized please enter corrent id and passwor")
                __input = input("want to sign up? y/n\n")
            else:
                os.system('cls')
                _input = '1' if __input == 'n' else '2'
            if _input == '1':
                _id = input("Enter ID: ")
                _pass = input("Enter password: ")
    if _input == '2':
        name = input("Enter name: ")
        password = input("Enter password: ")
        _id = _auth.add_player({"name":name, "password":password})
        print(f"Your id is {_id}, please use this to login again")
        sys.exit()
    
    # till here is authentication and login logic

    print("Authorised and logged in...")

    
