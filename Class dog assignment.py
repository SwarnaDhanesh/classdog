class Dog:
     def __init__(self,Name,Age,Coat_color):
           self.Name=Name
           self.Age=Age
           self.Coat_color=Coat_color
     def Description(self,Name,Age):
           self.Name=Name
           self.Age=Age
           print("The description of the Dog and its Child classes are:")
           return(f"The name of the dog is {self.Name} and It is {self.Age} year old.")
     def Getinfo(self):
          return("The Coat Color of the Dog is White.")
          pass
class JackRussellTerrier(Dog):
    def Dog_details(self):
        return (f"The name of the dog  is {self.Name}. It is {self.Age} years old and It's Coat Color is {self.Coat_color}.")
    def Speak(self, sound="Arff!!"):
     return f"{self.Name},says {sound}"
    def Eating(self):
      return "It is Hungry."
    def Barking(self):
     return "It makes Woof!!"
class Bulldog(Dog):
      def Dog_details(self):
        return (f"The name of the dog is {self.Name}. It is {self.Age} years old. It's Coat color is {self.Coat_color}")
      def Speak(self, sound="Grr!!"):
        return f"{self.Name},says {sound}"
      def Run(self):
         return "It is Running"
      def Bite(self):
       return "It is Biting"
       
Tomy = Dog("Name","Age","Coat_color")
print(Tomy.Description("Tomy",1))
print(Tomy.Getinfo())
Ringo=JackRussellTerrier("Ringo",5,"White")
Ringo.Speak()
print(Ringo.Dog_details())
print(Ringo.Speak())
print(Ringo.Barking())
print(Ringo.Eating())
Bella= Bulldog("Bella",3,"White")  
Bella.Speak()
print(Bella.Dog_details())
print(Bella.Speak())
print(Bella.Bite())
print(Bella.Run())
