
#functions with output
#change the title of your string

def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return
    print(f_name.title())
    print(l_name.title())
fi_name = input("Enter your first name: ")
li_name = input("Enter your last name: ")

format_name(fi_name, li_name)
print(len(fi_name))
print(len(li_name))


