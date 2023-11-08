input_string=input("Enter a lot of words (yes, it has to be a sentence): ")
def string(input_string):
    words = input_string.split()
    reversed_string = ' '.join(reversed(words))
    print(reversed_string)
    
string(input_string)
    