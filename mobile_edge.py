import subprocess
import time
import tkinter
from random_word import RandomWords

# Create an instance of RandomWords
r = RandomWords()

def showpopup():
    root = tkinter.Tk()
    root.title('Message')
    root.geometry('400x250')
    # Lift the window to the top
    root.lift()
    root.attributes('-topmost', True)
    message = tkinter.Label(root, text='Task is done')
    message.pack(pady=20)
    okbutton = tkinter.Button(root, text='OK', command=root.destroy)
    okbutton.pack(pady=10)
    root.mainloop()

def adb_command(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result.stdout

def adb_tap(x, y):
    adb_command(f"adb shell input tap {x} {y}")

def adb_input_text(text):
    adb_command(f'adb shell input text "{text}"')

def adb_key_event(keycode):
    adb_command(f"adb shell input keyevent {keycode}")

def open_app(package_name):
    if package_name ==1 or package_name==2:
        secure_folder(package_name)

    else:
        generated_words = [r.get_random_word() for _ in range(1)]
        if package_name=="com.microsoft.bing":
            command= f"adb shell monkey -p {package_name} -c android.intent.category.LAUNCHER 1"
            adb_command(command)
            time.sleep(2)
            adb_tap(723, 2196) #bing new tab pre
            time.sleep(2)
            adb_tap(960, 2004) #bing new tab
            time.sleep(2)
            adb_input_text(generated_words[0])
        else:
            command= f"adb shell monkey -p {package_name} -c android.intent.category.LAUNCHER 1"
            adb_command(command)
            time.sleep(2)
            adb_tap(753, 2221)#edge new tab pre
            time.sleep(2)
            adb_tap(552, 2229)#edge new tab 
            time.sleep(2)
            adb_tap(347, 1243) #edge search tap
            time.sleep(2)
            adb_input_text(generated_words[0])

def secure_folder(namee):
    # swipe home
    adb_command(f'adb shell input swipe 605 2332 565 1520')
    time.sleep(0.8)
    # swipe up
    adb_command(f'adb shell input swipe 573 1523 770 1064')
    time.sleep(1.5)
    # tap S folder
    adb_tap(687, 2240)
    time.sleep(0.8)
    adb_tap(920, 787)
    time.sleep(1)
    adb_tap(518, 1407)
    time.sleep(0.8)
    adb_input_text(2485)
    adb_tap(885, 2042)
    time.sleep(2)
    #S 
    generated_words = [r.get_random_word() for _ in range(1)]
    if namee ==1:
        adb_tap(667, 2100)
        time.sleep(3)
        adb_tap(723, 2196) #bing new tab pre
        time.sleep(2)
        adb_tap(960, 2004) #bing new tab
        time.sleep(2)
        adb_input_text(generated_words[0])
    else:
        adb_tap(153, 2087)
        time.sleep(3)
        adb_tap(750, 2210)#edge new tab pre
        time.sleep(2)
        adb_tap(540, 2228)#edge new tab 
        time.sleep(2)
        adb_tap(342, 1230) #edge search tap
        time.sleep(0.5)
        adb_input_text(generated_words[0])

apps=[1, 2, "com.microsoft.bing", "com.microsoft.emmx" ] #Package name in your Android device

def searches():
    # Number of words to generate
    num_words = 1
    execu = 21
    bing_search_bar_x = 300  # Example value, change to the actual x-coordinate
    bing_search_bar_y = 200  # Example value, change to the actual y-coordinate
    for i in range(0, execu):
        # Generate words
        generated_words = [r.get_random_word() for _ in range(num_words)]
        
        # Tap on the Bing search bar
        adb_tap(bing_search_bar_x, bing_search_bar_y)
        time.sleep(1)  # Wait for the search bar to get focus

        # clear the searched word
        adb_tap(1000, 200)

        # Enter the word and press Enter
        adb_input_text(generated_words[0])
        time.sleep(0.3)
        adb_key_event(66)  # Press Enter
        
        print(generated_words[0])
        execu -= 1
        time.sleep(10)  # Wait for the search results to load
    
for app in apps:
    open_app(app)
    searches()
    time.sleep(2)

showpopup()
