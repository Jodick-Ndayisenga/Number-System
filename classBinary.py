from colored import fg, attr, back


class BinaryField:
    def decimalToBinary(self, x: int) -> str:
        myNumber = int(x)
        mainBinary = ""
        while True:
            remainder = myNumber % 2
            myNumber = myNumber-remainder
            quotient = int(myNumber/2)
            myNumber = quotient
            mainBinary = mainBinary+str(remainder)
            if myNumber == 0:
                break
        mainBinary += "0"
        return mainBinary[::-1]

    def octalTODecimal(self, x: str) -> int:
        x = str(x)
        exponet = len(x)-1
        index = 0
        number = 0
        for i in range(0, len(x)):
            number += ((8**exponet)*int(x[index]))
            exponet -= 1
            index += 1
        return number

    def decimalToHexa(self, y) -> list:
        myNumber = int(y)
        mainBinary = ""
        while True:
            remainder = int(myNumber) % 16
            myNumber = myNumber-remainder
            quotient = int(myNumber/16)
            myNumber = quotient
            if remainder == 10:
                remainder = "A"

            elif remainder == 11:
                remainder = "B"

            elif remainder == 12:
                remainder = "C"

            elif remainder == 13:
                remainder = "D"

            elif remainder == 14:
                remainder = "E"

            elif remainder == 15:
                remainder = "F"

            mainBinary = mainBinary+str(remainder)
            if myNumber == 0:
                break

        return mainBinary[::-1]

    def hexaTODecimal(self, x):
        x = [i.upper() for i in x]
        exponet = len(x)-1
        index = 0
        number = 0
        for i in x:
            if i == "A":
                number += ((16**exponet)*10)

            elif i == "B":
                number += ((16**exponet)*11)

            elif i == "C":
                number += ((16**exponet)*12)

            elif i == "D":
                number += ((16**exponet)*13)

            elif i == "E":
                number += ((16**exponet)*14)

            elif i == "F":
                number += ((16**exponet)*15)

            else:
                number += ((16**exponet)*int(i))
            exponet -= 1
            index += 1
        return number

    def decimalToOctal(self, y):
        myNumber = int(y)
        myOctalNumber = ""
        while True:
            remainder = myNumber % 8
            myNumber = myNumber-remainder
            quotient = int(myNumber/8)
            myNumber = quotient
            myOctalNumber = myOctalNumber+str(remainder)
            if myNumber == 0:
                break

        return myOctalNumber[::-1]

    def binaryToDecimal(self, x):
        oBinary = x
        exponet = len(oBinary)-1
        index = 0
        if int(oBinary[0]) == 1:
            number = (-(2**len(oBinary)))
            for i in range(0, len(oBinary)):
                number += ((2**exponet)*int(oBinary[index]))
                exponet -= 1
                index += 1
        else:
            number = 0
            for i in range(0, len(oBinary)):
                number += ((2**exponet)*int(oBinary[index]))
                exponet -= 1
                index += 1
        return number


firstBinary = BinaryField()

while True:
    print("\n================================\n------------HOME PAGE-----------\n================================")
    print("")
    choice = int(input(
        "1. From octal\n2. From hexadecimal\n3. From Binary\n4. From decimal\n\nType the number here: "))
    print("")
    if choice == 1:
        while True:
            fromOctalTo = int(input(
                "       From Octal to:\n        1. Binary\n        2. Hexadecimal\n        3. Decimal\n\n      Type your choice here: "))

            if fromOctalTo == 1:
                print("------------------------------------------------------------\n ---THIS CALCULATION IS FROM OCTAL - BINARY--\n------------------------------------------------------------\n")
                enteredOctal = input(
                    "Enter your octal value to convert to binary: ")
                myDecimal = firstBinary.octalTODecimal(enteredOctal)
                binaryFromDecimal = firstBinary.decimalToBinary(myDecimal)

                print("-----------------------------------------------------")
                print("")
                print(
                    f'{fg("orchid")}{attr("bold")}OCTAL                    BINARY\n[ {enteredOctal} ]   ====>    [ {binaryFromDecimal} ] {attr("reset")}')
                print("")
                print('-----------------------------------------------------')

            elif fromOctalTo == 2:
                print("------------------------------------------------------------\n ---THIS CALCULATION IS FROM OCTAL - HEXADECIMAL--\n------------------------------------------------------------\n")
                value1 = int(
                    input("Enter your octal value convert to hexadecimal: "))
                myDecimal1 = int(firstBinary.octalTODecimal(value1))
                finalBinary1 = firstBinary.decimalToHexa(myDecimal1)
                print("-----------------------------------------------------")
                print("")
                print(
                    f'{fg("orchid")}{attr("bold")}OCTAL                    HEXADECIMAL\n[ {value1} ]   ====>    [ {finalBinary1} ] {attr("reset")}')
                print("")
                print('-----------------------------------------------------')

            elif fromOctalTo == 3:
                print("------------------------------------------------------------\n ---THIS CALCULATION IS FROM OCTAL - DECIMAL--\n----------------------------------------------------------\n")
                value3 = input(
                    "Enter your octal value that you want to convert to Decimal: ")
                myDecimal3 = firstBinary.octalTODecimal(value3)
                print("-----------------------------------------------------")
                print("")
                print(
                    f'{fg("orchid")}{attr("bold")}OCTAL                   DECIMAL\n[ {value3} ]   ====>      [ {myDecimal3} ] {attr("reset")}')
                print("")
                print('-----------------------------------------------------')

            else:
                print("Make sure you enter a valid octal number!!")
                continue
            cont = input("Continue?: ").lower().strip()

            if cont == "yes":
                continue
            else:
                break
