
import pywhatkit as pw
import pyautogui
import time
import pyfiglet
from colorama import init, Fore, Style
init(autoreset=True)

def countdown(seconds,phone_number,message):
    for remaining in range(seconds, 0, -1):
        # Clear the screen
        print("\033c", end="")
        print(f"{Fore.LIGHTGREEN_EX + Style.BRIGHT  } Message sending delay {seconds}sec")
    # Schedule the message
        # phone_number = "+91"+phone_number
        print(f"{Fore.CYAN + Style.BRIGHT  } phone no = +91 {phone_number} \n Massage =  { message}  \n    time =  { str(seconds)} sec")

        # Create the countdown banner
       
        banner = pyfiglet.figlet_format("time countdown  "+str(remaining), font="digital")
        # Print the countdown banner in green
        print(Fore.GREEN + Style.BRIGHT + banner)

        # Wait for one second
        time.sleep(1)

    # Clear the screen for the final message
    print("\033c", end="")

    # Print the final message
    final_message = pyfiglet.figlet_format("msg send", font="digital")
    print(Fore.RED + Style.BRIGHT + final_message)


def _priunt_msg():
    init(autoreset=True)
    # Print banner
    banner = pyfiglet.figlet_format("WP Bomber")  # Use a larger font style
    print(Fore.MAGENTA + Style.BRIGHT + "----------------------------------------------------------------------------------")
    print(Fore.GREEN + Style.BRIGHT + banner)  # Change color and style
    print(Fore.MAGENTA + Style.BRIGHT + "----------------------------------------------------------------------------------")
    print(Fore.RED + Style.BRIGHT + "created by drx  \t you can send whatsapp spam msg (bomber)")  # Change color and style


def clear_tab():
    pyautogui.hotkey('ctrl','w')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(2)

  
while True:
    print("\033c", end="")
    _priunt_msg()
    print(Fore.GREEN + Style.BRIGHT + "----------------------------------------------------------------------------------")
    print(Fore.GREEN + Style.BRIGHT + "----------------------------------------------------------------------------------")
    
    # Get user inputs
    phone_number = input("Enter the phone number (without country code, e.g., XXXXXXXXXX): ")
    message = input("Enter the message: ")
    delay_minutes = int(input("Enter the delay time in seconds: "))
    num_messages = int(input("enter no. of total msg you want to send "))


    phone_number = "+91"+phone_number
    print(f"{Fore.CYAN + Style.BRIGHT  } phone no = {phone_number} \n Massage =  { message}  \n    time =  { str(delay_minutes)} sec")
    # countdown(delay_seconds,phone_number,message,send_hour,0)
    print("pleass wait...........")
    for i in range(num_messages):
        # time.sleep(5)
        countdown(delay_minutes,phone_number,message)
        pw.sendwhatmsg_instantly(phone_number, message)
        time.sleep(4)
        clear_tab()
    # time.sleep(5)
    print('Message successfully delivered')
    if int(input("press 0 for exit or 1 for continue .. ")) == 0:
        break
