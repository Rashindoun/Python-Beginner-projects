
def calculate():
    print("bienvenue dans calculatrice voicit les opération possible + , - , * , /")
    operator = input("quel opération choissez-vous :")
    num1=int(input("premier chiffre ou nombre : "))
    num2=int(input("deuxième chiffre ou nombre: "))
    if operator == "+":
        opération = num1 + num2
        print("le résultat est : ",opération)
    elif operator == "-":
        opération = num1 - num2
        print("le résultat est : ",opération)
    elif operator == "*":
        opération = num1 * num2
        print("le résultat est : ",opération)
    elif operator == "/":
        opération = num1 / num2
        print("le résultat est : ",opération)
    else:
        print("sorry opération non supporté par la calculatrice")

while True:
    calculate()
    continuer =input("vouler continuer d'utiliser la calculatrice ? O/n :")
    if continuer == "O" or continuer == "o":
        continue
    elif continuer == "n" or continuer =="N":
        break