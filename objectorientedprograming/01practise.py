class programmer:
    company = "Microsoft"

    def __init__(self,name,product):
        self.name = name
        self.product = product
        
        print(f"The name of employee is {self.name}")
        print(f"The product of employee is {self.product}\n")
        

rehan = programmer("rehan","outlook")
sid = programmer("sid","msteams")
shubs = programmer("shubs","skype")