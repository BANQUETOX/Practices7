# Haga un programa que lea un arreglo de números reales que guarda los saldos de las cuentas de
# ahorro de un grupo de clientes de un banco y que lea otro arreglo que guarda los nombres de los
# clientes a los que corresponde cada cuenta, así el saldo de la cuenta[i] pertenece al cliente[i] del
# banco. El programa debe hacer un reporte e imprimir el nombre de cada cliente y el saldo de su cuenta
# de ahorro. Además, debe imprimir el saldo promedio de las cuentas de ahorro del banco y el nombre
# del cliente con saldo mayor en el banco. Para resolver esto usted debe hacer: una rutina
# llenarArregloReales que lee un arreglo de números reales, una rutina llenarArregloString que lee un
# arreglo de String, una rutina saldoPromedio recibe un arreglo de reales y calcula el promedio del
# arreglo, una rutina clienteSaldoMayor que recibe un arreglo de reales con los saldos de las cuentas y
# un arreglo de String con los nombres de los clientes, y retorna un String con el nombre del cliente con
# el saldo mayor.


amount_accounts = int(input("Cuantas cuentas quiere registrar?"))
def llenarArregloReales(amount_accounts):
    accounts = []
    for account in range(0,amount_accounts):
        account_value = int(input(f"Cual es el saldo de la cuenta #{account + 1} "))
        accounts.append(account_value)
    return accounts

def llenarArregloString(amount_accounts):
    clients = []
    for client in range(0,amount_accounts):
        client_name = input(f"Cual es el nombre de la cuenta #{client + 1} ")
        clients.append(client_name)
    return clients

def saldoPromedio(accounts:list):
    accounts_average = 0
    for account in accounts:
        accounts_average += account
    accounts_average =  accounts_average / len(accounts)
    return accounts_average

def clienteSaldoMayor(accounts, clients):
    most_value_account = 0
    for account in accounts:
        if account > most_value_account:
            most_value_account = account
    return f"La cuenta de ahorros con mas fondos es la de {clients[accounts.index(most_value_account)]} con un total de {most_value_account} en fondos"

accounts = llenarArregloReales(amount_accounts)
clients = llenarArregloString(amount_accounts)
print(saldoPromedio(accounts))
print(clienteSaldoMayor(accounts,clients))


# amount_accounts = int(input("Cuantas cuentas quiere registrar?"))
# accounts = []
# clients = []
# accounts_above_average = []
# accounts_average = 0
# most_value_account = 0
# for account in range(0,amount_accounts):
#     client_name = input(f"Cual es el nombre de la cuenta #{account + 1} ")
#     account_value = int(input(f"Cual es el saldo de la cuenta #{account + 1} "))
#     accounts_average += account_value
#     accounts.append(account_value)
#     clients.append(client_name)
# accounts_average = accounts_average / amount_accounts
# for account in accounts:
#     print(f"El saldo del cliente {clients[accounts.index(account)]} es de {accounts[accounts.index(account)]}")
#     if account > most_value_account:
#         most_value_account = account
#     if account >= accounts_average:
#         accounts_above_average.append(account)
# print(f"El saldo promedio en las cuentas de ahorro es de {accounts_average}")
# print(f"La cuenta de ahorros con mas fondos es la de {clients[accounts.index(most_value_account)]} con un total de {most_value_account} en fondos")
# print(f"Los clientes con fondos mayores al promedio son ")
# for account in accounts_above_average:
#     print(clients[accounts.index(account)])