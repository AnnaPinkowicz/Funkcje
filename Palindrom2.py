def sprawdzam_palindrom(word): 
  #word  =  word.upper
    if word == word[::-1]: 
      print("Jest palindromem!") 
      return True
    else:  
      print("Niestety nie jest palindromem")
      return False 
for x in range(1000): 
  word = input("Podaj mi jakis slowo do sprawdzenia: ")
  print(sprawdzam_palindrom(word))
  continue
#Wiec mam tu dwa problemy
#1. Kiedy string zaczyna sie z WIELKIEJ LITERY ? wtedy uznaje za nie-palindrom. Myslalam, ze to dzieki "upper/lower" zalatwie ale nie idzie.
#2. Chcialabym, aby funkcja po zakonczeniu sprawdzania pytala mnie BEZ KONCA. Prosze o pomoc