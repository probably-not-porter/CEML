from tkinter import filedialog
from tkinter import StringVar
from tkinter import *
import os

#other files
import ndvi




class SRSD_GUI:
    def __init__(self, master):
        self.master = master
        master.title("SRSD 0.0.1")
        self.detector_selection = [False,False,False]
        self.input_folder = None
        self.ndvi_folder = None

        # COLUMN 1
        col1_frame = Frame(root, bg='darkgray', width = 400, height=300, pady=20, padx=20).grid(row=0, column=0, columnspan=2, rowspan=10)
        self.img_label = StringVar()
        self.img_label.set("Input Folder: None")
        self.label1 = Label(master, text="Input Folder: None",textvariable=self.img_label).grid(row=0,column=0)
        self.select_folder_button = Button(master, text="Choose", command=self.select_img_folder).grid(row=0,column=1)

        self.createndvi_button = Button(master, text="Create NDVI", command=self.create_ndvi).grid(row=5,column=0)
        
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
        self.detector_selection = [self.var1.get(),self.var2.get(),self.var3.get()]
        print(self.detector_selection)
    
    def run(self):
        print('not set up yet')

    def select_img_folder(self):
        folder_selected = filedialog.askdirectory()
        self.input_folder = folder_selected
        self.ndvi_folder = folder_selected + "/ndvi"


        self.img_label.set("Input Folder: " + folder_selected)
        print(self.input_folder,self.ndvi_folder)
        

    def create_ndvi(self):
        try:
            os.mkdir(self.ndvi_folder)
        except OSError:
            print ("Creation of the directory %s failed" % self.ndvi_folder)
        
        for filename in os.listdir(self.input_folder):
            if (filename[-4:] == ".jpg") or (filename[-4:] == ".JPG") or (filename[-4:] == ".png"):
                print(filename)
                ndvi.createNDVI(str(self.input_folder) + "/" + str(filename), self.ndvi_folder + "/" + "ndvi_" + str(filename), False) # Enter the input JPG filename, Enter the output PNG filename, False


root = Tk()
my_gui = SRSD_GUI(root)
root.mainloop()
