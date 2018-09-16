#!/usr/bin/python

Amount_of_items = input("Vul hier het aantal items in: ")

if Amount_of_items == str(1):
    Eerste_Item = input("Prijs item 1 is: ")
    Subtotaal = Eerste_Item
    Taxpercentage = 0.07
    Tax = float(Taxpercentage) * float(Subtotaal)
    Eindtotaal = float(Subtotaal) * (1 + float(Taxpercentage))
    print("Het subtotaal bedraagt "+str(Subtotaal)+" euro")
    print("De tax bedraagt "+str(Tax)+" euro")
    print("Het eindtotaal bedraagt "+str(Eindtotaal)+" euro")
elif Amount_of_items == str(2):
    Eerste_Item = input("Prijs item 1 is: ")
    Tweede_Item = input("Prijs item 2 is: ")
    Subtotaal = float(Eerste_Item) + float(Tweede_Item)
    Taxpercentage = 0.07
    Tax = float(Taxpercentage) * float(Subtotaal)
    Eindtotaal = float(Subtotaal) * (1 + float(Taxpercentage))
    print("Het subtotaal bedraagt "+str(Subtotaal)+" euro")
    print("De tax bedraagt "+str(Tax)+" euro")
    print("Het eindtotaal bedraagt "+str(Eindtotaal)+" euro")
elif Amount_of_items == str(3):
    Eerste_Item = input("Prijs item 1 is: ")
    Tweede_Item = input("Prijs item 2 is: ")
    Derde_Item = input("Prijs item 3 is: ")
    Subtotaal = float(Eerste_Item) + float(Tweede_Item)+ float(Derde_Item)
    Taxpercentage = 0.07
    Tax = float(Taxpercentage) * float(Subtotaal)
    Eindtotaal = float(Subtotaal) * (1 + float(Taxpercentage))
    print("Het subtotaal bedraagt "+str(Subtotaal)+" euro")
    print("De tax bedraagt "+str(Tax)+" euro")
    print("Het eindtotaal bedraagt "+str(Eindtotaal)+" euro")
elif Amount_of_items == str(4):
    Eerste_Item = input("Prijs item 1 is: ")
    Tweede_Item = input("Prijs item 2 is: ")
    Derde_Item = input("Prijs item 3 is: ")
    Vierde_Item = input("Prijs item 4 is: ")
    Subtotaal = float(Eerste_Item) + float(Tweede_Item)+ float(Derde_Item)+ float(Vierde_Item)
    Taxpercentage = 0.07
    Tax = float(Taxpercentage) * float(Subtotaal)
    Eindtotaal = float(Subtotaal) * (1 + float(Taxpercentage))
    print("Het subtotaal bedraagt "+str(Subtotaal)+" euro")
    print("De tax bedraagt "+str(Tax)+" euro")
    print("Het eindtotaal bedraagt "+str(Eindtotaal)+" euro")
elif Amount_of_items == str(5):
    Eerste_Item = input("Prijs item 1 is: ")
    Tweede_Item = input("Prijs item 2 is: ")
    Derde_Item = input("Prijs item 3 is: ")
    Vierde_Item = input("Prijs item 4 is: ")
    Vijfde_Item = input("Prijs item 5 is: ")
    Subtotaal = float(Eerste_Item) + float(Tweede_Item)+ float(Derde_Item)+ float(Vierde_Item)+ float(Vijfde_Item)
    Taxpercentage = 0.07
    Tax = float(Taxpercentage) * float(Subtotaal)
    Eindtotaal = float(Subtotaal) * (1 + float(Taxpercentage))
    print("Het subtotaal bedraagt "+str(Subtotaal)+" euro")
    print("De tax bedraagt "+str(Tax)+" euro")
    print("Het eindtotaal bedraagt "+str(Eindtotaal)+" euro")
elif Amount_of_items == str(6):
    Eerste_Item = input("Prijs item 1 is: ")
    Tweede_Item = input("Prijs item 2 is: ")
    Derde_Item = input("Prijs item 3 is: ")
    Vierde_Item = input("Prijs item 4 is: ")
    Vijfde_Item = input("Prijs item 5 is: ")
    Zesde_Item = input("Prijs item 6 is: ")
    Subtotaal = float(Eerste_Item) + float(Tweede_Item)+ float(Derde_Item)+ float(Vierde_Item)+ float(Vijfde_Item)+ float(Zesde_Item)
    Taxpercentage = 0.07
    Tax = float(Taxpercentage) * float(Subtotaal)
    Eindtotaal = float(Subtotaal) * (1 + float(Taxpercentage))
    print("Het subtotaal bedraagt "+str(Subtotaal)+" euro")
    print("De tax bedraagt "+str(Tax)+" euro")
    print("Het eindtotaal bedraagt "+str(Eindtotaal)+" euro")
