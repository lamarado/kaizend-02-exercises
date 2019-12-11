# Challenge - Functions Exercise

# Create a function named tripleprint that takes a string as a parameter
# and prints that string 3 times in a row.
# So if I passed in the string "hello",
# it would print "hellohellohello"

def tripleprint(input_string):
    print("{}{}{}".format(input_string, input_string, input_string))

tripleprint("hello")