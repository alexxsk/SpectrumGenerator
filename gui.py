from tkinter import Tk, Label, Button, Entry, IntVar, END, W, E, StringVar, messagebox, filedialog
import parser as ps
import generator as gn
import pandas as pd
import tkinter as tk
import matplotlib.pyplot as plt
import seaborn as sns
import b2plot as bp
import os

plt.style.use('belle2') 

def find_in_file(filename=None, text=None):
    file = open(filename, "r")
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

        self.add_line_button = Button(master, text="Add LINE", 
            command=self.add_line_to)

        self.number_label = Label(master, text="Number: ")
        self.enter_number = Entry()
        self.energy_label = Label(master, text="Energy:")
        self.enter_energy = Entry()
        self.intensity_label = Label(master, text="Intensity:")
        self.enter_intensity = Entry()
        self.fwhm_label = Label(master, text="FWHM:")
        self.enter_fwhm = Entry()

        self.browse_button = Button(master, text="BROWSE", 
                                    command=self.get_browse)

        self.add_bkg_button = Button(master, text=" SET BKG", 
            command=self.set_bkg_to)

        self.first_lin_label = Label(master, text="First linear coef.:")
        self.enter_first_lin = Entry()
        self.second_lin_label = Label(master, text="Second linear coef.:")
        self.enter_second_lin = Entry()

        self.first_exp_label = Label(master, text="First exp coef.:")
        self.enter_first_exp = Entry()
        self.second_exp_label = Label(master, text="Second exp coef.:")
        self.enter_second_exp = Entry()


        self.add_range_button = Button(master, text="SET RANGE", 
            command=self.set_range_to)

        self.emin_label = Label(master, text="Emin:")
        self.enter_emin = Entry()
        self.emax_label = Label(master, text="Emax:")
        self.enter_emax = Entry()
        self.nchan_label = Label(master, text="Channel num.:")
        self.enter_nachan = Entry()

        self.label_a = Label(master, text="A:")
        self.label_b = Label(master, text="B:")

        self.enter_a = Entry()
        self.enter_b = Entry()

        self.current_filename = StringVar()
        self.current_filename.set(self.FILENAME)
        self.current_filename_label_text = Label(master, text="Current file:")
        self.current_filename_label = Label(master, textvariable=self.current_filename)

        self.file_label = Label(master, text="Filename:")
        self.enter_file = Entry()
        # self.set_file_button = Button(master, text="Set File", 
        #     command=lambda: self.set_file(str(self.enter_file.get())))

        self.data =[("S(0)",1),("S(0)+B",2),("S(1)+B",3),
                  ("S(2)+B",4),("S(1)+B+D",5),("S(2)+B+D",6)]

        self.v = tk.StringVar()
        for row, (start, goal) in enumerate(self.data):
            self.radiobutton = tk.Radiobutton(self.master, text=f"{start}",
                                              value=start, variable=self.v)
            self.radiobutton.grid(row=row+2, column=5, sticky="w")

        self.run_button = Button(master, text=" RUN!", bg='red', 
                                 command=lambda: self.generate(self.v.get()))
        self.import_button = Button(master, text=" Import to spectrum.txt",
                                    bg='green', 
                                    command=lambda: self.save_to_csv(self.v.get()))

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

        # self.set_file_button.grid(row=7, column=0)
        # self.file_label.grid(row=6, column=1, sticky=W)
        # self.enter_file.grid(row=7, column=1, sticky=W)

        # self.current_filename_label_text.grid(row=7, column=0)
        # self.current_filename_label.grid(row=7, column=1)

        self.browse_button.grid(row=6, column=1)
        self.run_button.grid(row=6, column=2)
        self.import_button.grid(row=6, column=3)


        self.label_a.grid(row=4, column=6, sticky=W+E)
        self.label_b.grid(row=6, column=6, sticky=W+E)
        self.enter_a.grid(row=5, column=6, sticky=W+E)
        self.enter_b.grid(row=7, column=6, sticky=W+E)

    def get_browse(self):
        self.FILENAME =  filedialog.askopenfilename(initialdir = "./",
                                                    title = "Select file",
                                            filetypes = (("txt files","*.txt"),
                                                         ("all files","*.*")))
        self.current_filename.set(f".../{os.path.basename(self.FILENAME)}")

    def check_file_set(self):
        if self.FILENAME == 'NONE':
            tk.messagebox.showinfo("GUI Python", 
                                   "file isn't set")
            return False
        return True
            

    def add_line_to(self):
        if not self.check_file_set(): return 
        if find_in_file(filename=self.FILENAME,
            text=f"LINE{int(self.enter_number.get())}"):
            tk.messagebox.showinfo("GUI Python", 
                f"Line {int(self.enter_number.get())} already exist")
        else:
            file = open(self.FILENAME, "a")
            file.write(f"\nLINE{int(self.enter_number.get())}" + 
                       f" ERG={float(self.enter_energy.get())}" +
                       f" ITS={float(self.enter_intensity.get())}" +
                       f" FWHM={float(self.enter_fwhm.get())}" + "\n")

            self.enter_number.delete(0, END)
            self.enter_energy.delete(0, END)
            self.enter_intensity.delete(0, END)
            self.enter_fwhm.delete(0, END)

            file.close()

    def set_bkg_to(self):
        if not self.check_file_set(): return 
        if find_in_file(filename=self.FILENAME,
            text=f"BKG"):
            tk.messagebox.showinfo("GUI Python", 
                f"Background already set")
        else:
            file = open(self.FILENAME, "a")
            file.write(f"\nBKG" + 
                       f" EP1={float(self.enter_first_exp.get())}" +
                       f" EP2={float(self.enter_second_exp.get())}" +
                       f" A={float(self.enter_first_lin.get())}" +
                       f" B={float(self.enter_second_lin.get())}" + "\n")

            self.enter_first_lin.delete(0, END)
            self.enter_second_lin.delete(0, END)
            self.enter_first_exp.delete(0, END)
            self.enter_second_exp.delete(0, END)

            file.close()

    def set_range_to(self):
        if not self.check_file_set(): return 
        if find_in_file(filename=self.FILENAME,
            text=f"RANGE"):
            tk.messagebox.showinfo("GUI Python", 
                f"Range already set")
        else:
            file = open(self.FILENAME, "a")
            file.write(f"\nRANGE" + 
                       f" EMIN={float(self.enter_emin.get())}" +
                       f" EMAX={float(self.enter_emax.get())}" +
                       f" NCH={int(self.enter_nachan.get())}" + "\n")

            self.enter_emin.delete(0, END)
            self.enter_emax.delete(0, END)
            self.enter_nachan.delete(0, END)

            file.close()

    def generate(self, cmd=""):
        if not self.check_file_set(): return 
        if cmd == "":
            tk.messagebox.showinfo("GUI Python", 
                                   "There is nothing to build")
        else:
            gen = gn.Generator(self.FILENAME)
            x = gen.x
            if cmd == "S(0)":
                y = gen.generate_peaks_without_extension()
            elif cmd == "S(0)+B":
                y = gen.generate_bkg_without_stat() + \
                    gen.generate_peaks_without_extension()
            elif cmd == "S(1)+B":
                y = gen.generate_peaks_with_custom_extension() + \
                    gen.generate_bkg_without_stat()
            elif cmd == "S(2)+B":
                if (self.enter_a.get() == "" or self.enter_b.get() == ""):
                    tk.messagebox.showinfo("GUI Python", 
                                   "Please enter A and B")
                y = gen.generate_peaks_with_extension(float(self.enter_a.get()),
                                                      float(self.enter_b.get())) + \
                    gen.generate_bkg_without_stat()
            elif cmd == "S(1)+B+D":
                temp = gen.generate_peaks_with_custom_extension() + \
                       gen.generate_bkg_without_stat()
                y = [gn.statistical_scatter(i) for i in temp]
            elif cmd == "S(2)+B+D":
                if (self.enter_a.get() == "" or self.enter_b.get() == ""):
                    tk.messagebox.showinfo("GUI Python", 
                                   "Please enter A and B")
                temp = gen.generate_peaks_with_extension(float(self.enter_a.get()),
                                                         float(self.enter_b.get())) + \
                       gen.generate_bkg_without_stat()
                y = [gn.statistical_scatter(i) for i in temp]

            bp.hist(x, weights=y, bins=gen.sts.nbins, style=0)
            plt.show()
            return (x, y)

    def save_to_csv(self, cmd=""):
        if not self.check_file_set(): return 
        x,y = self.generate(cmd)
        data = pd.DataFrame({'Energy' : x, 'Intensity' : y})
        data.to_csv("spectrum.txt")

def start_gui():
    root = Tk()
    my_gui = GUI(root)
    root.mainloop()