# This where transforming from hexadecimal to any other format starts.
    elif choice == 2:
        while True:
            fromHexaTo = int(input(
                "       From Hexadecimal to:\n        1. Binary\n        2. Octal\n        3. Decimal\n\n      Type your choice here: "))

            if fromHexaTo == 1:
                print("------------------------------------------------------------\n ---THIS CALCULATION IS FROM HEXADECIMAL - BINARY--\n------------------------------------------------------------\n")
                enteredHexadecimal = input(
                    "Enter your hexadecimal value to convert to binary: ")
                myHexadecimal = firstBinary.hexaTODecimal(enteredHexadecimal)
                binaryFromHexadecimal = firstBinary.decimalToBinary(
                    myHexadecimal)

                print("-----------------------------------------------------")
                print("")
                print(
                    f'{fg("orchid")}{attr("bold")}HEXADECIMAL      BINARY\n[ {enteredHexadecimal} ]   ====>    [ {binaryFromHexadecimal} ] {attr("reset")}')
                print("")
                print('-----------------------------------------------------')

            elif fromHexaTo == 2:
                print("------------------------------------------------------------\n ---THIS CALCULATION IS FROM HEXADECIMAL - OCTAL--\n------------------------------------------------------------\n")
                enteredHexadecimal = input(
                    "Enter your hexadecimal value to convert to binary: ")
                myHexadecimal = firstBinary.hexaTODecimal(enteredHexadecimal)
                octalFromHexadecimal = firstBinary.decimalToOctal(
                    myHexadecimal)
                print("-----------------------------------------------------")
                print("")
                print(
                    f'{fg("orchid")}{attr("bold")}HEXADECIMAL                  OCTAL\n[ {enteredHexadecimal} ]   ====>    [ {octalFromHexadecimal} ] {attr("reset")}')
                print("")
                print('-----------------------------------------------------')

            elif fromHexaTo == 3:
                print("------------------------------------------------------------\n ---THIS CALCULATION IS FROM HEXADECIMAL - DECIMAL--\n----------------------------------------------------------\n")
                enteredHexadecimalToDecimal = input(
                    "Enter your hexadecimal value that you want to convert to Decimal: ")
                gottenDecimal = firstBinary.hexaTODecimal(
                    enteredHexadecimalToDecimal)
                print("-----------------------------------------------------")
                print("")
                print(
                    f'{fg("orchid")}{attr("bold")}HEXADECIMAL             DECIMAL\n[ {enteredHexadecimalToDecimal} ]   ====>      [ {gottenDecimal} ] {attr("reset")}')
                print("")
                print('-----------------------------------------------------')

            else:
                print("Make sure you enter a valid hexadecimal value !!")
                continue
            cont = input("Continue?: ").lower().strip()

            if cont == "yes":
                continue
            else:
                break

    elif choice == 3:
        while True:
            fromBinaryTo = int(input(
                "       From Binary to:\n        1. Hexadecimal\n        2. Octal\n        3. Decimal\n\n      Type your choice here: "))

            if fromBinaryTo == 1:
                print("------------------------------------------------------------\n ---THIS CALCULATION IS FROM BINARY - HEXADECIMAL--\n------------------------------------------------------------\n")
                enteredBinaryValue = input(
                    "Enter your binary value to convert to hexadecimal: ")
                myDecimal = firstBinary.binaryToDecimal(enteredBinaryValue)
                hexadecimalFromDecimal = firstBinary.decimalToHexa(
                    myDecimal)

                print("-----------------------------------------------------")
                print("")
                print(
                    f'{fg("orchid")}{attr("bold")}BINARY      HEXADECIMAL\n[ {enteredBinaryValue} ]   ====>    [ {hexadecimalFromDecimal} ] {attr("reset")}')
                print("")
                print('-----------------------------------------------------')

            elif fromBinaryTo == 2:
                print("------------------------------------------------------------\n ---THIS CALCULATION IS FROM BINARY - OCTAL--\n------------------------------------------------------------\n")
                enteredBinaryValue = input(
                    "Enter your binary value to convert to octal: ")
                myDecimal = firstBinary.binaryToDecimal(enteredBinaryValue)
                hexadecimalFromDecimal = firstBinary.decimalToOctal(
                    myDecimal)

                print("-----------------------------------------------------")
                print("")
                print(
                    f'{fg("orchid")}{attr("bold")}BINARY      OCTAL\n[ {enteredBinaryValue} ]   ====>    [ {hexadecimalFromDecimal} ] {attr("reset")}')
                print("")
                print('-----------------------------------------------------')

            elif fromBinaryTo == 3:
                print("------------------------------------------------------------\n ---THIS CALCULATION IS FROM BINARY - DECIMAL--\n----------------------------------------------------------\n")
                enteredHexadecimalToDecimal = input(
                    "Enter your binary value that you want to convert to Decimal: ")
                gottenDecimal = firstBinary.binaryToDecimal(
                    enteredHexadecimalToDecimal)
                print("-----------------------------------------------------")
                print("")
                print(
                    f'{fg("orchid")}{attr("bold")}BINARY             DECIMAL\n[ {enteredHexadecimalToDecimal} ]   ====>      [ {gottenDecimal} ] {attr("reset")}')
                print("")
                print('-----------------------------------------------------')

            else:
                print("Make sure you enter a valid binary value !!")
                continue
            cont = input("Continue?: ").lower().strip()

            if cont == "yes":
                continue
            else:
                break

    elif choice == 4:
        while True:
            fromDecimalValueTo = int(input(
                "       From Decimal to:\n        1. Hexadecimal\n        2. Octal\n        3. Binary\n\n      Type your choice here: "))

            if fromDecimalValueTo == 1:
                print("------------------------------------------------------------\n ---THIS CALCULATION IS FROM DECIMAL - HEXADECIMAL--\n------------------------------------------------------------\n")
                decimal_to_be_transformed = input(
                    "Enter your decimal value to convert to hexadecimal: ")
                hexadecimalValueGotten = firstBinary.decimalToHexa(
                    decimal_to_be_transformed)

                print("-----------------------------------------------------")
                print("")
                print(
                    f'{fg("orchid")}{attr("bold")}DECIMAL      HEXADECIMAL\n[ {decimal_to_be_transformed} ]   ====>    [ {hexadecimalValueGotten} ] {attr("reset")}')
                print("")
                print('-----------------------------------------------------')

            elif fromDecimalValueTo == 2:
                print("------------------------------------------------------------\n ---THIS CALCULATION IS FROM DECIMAL - OCTAL--\n------------------------------------------------------------\n")
                decimal_to_be_transformed = input(
                    "Enter your decimal value to convert to octal: ")
                hexadecimalValueGotten = firstBinary.decimalToOctal(
                    decimal_to_be_transformed)

                print("-----------------------------------------------------")
                print("")
                print(
                    f'{fg("orchid")}{attr("bold")}DECIMAL      OCTAL\n[ {decimal_to_be_transformed} ]   ====>    [ {hexadecimalValueGotten} ] {attr("reset")}')
                print("")
                print('-----------------------------------------------------')

            elif fromDecimalValueTo == 3:
                print("------------------------------------------------------------\n ---THIS CALCULATION IS FROM DECIMAL - BINARY--\n------------------------------------------------------------\n")
                decimal_to_be_transformed = input(
                    "Enter your decimal value to convert to binary: ")
                hexadecimalValueGotten = firstBinary.decimalToBinary(
                    decimal_to_be_transformed)

                print("-----------------------------------------------------")
                print("")
                print(
                    f'{fg("orchid")}{attr("bold")}DECIMAL      BINARY\n[ {decimal_to_be_transformed} ]   ====>    [ {hexadecimalValueGotten} ] {attr("reset")}')
                print("")
                print('-----------------------------------------------------')

            else:
                print("Make sure you enter a valid decimal value !!")
                continue
            cont = input("Continue?: ").lower().strip()

            if cont == "yes":
                continue
            else:
                break
