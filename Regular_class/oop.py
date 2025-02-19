class my_car:
    def __init__(self,name,brand,model):
        self.name=name
        self.brand=brand
        self.model=model
    
    def info(self):
        print(f"Car name:{self.name}")
        print(f"Car brand:{self.brand}")
        print(f"Car model:{self.model}")

if __name__=="__main__":
    car_nm=input("Enter the name:")
    car_bnd=input("Enter the brand:")
    car_mdl=input("Enter the model:")
    car=my_car(car_nm,car_bnd,car_mdl)
    car.info()