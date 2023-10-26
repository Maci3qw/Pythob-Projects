import datetime
import time
import os

class todo:
        
        def __init__(self, lista_zadan=None):
                self.lista_zadan = [] 

        def dodaj_zadanie(self):
                while True:
                        print("Dodajemy zadanie")
                        zadanie = input("Podaj zadanie: ")
                        self.lista_zadan.append(zadanie)
                        print("Pomyślnie dodano zadanie!")
                        nastepne_zadanie = input("Chcesz dodać jeszcze jedno zadanie? (tak / nie)")
                        if nastepne_zadanie != "tak":
                                time.sleep(1)
                                return
                        print("Ponawiam dodawanie zadania..")       
                        time.sleep(1)
                    
        def wyswietl_zadania(self):
                print("Oto twoje aktualne zadania:")
                if not self.lista_zadan:
                            print("Twoja lista jest pusta")
                            
                else:
                    print(self.lista_zadan)
                    time.sleep(3)
                    
                nowe_zadanie = input("Czy chcesz coś dodać?")
                match nowe_zadanie:
                                    case "tak":
                                            self.dodaj_zadanie()
                                            print("Przenoszę do sekcji dodawania zadań..")
                                            time.sleep(1)

                                    case "nie":
                                            return
                                            
                time.sleep(2)

        def oznaczanie(self):
                print("Wykonane / Nie wykonane")

        def zapisz_do_pliku(self):
                print("Zapisuje do pliku")
        
        def odczytaj(self):
                print("Odczytuje plik...")
        
        def wyjdz(self):
                print("Do widzenia!")
                exit()
                
my_todo = todo()

while True:       
    print("\n\nWitamy w programie Notes2024!")
    print("----------")
    print("1: Dodaj zadanie" )
    print("2: Wyświetl liste zadań" )
    print("3: Oznacz jako wykonane" )
    print("4: Zapisz do pliku" )
    print("5: Odczytaj plik" )
    print("6: Wyjdź")
    print("----------")
    question = input("Co byś chciał dzisiaj zrobić?") 

   
    match question:
            case "1":
                    my_todo.dodaj_zadanie()
            
            case "2":
                    my_todo.wyswietl_zadania()
                
            case "3":
                my_todo.oznaczanie()
            case "4":        
                    my_todo.zapisz_do_pliku()
            case "5":
                    my_todo.odczytaj()
            case "6":
                    my_todo.wyjdz()