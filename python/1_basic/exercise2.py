# If Statements and Comments Exercise

# Make an if-else statement if year is between 2000 and 2100
# (including both numbers), then print out:
# "Welcome to the 21st century"
# Else print out:
# "You are before or after the 21st century"

year = 1830
output = ""
if year >= 2000 and year <= 2100:
    output = "Welcome to the 21st century"
else:
    output = "You are before or after the 21st century"
print(output)