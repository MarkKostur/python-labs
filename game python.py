import time

def start_game():
    print("Привіт! Вітаємо в квест-грі")
    time.sleep(1)
    print("Ви опинились в лісі і перед вами розгалуження шляхів")
    time.sleep(1)
    print("1. Оберіть лівий шлях.\n2.Оберіть правий шлях.\n")
    
    choice = input("Введіть 1 чи 2: ")
    
    if choice == "1":
        house()
    elif choice == "2":
        castle()
    else:
        print("Ваш вибір неможливй.Введіть 1 або 2.")
        start_game()

def house():
    print("\nВи вбрали лівий шлях та зустрічаєте будинок та заходите в нього і бачите банду злочинців")
    print("Що ви зробите з ними?\n1.Втечете\n2.Поб'єте їх\n")
    
    choice = input("Введіть 1 чи 2: ")
    
    if choice == "1":
        print("\nВи вийшли з будинку і почуваєтесь в безпеці.\nПроте злочинці вас побачили і йдуть а вами.")
        print("1.Ви втікаєте дальше.\n2.Ви вирішили зібратись з силами і побити їх.\n")
        choice = input("Ваш вибір: ")
        if choice == "1":
           print("\nЗлодії вас побили. Ви програли!")
        elif choice == "2":
            print("\nВи побили злочинців! Ви виграли!")
            
    elif choice == "2":
        print("\nВи вирішили побити їх.\nВи підбігаєте до головного, а решта забоялись і втікають.\n1.Вдарити головного злончинця ногою\n2.Вдарити головного злонця кулаком\n")
        choice = input("Введіть 1 чи 2: ")
        if choice == "1":
            print("\nВи його повалили і він впав на спину, і не може встати! Ви пройшли гру, вітаємо вас!")
        elif choice == "2":
            print("\nВи попали йому в голову і він втрати свідомість! Ви пройшли гру, вітаємо вас!")
    
    else:
        print("Ваш вибір неможливй.Введіть 1 або 2.")
        house()

def castle():
    print("\nВи вбрали лівий шлях та зустрічаєте замок та заходите в нього і бачите там гномів.\nЩо ви скажете гномам?\n1.'Я ваш король'. і вони вірять вам.\n2.Я просто гість і хочу подивитись на ваше королівство")
    
    choice = input("Введіть 1 чи 2: ")
    
    if choice == "1":
        print("\nГноми вам повірили\nЧи будете ви дійсно їхнім королем?\n1.Так\n2.Ні")
        choice = input("Введіть 1 чи 2: ")
        if choice == "1":
            print("\nВітаю ви стали королем гномів.Ви виграли!")
        elif choice == "2":
          print("\nВи чесна людина. Ви молодець!")
            
        
    elif choice == "2":
        print("\nВи ходите по замку і побачили золото.\nВаш вибір:\n1.Вкрасти його\n2.Продовжити екскурсію\n")
        choice = input("Введіть 1 чи 2: ")
        if choice == "1":
            print("\nВи вкрали золото та гноми побачили це і посадили вас у в'язницю. Ви програли!")
        elif choice == "2":
            print("\nВи чесна людина! Молодець!")
    
        else:
          print("Ваш вибір неможливй.Введіть 1 або 2.")
          castle()
          
if __name__ == "__main__":
     start_game()