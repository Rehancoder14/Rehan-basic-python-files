class employee:
    company = "Google"
    ecode = 120
    def getinfo(self):
        print("This employee works in Google")

class freelancer:
    company = "internshala"
    level = 2
    def upgrade_level(self):
        self.level= self.level + 1
        
class programmer(employee,freelancer): 
    name = "Rehan"

p = programmer()
print(p.name)
print(p.company)
print(p.ecode)
p.upgrade_level()
print(p.level)





