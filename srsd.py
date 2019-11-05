from tkinter import filedialog
from tkinter import StringVar
from tkinter import *
import os
import time

#other files
import operations.ndvi as ndvi
import operations.edge_detectors as edge_detectors




class SRSD_GUI:
    def __init__(self, master):
        self.master = master
        master.title("SRSD 0.0.1")
        self.detector_selection = [False,False,False]
        self.input_folder = None
        self.ndvi_folder = None
        self.caney_folder = None
        self.images = 0

        # COLUMN 1
        col1_frame = Frame(root, bg='darkgray', width = 400, height=300, pady=20, padx=20).grid(row=0, column=0, columnspan=2, rowspan=10)
        self.img_label = StringVar()
        self.img_label.set("Input Folder: None")
        self.label1 = Label(master, text="Input Folder: None",textvariable=self.img_label)
        self.label1.grid(row=0,column=0)

        self.select_folder_button = Button(master, text="Choose", command=self.select_img_folder)
        self.select_folder_button.grid(row=0,column=1)

        self.ndvi_loading = StringVar()
        self.ndvi_loading.set("select folder...")
        self.ndvi_label = Label(master, text="",textvariable=self.ndvi_loading)
        self.ndvi_label.grid(row=6,column=0)
        
        self.ndvibutton = Button(master, text="Create NDVI", command=self.create_ndvi)
        self.ndvibutton.grid(row=5,column=0)
        
        # COLUMN 2
        col2_frame = Frame(root, bg='darkgray', width = 400, height=300, pady=20, padx=20).grid(row=0, column=2, columnspan=1, rowspan=10)
        self.label3 = Label(master, text="Select Edge Detector:")
        self.label3.grid(row=0,column=2)

        self.var1 = IntVar()
        Checkbutton(master, text="Canny Detector", variable=self.var1,command=self.cb).grid(row=1, column=2, sticky=W)
        self.var2 = IntVar()
        Checkbutton(master, text="Marr-Hildreth Detector", variable=self.var2,command=self.cb).grid(row=2, column=2, sticky=W)
        self.var3 = IntVar()
        Checkbutton(master, text="Sobel Detector", variable=self.var3,command=self.cb).grid(row=3, column=2, sticky=W)

        self.imagestoprocess = StringVar()
        self.imagestoprocess.set("select folder to see process-able images here...")
        self.imagescount_label = Label(master, text="",textvariable=self.imagestoprocess)
        self.imagescount_label.grid(row=6,column=2)


        # COLUMN 3

        self.run_button = Button(master, text="RUN", command=self.run)
        self.run_button.grid(row=1,column=4)

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.grid(row=2,column=4)



    def cb(self):
        self.detector_selection = [self.var1.get(),self.var2.get(),self.var3.get()]
        print(self.detector_selection)
    
    def run(self):
        print('caney only')
        try:
            os.mkdir(self.caney_folder)
        except OSError:
            print ("Creation of the directory %s failed" % self.caney_folder)

        current_file = 0
        for filename in os.listdir(self.input_folder):
            if (filename[-4:] == ".jpg") or (filename[-4:] == ".JPG") or (filename[-4:] == ".png"):
                current_file = current_file + 1

                print(filename)
                time.sleep(1)
                edge_detectors.caney_edge(str(self.input_folder) + "/" + str(filename), self.caney_folder + "/" + "caney_" + str(filename)) #get detection
        print('done')
        self.imagestoprocess.set(self.getImagesToProcess([self.input_folder,self.ndvi_folder,self.caney_folder]))


    def getImagesToProcess(self, folders_arr):
        total_file = 0
        ndvi = 0
        unprocessed = 0
        # disables
        if os.path.exists(self.ndvi_folder):
            self.ndvibutton.configure(state=DISABLED)
            self.ndvi_loading.set("NDVI already present")
        else: 
            self.ndvibutton.configure(state=NORMAL)
            
        for folder in folders_arr:
            if (folder) and os.path.exists(folder):
                for filename in os.listdir(folder):
                    if (filename[-4:] == ".jpg") or (filename[-4:] == ".JPG") or (filename[-4:] == ".png"):
                        total_file = total_file + 1
                        if folder[-6:] == 'images':
                            unprocessed = unprocessed + 1
                        if folder[-4:] == 'ndvi':
                            ndvi = ndvi + 1
        return (str(total_file) + " images (" + str(unprocessed) + " unprocessed, " + str(ndvi) + " NDVI).")

    def select_img_folder(self):
        folder_selected = filedialog.askdirectory()
        self.input_folder = folder_selected
        self.ndvi_folder = folder_selected + "/ndvi"
        self.caney_folder = folder_selected + "/caney"

        self.img_label.set("Input Folder: " + folder_selected)
        print(self.input_folder,self.ndvi_folder)

        total_files = 0
        for filename in os.listdir(self.input_folder):
            if (filename[-4:] == ".jpg") or (filename[-4:] == ".JPG") or (filename[-4:] == ".png"):
                total_files = total_files + 1
        self.ndvi_loading.set("Found " + str(total_files) + " images to convert")
        self.imagestoprocess.set(self.getImagesToProcess([self.input_folder,self.ndvi_folder, self.caney_folder])) 

    def create_ndvi(self):
        self.ndvi_loading.set("Working...")
        try:
            os.mkdir(self.ndvi_folder)
        except OSError:
            print ("Creation of the directory %s failed" % self.ndvi_folder)

        current_file = 0
        for filename in os.listdir(self.input_folder):
            if (filename[-4:] == ".jpg") or (filename[-4:] == ".JPG") or (filename[-4:] == ".png"):
                current_file = current_file + 1

                print(filename)
                ndvi.createNDVI(str(self.input_folder) + "/" + str(filename), self.ndvi_folder + "/" + "ndvi_" + str(filename), False) # Enter the input JPG filename, Enter the output PNG filename, False
        self.ndvi_loading.set("Done.")
        self.imagestoprocess.set(self.getImagesToProcess([self.input_folder,self.ndvi_folder, self.caney_folder]))
        

root = Tk()
my_gui = SRSD_GUI(root)
root.mainloop()