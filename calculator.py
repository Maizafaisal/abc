while True:
     num1=int(input("Enter your first number"))
     num2=int(input("Enter your second number"))
     opt=int(input("""Choose opt
                1.add
                2.sub
                3.divide
                4.multiply
                5.percentage
                6.modulus"""))
     if opt==1:
      print(num1+num2)
     elif opt==2:
      print(num1-num2)
     elif opt==3:
      print(num1/num2)
     elif opt==4:
      print(num1*num2)
     elif opt==5:
      print(num1*num2/100)
     else:
      opt==6
      print(num1%num2)

     
