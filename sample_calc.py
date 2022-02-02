import json

def add(num1, num2):
    return num1 + num2
  
# Function to subtract two numbers 
def subtract(num1, num2):
    return num1 - num2
  
# Function to multiply two numbers
def multiply(num1, num2):
    return num1 * num2
  
# Function to divide two numbers
def divide(num1, num2):
    return num1 / num2

print("Please paste the data in JSON.")
json_input = input()
#json_input = {
  #"input1": 0.2,
  #"input2": 3,
  #"operator":"/"
#}
#print(json_input)
#with open("data.json", "w") as write_file:
    #json.dump(json_input, write_file)

#with open("data.json", "r") as read_file:
b = json.loads(json_input)
#print(b)
#print(type(b))
#for (k, v) in b.items():
   #print("Key: " + k)
   #print("Value: " + str(v))
c = b.items()
#print(c)
#print(type(c))
values = []
for d in c:
    values.append(d[1])
#print(values)
number_1 = values[0]
#print(number_1)
number_2 = values[1]
#print(number_2)
operator = values[2]
#print(operator)
#calc loops
sol_dict = {}
sol_list = []
if operator == '+':
    #print(number_1, "+", number_2, "=",
          #add(number_1, number_2))
    sol_dict["solution"] = add(number_1, number_2)
    #sol_list.append(add(number_1, number_2))
    #sol = add(number_1, number_2)
    #print(sol_list)

elif operator == '-':
    #print(number_1, "-", number_2, "=",
          #subtract(number_1, number_2))
    sol_dict["solution"] = subtract(number_1, number_2)

elif operator == '*':
    #print(number_1, "*", number_2, "=",
          #multiply(number_1, number_2))
    sol_dict["solution"] = multiply(number_1, number_2)
elif operator == '/':
    #print(number_1, "/", number_2, "=",
          #divide(number_1, number_2))
    sol_dict["solution"] = divide(number_1, number_2)
else:
    print("Invalid input")

#sol_dict["solutin"] = []
#sol_dict.update({"solutin": sol_list})
#print(sol_dict)
json_output = json.dumps(sol_dict)
print(json_output)
#data = json.load(input)
#def
#for (a, b, c,) in data.items():
    #print(a)
    #print(b)
    #print(C)

#print(data)














