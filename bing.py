import pyautogui
from random_word import RandomWords
import time
import tkinter 
# Create an instance of RandomWords
r = RandomWords()

def showpopup():
    root=tkinter.Tk()
    root.title('message')
    root.geometry('400x250')
    # Lift the window to the top
    root.lift()
    root.attributes('-topmost', True)
    message=tkinter.Label(root, text='Task is done')
    message.pack(pady=20)
    okbutton=tkinter.Button(root, text='ok', command=root.destroy)
    okbutton.pack(pady=10)
    root.mainloop()

def bingPoints():
    # Number of words to generate
    num_words = 1
    time.sleep(5)
    execu=30
    wrds=5
    pyautogui.hotkey('ctrl', 't')
    pyautogui.hotkey('ctrl', 't')
    alter=0
    for i in range(0, execu):
        # Generate words
        generated_words = [r.get_random_word() for _ in range(num_words)]
        # pyautogui.click(961, 62)
        pyautogui.write(generated_words[0])
        time.sleep(0.3)
        pyautogui.press('enter')
        time.sleep(7)
        if alter==0:
            pyautogui.hotkey('ctrl', 'shift', 'tab')
            alter=1
        else:
            pyautogui.hotkey('ctrl', 'tab')
            alter=0
        if wrds==0:
            pyautogui.hotkey('ctrl', 'w')
            wrds=4
            alter=0
            pyautogui.hotkey('ctrl', 't')
            
            time.sleep(0.6)
        wrds -=1

        print(generated_words[0])
        execu -=1

nums=['2', '7', '8', '9'] #The taskbar postion of your edge apps
for i in range(len(nums)):
    pyautogui.hotkey('win', nums[i])
    bingPoints()
    pyautogui.hotkey('alt', 'f4')
showpopup()
