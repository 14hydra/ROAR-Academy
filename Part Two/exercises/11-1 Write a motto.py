with open("motto.txt", "w") as file:
    file.write("My motto goes here")

with open("motto.txt", "a") as file:
    file.write("\nLebron")

with open("motto.txt", "r") as file:
    updated_content = file.read()
    print(updated_content)