open("data", "w").write(f'Name: {input("Your Name: ")}\nSurname: {input("Your Surname: ")}\nGender: {input("Your gender: ")}\nUsername: {input("Your username: ")}\nJob: {input("Your job: ")}')
print({item.split(": ")[0]:item.split(": ")[1] for item in open("data").read().split("\n")})
