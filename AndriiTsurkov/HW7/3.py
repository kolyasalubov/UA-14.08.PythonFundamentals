# Write a function that calculates the number of caracters included in given string 

def number_of_characters(given_string):

    given_string = list(given_string)
    result_dictonary = {}
 
    for symbol in given_string:
        if symbol not in result_dictonary.keys():
            result_dictonary[symbol] = given_string.count(symbol)
    
    return result_dictonary


print("Dictnary of characters:", number_of_characters("hello"))
