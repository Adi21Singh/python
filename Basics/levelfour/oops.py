class Phone:
    "A simple class for test"
    phone_version = "S10"
    brand_name = "Samsung"
    user_name = ""
    
    #model = "S10+"
    def get_model(self):
        # return self.model
        return "S10+"
    
    # def set_model(self, val):
    #     self.model = "S10+, " + val
        
    
    #constructor
    def __init__(self,user_name):
        self.user_name = user_name
    
    
    def BootLogo(self):
        print("Samsung", self.phone_version)
        
        
hitesh = Phone("Samsung")
hitesh.phone_version = "Nokia"

# hitesh.set_model("Iphone")
print(hitesh.get_model())


hitesh.__doc__

hitesh.BootLogo()