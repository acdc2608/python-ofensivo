
# Inmutables

example = (1,2,3,4,5)

# example[2] = 13

a,b,c,d,e = example

print(a,b,c)

my_second_tuple = (6,7,8,9)
my_third_tuple = example + my_second_tuple

print(my_third_tuple)

even_numbers = tuple(elem for elem in my_third_tuple if elem % 2 == 0)

db1_credential = ("acdc2608", "134534")
db2_crednetial = ("hack4u", "Password")

try:
    db1_credential[0] = db2_crednetial[0]
except:
    print("No se pueden manipular tuples")