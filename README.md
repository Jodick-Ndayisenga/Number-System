This program allows the user to convert numbers either from Hexadecimal, Octal, Decimal, or Binary to either hexadecimal, 
octal or decimal numbers, based on the user's choice. The program continuously 
prompts the user to enter a number to convert and then prompts the user to choose the conversion type. 
After the conversion is made, the program displays the result and asks if the user wants to continue converting or exit.

It tarts with an infinite loop using while True:
Within the loop, the user is prompted to select the desired conversion option by entering 1 for hexadecimal, 
2 for octal, or 3 hexadecimal and 4 for decimal. The user's input is stored in the variable 
as integer datatype and will ultmately be used to perform several activities.

The program then uses if-elif-else statements to determine which conversion option the user selected. 
If the user selects 1, the program converts the entered binary number to hexadecimal using the 
binaryToDecimal() and decimalToHexa() methods of the firstBinary object. The resulting hexadecimal number is then printed to the console.

If the user selects 2, the program converts the entered binary number to octal using the binaryToDecimal() 
and decimalToOctal() methods of the firstBinary object. The resulting octal number is then printed to the console.

If the user selects 3, the program converts the entered binary number to decimal using the binaryToDecimal() 
method of the firstBinary object. The resulting decimal number is then printed to the console.

If the user enters an invalid input, the program will print an error message and prompt the user to continue or not. 
If the user enters "yes", the program will continue the loop, prompting the user for another conversion option. 
If the user enters any other input, the program will break out of the loop and end.
