from tkinter import Tk
from ui.UI import UI

# At this point the spotify username is a constant that defines it to my spotify account because i couldnt get the tKinter entry fields working
# Because of this the application cannot be accesed by other users at the moment

def main():

    window = Tk()
    window.title("Playlist Generator")

    ui = UI(window)
    ui.start()

    window.mainloop()

if __name__ == "__main__":
    main()

