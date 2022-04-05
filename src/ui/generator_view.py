from tkinter import ttk, constants, StringVar
from application.playlist_functionality import Playlist_Gen

class GeneratorView:
    def __init__(self, root):
        self._root = root
        self._frame = None

        self._initialize()

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        label1 = ttk.Label(master=self._frame, text="Pick a playlist")
        label2 = ttk.Label(master=self._frame,
                           text="The new playlist will be based off:")

        username_var = StringVar()
        username_label = ttk.Label(master=self._frame, text="Username:")
        username_entry = ttk.Entry(master=self._frame, text="")

        playlist_name_var = StringVar()
        playlist_name_label = ttk.Label(master=self._frame, text="Playlist name:")
        playlist_name_entry = ttk.Entry(master=self._frame, text="")

        playlist_desc_var = StringVar()
        playlist_desc_label = ttk.Label(master=self._frame, text="Playlist description:")
        playlist_desc_entry = ttk.Entry(master=self._frame, text="")
        
        pl_name_get = playlist_name_var.get
        pl_desc_get = playlist_desc_entry.get
    
        plg = Playlist_Gen(pl_name_get,pl_desc_get)
        button_auth = ttk.Button(
            master=self._frame,
            text="Authenticate",command=plg.get_token())
        button_gen = ttk.Button(
            master=self._frame,
            text="Generate playlist",command=plg.create_playlist())





        label1.grid(row=0, column=0)
        label2.grid(row=1, column=0)
        username_label.grid(row=2, column=0)
        username_entry.grid(row=2, column=1)
        playlist_name_label.grid(row=3, column=0)
        playlist_name_entry.grid(row=3, column=1)
        playlist_desc_label.grid(row=4, column=0)
        playlist_desc_entry.grid(row=4, column=1)
        button_auth.grid(row=5,column=1)
        button_gen.grid(row=5, column=0)


    def pack(self):
        self._frame.pack(fill=constants.X)
