from modules import script
from colorama import init, Fore, Style
from random import randint
from os import system
from platform import uname
reset = Fore.RESET + Style.RESET_ALL
init()
def clear():
    plat = uname()[0].lower()
    if plat.startswith("win"): system("cls")
    else: system("clear")
def random_banner():
    banners = ["""
 ____    _       _____    ____            ____    ____    _      ___  _   ____    _    _       ____ 
/  _ \  / \ /\  /__ __\  /  _ \          /  __\  /  _ \  / \     \  \//  /  __\  / \  / \ /\  / ___\
| / \|  | | ||    / \    | / \|  _____   |  \/|  | / \|  | |      \  /   | | //  | |  | | ||  |    \
| |-||  | \_/|    | |    | \_/|  \____\  |  __/  | \_/|  | |_/\   / /    | |_\\  | |  | \_/|  \___ |
\_/ \|  \____/    \_/    \____/          \_/     \____/  \____/  /_/     \____/  \_/  \____/  \____/
                                                                                                    
""", """
  /$$$$$$        /$$   /$$       /$$$$$$$$        /$$$$$$                      /$$$$$$$         /$$$$$$        /$$             /$$     /$$       /$$$$$$$        /$$$$$$       /$$   /$$        /$$$$$$ 
 /$$__  $$      | $$  | $$      |__  $$__/       /$$__  $$                    | $$__  $$       /$$__  $$      | $$            |  $$   /$$/      | $$__  $$      |_  $$_/      | $$  | $$       /$$__  $$
| $$  \ $$      | $$  | $$         | $$         | $$  \ $$                    | $$  \ $$      | $$  \ $$      | $$             \  $$ /$$/       | $$  \ $$        | $$        | $$  | $$      | $$  \__/
| $$$$$$$$      | $$  | $$         | $$         | $$  | $$       /$$$$$$      | $$$$$$$/      | $$  | $$      | $$              \  $$$$/        | $$$$$$$         | $$        | $$  | $$      |  $$$$$$ 
| $$__  $$      | $$  | $$         | $$         | $$  | $$      |______/      | $$____/       | $$  | $$      | $$               \  $$/         | $$__  $$        | $$        | $$  | $$       \____  $$
| $$  | $$      | $$  | $$         | $$         | $$  | $$                    | $$            | $$  | $$      | $$                | $$          | $$  \ $$        | $$        | $$  | $$       /$$  \ $$
| $$  | $$      |  $$$$$$/         | $$         |  $$$$$$/                    | $$            |  $$$$$$/      | $$$$$$$$          | $$          | $$$$$$$/       /$$$$$$      |  $$$$$$/      |  $$$$$$/
|__/  |__/       \______/          |__/          \______/                     |__/             \______/       |________/          |__/          |_______/       |______/       \______/        \______/ 
""", """
 $$$$$$\        $$\   $$\       $$$$$$$$\        $$$$$$\                      $$$$$$$\         $$$$$$\        $$\             $$\     $$\       $$$$$$$\        $$$$$$\       $$\   $$\        $$$$$$\  
$$  __$$\       $$ |  $$ |      \__$$  __|      $$  __$$\                     $$  __$$\       $$  __$$\       $$ |            \$$\   $$  |      $$  __$$\       \_$$  _|      $$ |  $$ |      $$  __$$\ 
$$ /  $$ |      $$ |  $$ |         $$ |         $$ /  $$ |                    $$ |  $$ |      $$ /  $$ |      $$ |             \$$\ $$  /       $$ |  $$ |        $$ |        $$ |  $$ |      $$ /  \__|
$$$$$$$$ |      $$ |  $$ |         $$ |         $$ |  $$ |      $$$$$$\       $$$$$$$  |      $$ |  $$ |      $$ |              \$$$$  /        $$$$$$$\ |        $$ |        $$ |  $$ |      \$$$$$$\  
$$  __$$ |      $$ |  $$ |         $$ |         $$ |  $$ |      \______|      $$  ____/       $$ |  $$ |      $$ |               \$$  /         $$  __$$\         $$ |        $$ |  $$ |       \____$$\ 
$$ |  $$ |      $$ |  $$ |         $$ |         $$ |  $$ |                    $$ |            $$ |  $$ |      $$ |                $$ |          $$ |  $$ |        $$ |        $$ |  $$ |      $$\   $$ |
$$ |  $$ |      \$$$$$$  |         $$ |          $$$$$$  |                    $$ |             $$$$$$  |      $$$$$$$$\           $$ |          $$$$$$$  |      $$$$$$\       \$$$$$$  |      \$$$$$$  |
\__|  \__|       \______/          \__|          \______/                     \__|             \______/       \________|          \__|          \_______/       \______|       \______/        \______/ 
""", """
  ____      __ __      ______       ___                  ____        ___       _          __ __      ____       ____      __ __       _____
 /    |    |  |  |    |      |     /   \                |    \      /   \     | |        |  |  |    |    \     |    |    |  |  |     / ___/
|  o  |    |  |  |    |      |    |     |     _____     |  o  )    |     |    | |        |  |  |    |  o  )     |  |     |  |  |    (   \_ 
|     |    |  |  |    |_|  |_|    |  O  |    |     |    |   _/     |  O  |    | |___     |  ~  |    |     |     |  |     |  |  |     \__  |
|  _  |    |  :  |      |  |      |     |    |_____|    |  |       |     |    |     |    |___, |    |  O  |     |  |     |  :  |     /  \ |
|  |  |    |     |      |  |      |     |               |  |       |     |    |     |    |     |    |     |     |  |     |     |     \    |
|__|__|     \__,_|      |__|       \___/                |__|        \___/     |_____|    |____/     |_____|    |____|     \__,_|      \___|
""", """
 _______              _________   _______             _______    _______    _                     ______    _________              _______ 
(  ___  )  |\     /|  \__   __/  (  ___  )           (  ____ )  (  ___  )  ( \        |\     /|  (  ___ \   \__   __/  |\     /|  (  ____ \
| (   ) |  | )   ( |     ) (     | (   ) |           | (    )|  | (   ) |  | (        ( \   / )  | (   ) )     ) (     | )   ( |  | (    \/
| (___) |  | |   | |     | |     | |   | |   _____   | (____)|  | |   | |  | |         \ (_) /   | (__/ /      | |     | |   | |  | (_____ 
|  ___  |  | |   | |     | |     | |   | |  (_____)  |  _____)  | |   | |  | |          \   /    |  __ (       | |     | |   | |  (_____  )
| (   ) |  | |   | |     | |     | |   | |           | (        | |   | |  | |           ) (     | (  \ \      | |     | |   | |        ) |
| )   ( |  | (___) |     | |     | (___) |           | )        | (___) |  | (____/\     | |     | )___) )  ___) (___  | (___) |  /\____) |
|/     \|  (_______)     )_(     (_______)           |/         (_______)  (_______/     \_/     |/ \___/   \_______/  (_______)  \_______)
""", """
   (                *   )   ( /(          )\ )   ( /(    )\ )    ( /(     (    )\ )           )\ )  
   )\         (   ` )  /(   )\())        (()/(   )\())  (()/(    )\())  ( )\  (()/(      (   (()/(  
((((_)(       )\   ( )(_)) ((_)\    ___   /(_)) ((_)\    /(_))  ((_)\   )((_)  /(_))     )\   /(_)) 
 )\ _ )\   _ ((_) (_(_())    ((_)  |___| (_))     ((_)  (_))   __ ((_) ((_)_  (_))    _ ((_) (_))   
 (_)_\(_) | | | | |_   _|   / _ \        | _ \   / _ \  | |    \ \ / /  | _ ) |_ _|  | | | | / __|  
  / _ \   | |_| |   | |    | (_) |       |  _/  | (_) | | |__   \ V /   | _ \  | |   | |_| | \__ \  
 /_/ \_\   \___/    |_|     \___/        |_|     \___/  |____|   |_|    |___/ |___|   \___/  |___/  
""", """
   _____     ____ ___  ___________ ________              __________  ________    .____      _____.___. __________  .___   ____ ___    _________
  /  _  \   |    |   \ \__    ___/ \_____  \             \______   \ \_____  \   |    |     \__  |   | \______   \ |   | |    |   \  /   _____/
 /  /_\  \  |    |   /   |    |     /   |   \    ______   |     ___/  /   |   \  |    |      /   |   |  |    |  _/ |   | |    |   /  \_____  \ 
/    |    \ |    |  /    |    |    /    |    \  /_____/   |    |     /    |    \ |    |___   \____   |  |    |   \ |   | |    |  /   /        \
\____|__  / |______/     |____|    \_______  /            |____|     \_______  / |_______ \  / ______|  |______  / |___| |______/   /_______  /
        \/                                 \/                                \/          \/  \/                \/                           \/ 
"""]
    clear()
    rand = randint(0, (len(banners-1)))
    print(Fore.CYAN + banners[rand])
def get_info():
    try:
        dir = input(f"{Fore.WHITE}[{Fore.YELLOW}+{Fore.WHITE}] {Fore.GREEN}For decode a text write '{Fore.YELLOW}D{Fore.GREEN}', and for encode a text wirte '{Fore.YELLOW}E{Fore.GREEN}': {reset}").lower()
        if dir == "d": 
            text = input(f"{Fore.WHITE}[{Fore.YELLOW}+{Fore.WHITE}] {Fore.GREEN}Write the text to decode: {reset}")
            out = script.decode(text)
            print(out)
        elif dir == "e":
            text = input(f"{Fore.WHITE}[{Fore.YELLOW}+{Fore.WHITE}] {Fore.GREEN}Write the text to encode: {reset}")
            out = script.encode(text)
            print(out)
        else:
            print("Invalid Input.")
    except KeyboardInterrupt: exit(f"\n\n {Fore.CYAN}Good Luck{reset} \n\n")
    except: exit(f"\n\n {Fore.RED}Unknown error{reset} \n\n")
