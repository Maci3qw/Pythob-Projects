#slownik = {"audi" : "białe", "bmw" : "czarne", "mercedes":"szary"}
#print(slownik["mercedes"])

#slownik["skoda"] = "zielona"

#print(slownik)
def feedback():
       film = input("Jaki film chcesz dodać? ")
       ocena = input("Jaka ocena? ")
       netflix[film]=ocena
       print("Dodałeś pomyślnie feedback!") 
       print(f"Oto nasza biblioteka: {netflix}")
        

netflix = {"Suits":"10", "House of Cards":"6", "The Crown":"9", "Narcos":"7", "Pitbull":"1"}

ask = input("Jaki serial chcesz obejrzeć?   ")

match ask:
        case "Suits":
                print(f"Wybrałeś serial: {ask}")
                print("Ocena serialu:   " + netflix["Suits"])
        case "House of Cards":
                  print(f"Wybrałeś serial: {ask}")
                  print("Ocena serialu:   " + netflix["House of Cards"])
        case "The Crown":
                  print(f"Wybrałeś serial: {ask}")
                  print("Ocena serialu:   " + netflix["The Crown"])
        case "Narcos":
                  print(f"Wybrałeś serial: {ask}")
                  print("Ocena serialu:   " + netflix["Narcos"])
        case "Pitbull":
                  print(f"Wybrałeś serial: {ask}")
                  print("Ocena serialu:   " + netflix["Pitbull"])

score = input("Chcesz dodać film i go ocenić? ")

if score == "Nie":
        print("Dziękuję za skorzystanie z naszych usług")
        quit()
else: 
        feedback()