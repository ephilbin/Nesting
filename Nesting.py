def analyze_input(user_input):
    #Check if the entered string is a number
    if user_input.isdigit():
        #Check if the number is even or odd
        number = int (user_input)
        if number % 2 == 0:
            return f"{number} is an even number."
        else:
            return f"{number} is an odd number."
    else:
        #Check if the entered string is all uppercase 
        if user_input.isupper():
            return "The input is in uppercase."
        else:
            return "The input is neither a number nor in uppercase"
            
#Accept user input
user_input = input("Enter a number or a string:")

#Process and display output
output_result = analyze_input(user_input)
print("Output:", output_result)