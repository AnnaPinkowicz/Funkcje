def sprawdzam_palindrom(wyraz): 
    print(f" Wpisany przez Ciebie wyraz to >{wyraz}<")
    print("-----------------------")
    if wyraz.isalpha() !=True:
      print("Uwaga - wyraz moze zawierac tylko literki (nie znaki, czy spacje) wpisz jeszcze raz poprawnie!")
  
    print("-----------------------")
    
    wyraz = wyraz.lower()
    wyraz = wyraz.replace(" ","")
    #wyraz = wyraz.replace(",","")
    #wyraz = wyraz.replace(".","") 
    # POWYZSZE W SUMIE BEZ SENSU -MUSIALABYM WSZYSTKIE ZNAKI INTERPUNKCYJNE WYKLUCZYC jak znasz metode klasy string ktors usuwa znaki to bede wdzieczna
    print(f"Rozumiem, ze moglo Ci chodzic o wyraz >{wyraz}< - \n jak nie - wpisz ponownie!")
    if wyraz == wyraz[::-1]: 
      print(" Twoj wyraz jest palindromem!") 
      return True
    else:  
      print(" To cos nie jest palindromem \n ")
      return False 

    

while True:
  wyraz = input("Podaj mi jakis slowo do sprawdzenia\n(zaczynajac od malej litery prosze i \nbez znakow interpunkcyjnych): \n")
  print(sprawdzam_palindrom(wyraz))
  continue