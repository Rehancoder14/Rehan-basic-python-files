class Train:
    def __init__(self,name, fare, seats,from_junction,to_junction):
        self.name = name
        self.fare = fare
        self.seats = seats
        self.from_junction = from_junction
        self.to_junction = to_junction
        
        
    def getstatus(self):
        print(f"The Train is going to travel from {self.from_junction} to {self.to_junction}\n")

        print(f"The name of the train is {self.name}\n")

        print(f"The fare of the train is ₹{self.fare}\n")


    def seatinfo(self):
        print(f"The seats available in the train is {self.seats}\n")
   
        

    def book_ticket(self):
        if (self.seats>0):
            print(f"Your ticket is booked and your seat number are {self.seats}😊😊")
            A = self.seats - 1
            print(A, "seats are available")
        else:
            print("Sorry, This Train is full. kindly try in tatkal section. 😅")


    def cancel_ticket(self):
        pass
    # @staticmethod
    # def cancel_ticket(seatno):
    #     print(f"{seatno} is cancelled")

    # def available_seats():
    #     B =  + 1
    #     print(f"The seat available after cancellation is {B} ")
   

 
        
Intercity = Train("Intercity express: 14002",500,2,"Pune Junction","Delhi Junction" )
Intercity.getstatus()
Intercity.book_ticket()
Intercity.book_ticket()
Intercity.seatinfo()






# nizammuddin = Train("nizammuddin express: 14014",400, 2,"Pune Junction","Bangalore Junction")
# nizammuddin.getstatus()
# nizammuddin.book_ticket()
