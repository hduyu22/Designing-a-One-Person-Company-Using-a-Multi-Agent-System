class Founder:
    def __init__(self,name,task):
        self.name=name
        self.task=task
    def finaldecision(self):
        print("finaldecision:He is building an online store and working to grow his business through it.")

class Agent:
     def processtask(self):
      print("The agent performs is a task within the task.")

class MarketingAgent(Agent):
     def processtask(self):
      print("MarketingAgent is promotes the e-store and suggests methods to attractadditional customers.")
      print("Recommendations : He promoted my online store and suggested other ways for me to attract more customers.")

class OrderAgent(Agent):
     def processtask(self):
      print(" Order Agent is accountable for tracking and organizing customer requests throughthe system.")
      print("Recommendations :The system tracks and organizes customer orders.")

class ProductAgent(Agent):
     def processtask(self):
      print("Product Agent is manages the products in the store, adding new products and updating information related to the items.")
      print("Recommendations :It organizes products by adding new items and updating existing information.")
class AiAgent:
    def AI (self):
      print("This main operation is split up into three primary agents that each handle a different part of the e-store operations.")
      print()
      print("Marketing Agent: which studies the attractions of customers and market needs, and builds strategies to make it more visible to customers.")
      print()
      print("Order Agent: An order agent manages the purchases from customers by receiving, organizing, and routing orders properly and timely processing.")  
      print()
      print("The Product Agent: whose use cases are store inventory management, like adding new products and updating product details in order to keep product information accurate.")
      print()
      print("After task completion, all agents bring together their outputs into the same place. They feed artificial intelligence, and it reviews the records, information, and products, and finally saves them. ")

f=Founder("Elias","Start your own online business")
print("Founder Name:",f.name)
print()
print("Task Created:",f.task)
print()
a1=MarketingAgent()
a2=OrderAgent()
a3=ProductAgent()

a1.processtask()
print()
a2.processtask()
print()
a3.processtask()
print()
ai=AiAgent()
ai.AI()
print()
f.finaldecision()