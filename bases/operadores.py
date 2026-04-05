
first_number = 29
second_number = 8

addition = first_number + second_number
substraction = first_number - second_number
int_division = first_number // second_number
division = first_number / second_number
pow_number = first_number ** second_number

print(f"Add: {addition}, Sub: {substraction}, Int_div: {int_division}, Division: {division}, Exp: {pow_number}")

print("{:,}".format(pow_number).replace(",","."))

remainder = first_number % second_number
print(f"Remainder: {remainder}")



# Strings

first_str = "Hola"
second_str = " "
third_str = "Python!"

rep_str = first_str * 5
rep_first_letter = third_str[0] * 4

# Lists

first_elements = [2,5,7,3,9,4]
second_elements = [4,7, 3, 6, 7]

union = first_elements + second_elements
print(union)

x_coordenates = [1,3,5,7,9]
y_coordenates = [2,4,6,8,10]

union_numbers = zip(x_coordenates, y_coordenates)
for coordenate in union_numbers:
    print(coordenate)

result_map = list(map(sum, zip(x_coordenates, y_coordenates)))
for coordenate in result_map:
    print(coordenate)

print(result_map)