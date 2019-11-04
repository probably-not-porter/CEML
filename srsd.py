from tkinter import filedialog
from tkinter import StringVar
from tkinter import *
import ndvi

detector_selection = [False,False,False]
input_folder = None
ndvi_folder = None

class SRSD_GUI:
    def __init__(self, master):
        self.master = master
        master.title("SRSD 0.0.1")

        # COLUMN 1
        col1_frame = Frame(root, bg='darkgray', width = 300, height=300, pady=20, padx=20).grid(row=0, column=0, columnspan=1, rowspan=10)
        self.img_label = StringVar()
        self.img_label.set("Input Folder: None")
        self.label1 = Label(master, text="Input Folder: None",textvariable=self.img_label).grid(row=0,column=0)
        self.select_folder_button = Button(master, text="Choose", command=self.select_img_folder).grid(row=1,column=0)

        self.ndvi_label = StringVar()
        self.ndvi_label.set("NDVI Folder: None")
        self.label12 = Label(master, text="NDVI Folder: None",textvariable=self.ndvi_label).grid(row=3,column=0)
        self.select_ndvi_button = Button(master, text="Choose", command=self.select_ndvi_folder).grid(row=4,column=0)

        self.createndvi_button = Button(master, text="Create NDVI", command=self.run).grid(row=5,column=0)
        
        # COLUMN 2
        col2_frame = Frame(root, bg='darkgray', width = 250, height=300, pady=20, padx=20).grid(row=0, column=2, columnspan=1, rowspan=10)
        self.label3 = Label(master, text="Select Edge Detector:").grid(row=0,column=2)
        self.var1 = IntVar()
        Checkbutton(master, text="Canny Detector", variable=self.var1,command=self.cb).grid(row=1, column=2, sticky=W)
        self.var2 = IntVar()
        Checkbutton(master, text="Marr-Hildreth Detector", variable=self.var2,command=self.cb).grid(row=2, column=2, sticky=W)
        self.var3 = IntVar()
        Checkbutton(master, text="Sobel Detector", variable=self.var3,command=self.cb).grid(row=3, column=2, sticky=W)
        # COLUMN 3

        self.greet_button = Button(master, text="RUN", command=self.run).grid(row=1,column=4)

        self.close_button = Button(master, text="Close", command=master.quit).grid(row=2,column=4)

    def cb(self):
        detector_selection = [self.var1.get(),self.var2.get(),self.var3.get()]
        print(detector_selection)
    
    def run(self):
        print('not set up yet')

    def select_img_folder(self):
        folder_selected = filedialog.askdirectory()
        input_folder = folder_selected
        self.img_label.set("Input Folder: " + input_folder)
        
    def select_ndvi_folder(self):
        folder_selected = filedialog.askdirectory()
        ndvi_folder = folder_selected
        self.ndvi_label.set("NDVI Folder: " + ndvi_folder)

    def create_ndvi(self):
        #for each file
        ndvi.createNDVI() # Enter the input JPG filename, Enter the output PNG filename, False


root = Tk()
my_gui = SRSD_GUI(root)
root.mainloop()
