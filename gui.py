from tkinter import Tk, Label, Button, Entry, IntVar, END, W, E, StringVar, messagebox 

def generate(filename=None):
    pass

def findInFile(filename=None, text=None):
    file = open(filename, "r+")
    for line in file:
        if text in line:
            file.close()
            return True
    file.close()
    return False

class GUI:

    def __init__(self, master):
        self.master = master
        master.title("Spectrum Creator")

        self.FILENAME = 'NONE'
        self.label = Label(master, text="Output File:")

        self.add_line_button = Button(master, text="Add LINE", 
            command=self.addLine_to)

        self.number_label = Label(master, text="Number: ")
        self.enter_number = Entry()
        self.energy_label = Label(master, text="Energy:")
        self.enter_energy = Entry()
        self.intensity_label = Label(master, text="Intensity:")
        self.enter_intensity = Entry()
        self.fwhm_label = Label(master, text="FWHM:")
        self.enter_fwhm = Entry()

        self.add_bkg_button = Button(master, text=" SET BKG", 
            command=self.setBkg_to)

        self.first_lin_label = Label(master, text="First linear coef.:")
        self.enter_first_lin = Entry()
        self.second_lin_label = Label(master, text="Second linear coef.:")
        self.enter_second_lin = Entry()

        self.first_exp_label = Label(master, text="First exp coef.:")
        self.enter_first_exp = Entry()
        self.second_exp_label = Label(master, text="Second exp coef.:")
        self.enter_second_exp = Entry()


        self.add_range_button = Button(master, text="SET RANGE", 
            command=self.setRange_to)

        self.emin_label = Label(master, text="Emin:")
        self.enter_emin = Entry()
        self.emax_label = Label(master, text="Emax:")
        self.enter_emax = Entry()
        self.nchan_label = Label(master, text="Channel num.:")
        self.enter_nachan = Entry()

        self.current_filename = StringVar()
        self.current_filename.set(self.FILENAME)
        self.current_filename_label_text = Label(master, text="Current filename:")
        self.current_filename_label = Label(master, textvariable=self.current_filename)

        self.file_label = Label(master, text="Filename:")
        self.enter_file = Entry()
        self.set_file_button = Button(master, text="Set File", 
            command=lambda: self.setFile(str(self.enter_file.get())))

        self.run_button = Button(master, text=" RUN!", bg='red', 
            command=lambda: generate(self.FILENAME))
        
        self.add_line_button.grid(row=1, column=0)

        self.number_label.grid(row=0, column=1, sticky=W)
        self.enter_number.grid(row=1, column=1, columnspan=2, sticky=W+E)

        self.energy_label.grid(row=0, column=2, sticky=W)
        self.enter_energy.grid(row=1, column=2, columnspan=2, sticky=W+E)

        self.intensity_label.grid(row=0, column=3, sticky=W)
        self.enter_intensity.grid(row=1, column=3, columnspan=2, sticky=W+E)

        self.fwhm_label.grid(row=0, column=5, sticky=W)
        self.enter_fwhm.grid(row=1, column=5, columnspan=3, sticky=W+E)

        self.add_bkg_button.grid(row=3, column=0)

        self.first_lin_label.grid(row=2, column=1, sticky=W)
        self.enter_first_lin.grid(row=3, column=1, sticky=W+E)
        self.second_lin_label.grid(row=2, column=2, sticky=W)
        self.enter_second_lin.grid(row=3, column=2, sticky=W+E)
        self.first_exp_label.grid(row=2, column=3, sticky=W)
        self.enter_first_exp.grid(row=3, column=3, sticky=W+E)
        self.second_exp_label.grid(row=2, column=4, sticky=W)
        self.enter_second_exp.grid(row=3, column=4, sticky=W+E)


        self.add_range_button.grid(row=5, column=0)
        
        self.emin_label.grid(row=4, column=1, sticky=W)
        self.enter_emin.grid(row=5, column=1, sticky=W+E)
        self.emax_label.grid(row=4, column=2, sticky=W)
        self.enter_emax.grid(row=5, column=2, sticky=W+E)
        self.nchan_label.grid(row=4, column=3, sticky=W)
        self.enter_nachan.grid(row=5, column=3, sticky=W+E)

        self.set_file_button.grid(row=7, column=0)
        self.file_label.grid(row=6, column=1, sticky=W)
        self.enter_file.grid(row=7, column=1, sticky=W)

        self.current_filename_label_text.grid(row=6, column=2)
        self.current_filename_label.grid(row=7, column=2)

        self.run_button.grid(row=7, column=3)

        # self.reset_button.grid(row=2, column=2, sticky=W+E)
    def setFile(self, new_filename=None):
        if new_filename != '':
            self.FILENAME = new_filename
        self.current_filename.set(self.FILENAME)
        self.enter_file.delete(0, END)

    def addLine_to(self):
        if findInFile(filename=self.FILENAME,
            text=f"LINE{int(self.enter_number.get())}"):
            tk.messagebox.showinfo("GUI Python", 
                f"Line {int(self.enter_number.get())} already exist")
        else:
            file = open(self.FILENAME, "a+")
            file.write(f"\nLINE{int(self.enter_number.get())}" + 
                       f" ERG={float(self.enter_energy.get())}" +
                       f" ITS={float(self.enter_intensity.get())}" +
                       f" FWHM={float(self.enter_fwhm.get())}")
            file.close()

    def setBkg_to(self):
        if findInFile(filename=self.FILENAME,
            text=f"BKG"):
            tk.messagebox.showinfo("GUI Python", 
                f"Background already set")
        else:
            file = open(self.FILENAME, "a+")
            file.write(f"\nBKG" + 
                       f" EP1={float(self.enter_first_exp.get())}" +
                       f" EP2={float(self.enter_second_exp.get())}" +
                       f" A={float(self.enter_first_lin.get())}" +
                       f" B={float(self.enter_second_lin.get())}")
            file.close()

    def setRange_to(self):
        if findInFile(filename=self.FILENAME,
            text=f"RANGE"):
            tk.messagebox.showinfo("GUI Python", 
                f"Range already set")
        else:
            file = open(self.FILENAME, "a+")
            file.write(f"\nRANGE" + 
                       f" EMIN={float(self.enter_emin.get())}" +
                       f" EMAX={float(self.enter_emax.get())}" +
                       f" A={float(self.enter_nachan.get())}")
            file.close()

        # else: # reset
            # self.total = 0

        # self.total_label_text.set(self.total)
        # self.entry.delete(0, END)


root = Tk()
my_gui = GUI(root)
root.mainloop()