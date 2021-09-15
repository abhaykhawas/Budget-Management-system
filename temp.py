import json

class Budget(object):
  def __init__(self,salary , food, cloothing, entertainment, savings, mob):
    self.salary = salary
    self.food = food
    self.cloothing = cloothing
    self.entertainment = entertainment
    self.savings = savings
    self.mob = mob

  def __str__(self):  
    return "---------------------------------------\nSalary: "+str(self.salary)+"\nFood: "+str(self.food)+"\nCloothing: "+str(self.cloothing)+"\nEntertainment: "+str(self.entertainment)+"\nSavings: "+str(self.savings)+"\nMobile number: "+str(self.mob)+"\n---------------------------------------"

  def jsonData(self):
    dict = {
             "Salary": self.salary,
             "Food": self.food,
             "Cloothing": self.cloothing,
             "Entertainment": self.entertainment,
             "Savings": self.savings,
             "Mob": self.mob
           }
    return dict


print("Welcome to Budget management system")


while True:
  try:
    usr = int(input("What do you want to do select from the option below\n1.Add your Data\n2.See your current budget management\n3.Exit\n"))
  except ValueError:
    print("Please enter 1/2/3")  
    continue
  
  if(usr == 1):
    try:
      s = int(input("Enter your salary: "))
    except ValueError:
      print("Please enter ints")
      continue
    mob = int(input("Enter your mobile number"))
    f = 0.15*s
    c = 0.1*s
    e = 0.07*s
    sav = 0.4*s

    budget = Budget(s,f,c,e,sav,mob)

    with open("budget.json", "r") as file:
        data = json.load(file)
    
    flag = 0

    for i in range(len(data)):
      if(data[i]['Mob'] == mob):
        print("Number exsists, Try again!!!!")
        flag = 1  
        break


    if flag == 0:
        data.append(budget.jsonData())    

        with open("budget.json", "w") as outfile:
            json.dump(data, outfile)

        print("Data stored!!!!!") 

    cont = input("Do you want to continue(y or n): ")
    if(cont == 'y'):
      continue
    else:
      break     





  elif(usr == 2):
    mob = int(input("Enter your registered mob number: "))

    with open("budget.json", "r") as file:
      data = json.load(file)

    flag = 0

    for i in range(len(data)):
      if(data[i]['Mob'] == mob):
        flag = 1  
        break  
      else:
        print("Number does not exsists, Try again!!!!")
        break  

    if flag == 1:
      for i in range(len(data)):
        if(data[i]['Mob'] == mob):
          budget = Budget(data[i]['Salary'],data[i]['Food'],data[i]['Cloothing'],data[i]['Entertainment'],data[i]['Savings'],data[i]['Mob'])
          print(budget)
          break
    cont = input("Do you want to continue(y or n): ")
    if(cont == 'y'):
      continue
    else:
      break        

  elif usr == 3:
    print("Bye!!!! Hope to see you soon")
    break

  else:
    print("Invalid Input!!!")  
    break    