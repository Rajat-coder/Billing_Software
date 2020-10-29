import os
from tkinter import*
import math,random
from tkinter import messagebox

class Bill_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
        self.root.title("Billing Software")
        bg_color="#074463"
        title=Label(self.root,text="Billing Software",bd=12,relief=GROOVE,bg=bg_color,fg="white",font=("times new roman",30,"bold"),pady=2).pack(fill=X)

        #---------------Variables------------------
        #---------------Cosmetics var ------------------
        self.bath_soup = IntVar()
        self.face_wash = IntVar()
        self.hair_cream = IntVar()
        self.hair_spray = IntVar()
        self.coconut_oil = IntVar()
        self.hair_wax = IntVar()


        # ---------------Grocery var ------------------
        self.rice = IntVar()
        self.sugar = IntVar()
        self.wheat = IntVar()
        self.pulses = IntVar()
        self.kitchen_oil = IntVar()
        self.ghee = IntVar()

        # ---------------Soft Drink var ------------------
        self.maaza = IntVar()
        self.coka_cola = IntVar()
        self.thumbs_up = IntVar()
        self.limca = IntVar()
        self.nimbu_soda = IntVar()
        self.pepsi = IntVar()

        #--------------------Total product price and tax variable
        self.cosmetic_price=StringVar()
        self.grocery_price = StringVar()
        self.softdrink_price = StringVar()

        self.cosmetic_tax = StringVar()
        self.grocery_tax = StringVar()
        self.softdrink_tax = StringVar()

        # --------------------Customer
        self.c_name = StringVar()
        self.c_phone = StringVar()
        self.bill_no = StringVar()
        x=random.randint(1000,9999)
        self.bill_no.set(str(x))
        self.search_bill = StringVar()

        # Frame details
        f1=LabelFrame(self.root,text="Customer Details",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        f1.place(x=0,y=80,relwidth=1)

        # Customer details

        cname=Label(f1,text="Customer Name",bg=bg_color,fg="white",font=("times new roman",18,"bold")).grid(row=0,column=0,padx=20,pady=5)
        cname=Entry(f1,width=20,textvariable=self.c_name,font="arial 15",bd=3,relief=SUNKEN).grid(row=0,column=1,pady=5)

        pname = Label(f1, text="Phone No:", bg=bg_color, fg="white", font=("times new roman", 18, "bold")).grid(row=0, column=2, padx=20, pady=5)
        pname = Entry(f1, width=20,textvariable=self.c_phone, font="arial 15", bd=3, relief=SUNKEN).grid(row=0, column=3, pady=5)

        bname = Label(f1, text="Bill Number", bg=bg_color, fg="white", font=("times new roman", 18, "bold")).grid(row=0, column=4, padx=20, pady=5)
        bname = Entry(f1, width=20, font="arial 15",textvariable=self.search_bill, bd=3, relief=SUNKEN).grid(row=0, column=5, pady=5)

        bill_btn=Button(f1,text="Search",width=10,bd=3,command=self.find_bill,font="arial 12 bold").grid(row=0,column=6,padx=30,pady=15)

        #Cosmetic details

        f2 = LabelFrame(self.root, text="Cosmetics Details", font=("times new roman", 15, "bold"), fg="gold", bg=bg_color)
        f2.place(x=5, y=180,width=350,height=380)

        x_lbl=Label(f2,text="Bath Soap",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        x_txt=Entry(f2,width=13,textvariable=self.bath_soup,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady= 10)

        x1_lbl = Label(f2, text="Face Wash", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        x1_txt = Entry(f2, width=13,textvariable=self.face_wash, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=1, column=1,padx=10, pady=10)

        x2_lbl = Label(f2, text="Hair Cream", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        x2_txt = Entry(f2, width=13,textvariable=self.hair_cream, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=2, column=1,padx=10, pady=10)

        x3_lbl = Label(f2, text="Hair Spray", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        x3_txt = Entry(f2, width=13,textvariable=self.hair_spray, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=3, column=1,padx=10, pady=10)

        x4_lbl = Label(f2, text="Cocunut Oil", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        x4_txt = Entry(f2, width=13,textvariable=self.coconut_oil, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=4, column=1,padx=10, pady=10)

        x5_lbl = Label(f2, text="Hair Wax", font=("times new roman", 16, "bold"), bg=bg_color,fg="lightgreen").grid(row=5, column=0, padx=10, pady=10, sticky="w")
        x5_txt = Entry(f2, width=13,textvariable=self.hair_wax, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)

        # Grocery details

        f3 = LabelFrame(self.root, text="Grocery Details", font=("times new roman", 15, "bold"), fg="gold",bg=bg_color)
        f3.place(x=360, y=180, width=350, height=380)

        y1_lbl = Label(f3, text="Rice", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        y1_txt = Entry(f3, width=13,textvariable=self.rice, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=0, column=1,padx=10, pady=10)

        y2_lbl = Label(f3, text="Sugar", font=("times new roman", 16, "bold"), bg=bg_color,fg="lightgreen").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        y2_txt = Entry(f3, width=13,textvariable=self.sugar, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        y3_lbl = Label(f3, text="Wheat", font=("times new roman", 16, "bold"), bg=bg_color,fg="lightgreen").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        y3_txt = Entry(f3, width=13,textvariable=self.wheat, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        y4_lbl = Label(f3, text="Pulses", font=("times new roman", 16, "bold"), bg=bg_color,fg="lightgreen").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        y4_txt = Entry(f3, width=13,textvariable=self.pulses, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        y5_lbl = Label(f3, text="Kitchen-Oil", font=("times new roman", 16, "bold"), bg=bg_color,fg="lightgreen").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        y5_txt = Entry(f3, width=13,textvariable=self.kitchen_oil, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        y6_lbl = Label(f3, text="Ghee", font=("times new roman", 16, "bold"), bg=bg_color,fg="lightgreen").grid(row=5, column=0, padx=10, pady=10, sticky="w")
        y6_txt = Entry(f3, width=13,textvariable=self.ghee, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)

        # Softdrink details

        f4 = LabelFrame(self.root, text="Softdrinks Details", font=("times new roman", 15, "bold"), fg="gold",bg=bg_color)
        f4.place(x=716, y=180, width=350, height=380)



        z1_lbl = Label(f4, text="Mazza", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        z1_txt = Entry(f4, width=13,textvariable=self.maaza, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=0, column=1,padx=10, pady=10)

        z2_lbl = Label(f4, text="Coka-Cola", font=("times new roman", 16, "bold"), bg=bg_color,fg="lightgreen").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        z2_txt = Entry(f4, width=13,textvariable=self.coka_cola, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        z3_lbl = Label(f4, text="Thumbs Up", font=("times new roman", 16, "bold"), bg=bg_color,fg="lightgreen").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        z3_txt = Entry(f4, width=13,textvariable=self.thumbs_up, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        z4_lbl = Label(f4, text="Limca", font=("times new roman", 16, "bold"), bg=bg_color,fg="lightgreen").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        z4_txt = Entry(f4, width=13,textvariable=self.limca, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        z5_lbl = Label(f4, text="Nimbu-Soda", font=("times new roman", 16, "bold"), bg=bg_color,fg="lightgreen").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        z5_txt = Entry(f4, width=13,textvariable=self.coconut_oil, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        z6_lbl = Label(f4, text="Pepsi", font=("times new roman", 16, "bold"), bg=bg_color,fg="lightgreen").grid(row=5, column=0, padx=10, pady=10, sticky="w")
        z6_txt = Entry(f4, width=13,textvariable=self.hair_wax, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)

        # Billing area

        f5 = Frame(self.root, bd=6, relief=GROOVE)
        f5.place(x=1080, y=180, width=430, height=380)
        bill_tilte=Label(f5,text="Bill Area",font="arial 15 bold",bd=6,relief=GROOVE).pack(fill=X)
        scrol_y=Scrollbar(f5,orient=VERTICAL)
        self.txtarea=Text(f5,yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH,expand=1)

        #Bill menu

        f6 = LabelFrame(self.root, text="Bill Menu", font=("times new roman", 15, "bold"), fg="gold",bg=bg_color)
        f6.place(x=0, y=570, relwidth=1, height=225)

        a1_lbl=Label(f6,text="Total Cosmetic Price",bg=bg_color,fg="lightgreen",font=("times new roman ",14,"bold")).grid(row=0,column=0,padx=20,pady=1,sticky="w")
        al_txt=Entry(f6,width=19,textvariable=self.cosmetic_price,font="arial 10 bold",bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        a2_lbl = Label(f6, text="Total Grocery Price", bg=bg_color, fg="lightgreen",font=("times new roman ", 14, "bold")).grid(row=1, column=0, padx=20, pady=1, sticky="w")
        a2_txt = Entry(f6, width=19,textvariable=self.grocery_price, font="arial 10 bold", bd=5, relief=SUNKEN).grid(row=1, column=1, padx=10, pady=10)

        a3_lbl = Label(f6, text="Total Softdrink Price", bg=bg_color, fg="lightgreen",font=("times new roman ", 14, "bold")).grid(row=2, column=0, padx=20, pady=1, sticky="w")
        a3_txt = Entry(f6, width=19, font="arial 10 bold",textvariable=self.softdrink_price, bd=5, relief=SUNKEN).grid(row=2, column=1, padx=10, pady=10)

        #Tax menu

        b1_lbl = Label(f6, text="Cosmetic Tax", bg=bg_color, fg="lightgreen",font=("times new roman ", 14, "bold")).grid(row=0, column=2, padx=20, pady=1, sticky="w")
        bl_txt = Entry(f6, width=19, font="arial 10 bold",textvariable=self.cosmetic_tax, bd=5, relief=SUNKEN).grid(row=0, column=3, padx=10, pady=10)

        b2_lbl = Label(f6, text="Grocery Tax", bg=bg_color, fg="lightgreen",font=("times new roman ", 14, "bold")).grid(row=1, column=2, padx=20, pady=1, sticky="w")
        b2_txt = Entry(f6, width=19, font="arial 10 bold",textvariable=self.grocery_tax, bd=5, relief=SUNKEN).grid(row=1, column=3, padx=10, pady=10)

        b3_lbl = Label(f6, text="Softdrink Tax", bg=bg_color, fg="lightgreen",font=("times new roman ", 14, "bold")).grid(row=2, column=2, padx=20, pady=1, sticky="w")
        b3_txt = Entry(f6, width=19, font="arial 10 bold", bd=5,textvariable=self.softdrink_tax, relief=SUNKEN).grid(row=2, column=3, padx=10, pady=10)

        btn_F=Frame(f6,bd=7,relief=GROOVE)
        btn_F.place(x=750,y=10,width=760,height=125)

        total_btn=Button(btn_F,text="Total",command=self.total,bg="cadetblue",fg="white",bd=5,padx=15,width=11,height=2,font="arial 15 bold").grid(row=0,column=0,padx=5,pady=15)
        Gen_btn = Button(btn_F, text="Genrate Bill",command=self.bill_area, bg="cadetblue", fg="white", bd=5, padx=15, width=11, height=2,font="arial 15 bold").grid(row=0, column=1, padx=5, pady=15)
        clr_btn = Button(btn_F, text="Clear",command=self.clear_data, bg="cadetblue", fg="white", bd=5, padx=15, width=11, height=2,font="arial 15 bold").grid(row=0, column=2, padx=5, pady=15)
        exit_btn = Button(btn_F, text="Exit ",command=self.exit_app, bg="cadetblue", fg="white", bd=5, padx=15, width=11, height=2,font="arial 15 bold").grid(row=0, column=3, padx=5, pady=15)
        self.welcome_bill()

    def total(self):
        self.c_bs_p=self.bath_soup.get() * 40
        self.hw_p=self.hair_wax.get() * 140
        self.hs_p=self.hair_spray.get() * 120
        self.hc_p=self.hair_cream.get() * 90
        self.co_p=self.coconut_oil.get() * 340
        self.fw_p=self.face_wash.get() * 40

        self.total_cosmetic_price=float(
                   self.c_bs_p+
                   self.hw_p+
                   self.hs_p+
                   self.hc_p+
                   self.co_p+
                   self.fw_p

                                )
        self.cosmetic_price.set("Rs "+str(self.total_cosmetic_price))
        self.c_tax=round((self.total_cosmetic_price*0.05))
        self.cosmetic_tax.set("Rs "+str(self.c_tax))

        self.r_p=self.rice.get() * 240
        self.w_p=self.wheat.get() * 140
        self.s_p=self.sugar.get() * 120
        self.ko_p=self.kitchen_oil.get() * 190
        self.p_p=self.pulses.get() * 340
        self.gh_p=self.ghee.get() * 440

        self.total_grocery_price = float(
             self.r_p +
             self.s_p+
             self.w_p +
             self.gh_p +
             self.ko_p+
             self.p_p

        )
        self.grocery_price.set("Rs "+str(self.total_grocery_price))
        self.g_tax=round((self.total_grocery_price * 0.10))
        self.grocery_tax.set("Rs " + str(self.g_tax))

        self.m_p=self.maaza.get() * 25
        self.cc_p=self.coka_cola.get() * 60
        self.li_p=self.limca.get() * 60
        self.pe_p=self.pepsi.get() * 60
        self.ns_p=self.nimbu_soda.get() * 40
        self.th_p=self.thumbs_up.get() * 60



        self.total_softdrink_price = float(
            self.m_p +
            self.cc_p +
            self.li_p +
            self.pe_p +
            self.ns_p +
            self.th_p
        )
        self.softdrink_price.set("Rs "+str(self.total_softdrink_price))
        self.sf_tax=round((self.total_softdrink_price * 0.05))
        self.softdrink_tax.set("Rs " + str(self.sf_tax))


        self.total_bill=float(
                self.total_cosmetic_price+
                self.total_grocery_price+
                self.total_softdrink_price+
                self.c_tax+
                self.g_tax+
                self.sf_tax
        )


    def welcome_bill(self):
        self.txtarea.delete('1.0',END)
        self.txtarea.insert(END,"\t      WELCOME TO HANDA STORE")
        self.txtarea.insert(END, f"\n Bill Number : {self.bill_no.get()}")
        self.txtarea.insert(END, f"\n Customer Name : {self.c_name.get()}")
        self.txtarea.insert(END, f"\n Phone Number : {self.c_phone.get()}")
        self.txtarea.insert(END, f"\n ================================================")
        self.txtarea.insert(END, f"\n Products \t\t\tQTY\t\tPrice")
        self.txtarea.insert(END, f"\n ================================================")

    def bill_area(self):
        if self.c_name.get()=="" or self.c_phone.get()=="":
            messagebox.showerror("Error","Customer details are must")
        else:
            self.welcome_bill()
            #---------------cosmetics
            if self.bath_soup.get()!=0:
                self.txtarea.insert(END,f"\n Bath Soap \t\t\t{self.bath_soup.get()}\t\t{self.c_bs_p}")
            if self.face_wash.get()!=0:
                self.txtarea.insert(END,f"\n Face Wash \t\t\t{self.face_wash.get()}\t\t{self.fw_p}")
            if self.hair_wax.get()!=0:
                self.txtarea.insert(END,f"\n Hair wax \t\t\t{self.hair_wax.get()}\t\t{self.hw_p}")
            if self.hair_cream.get()!=0:
                self.txtarea.insert(END,f"\n Hair Cream \t\t\t{self.hair_cream.get()}\t\t{self.hc_p}")
            if self.hair_spray.get()!=0:
                self.txtarea.insert(END,f"\n Hair spray \t\t\t{self.hair_spray.get()}\t\t{self.hs_p}")
            if self.coconut_oil.get()!=0:
                self.txtarea.insert(END,f"\n Coconut Oil \t\t\t{self.coconut_oil.get()}\t\t{self.co_p}")

            #---------------Grocery
            if self.rice.get()!=0:
                self.txtarea.insert(END,f"\n Rice \t\t\t{self.rice.get()}\t\t{self.r_p}")
            if self.wheat.get()!=0:
                self.txtarea.insert(END,f"\n Wheat \t\t\t{self.wheat.get()}\t\t{self.w_p}")
            if self.sugar.get()!=0:
                self.txtarea.insert(END,f"\n Sugar \t\t\t{self.sugar.get()}\t\t{self.s_p}")
            if self.kitchen_oil.get()!=0:
                self.txtarea.insert(END,f"\n Kitchen Oil \t\t\t{self.kitchen_oil.get()}\t\t{self.ko_p}")
            if self.pulses.get()!=0:
                self.txtarea.insert(END,f"\n Pulses \t\t\t{self.pulses.get()}\t\t{self.p_p}")
            if self.ghee.get()!=0:
                self.txtarea.insert(END,f"\n Ghee \t\t\t{self.ghee.get()}\t\t{self.gh_p}")

            #---------------Softdrink
            if self.maaza.get()!=0:
                self.txtarea.insert(END,f"\n Maaza \t\t\t{self.maaza.get()}\t\t{self.m_p}")
            if self.coka_cola.get()!=0:
                self.txtarea.insert(END,f"\n Coka-Cola \t\t\t{self.coka_cola.get()}\t\t{self.cc_p}")
            if self.limca.get()!=0:
                self.txtarea.insert(END,f"\n Limca \t\t\t{self.limca.get()}\t\t{self.li_p}")
            if self.pepsi.get()!=0:
                self.txtarea.insert(END,f"\n Pepsi \t\t\t{self.pepsi.get()}\t\t{self.pe_p}")
            if self.nimbu_soda.get()!=0:
                self.txtarea.insert(END,f"\n Nimbu-Soda \t\t\t{self.nimbu_soda.get()}\t\t{self.ns_p}")
            if self.thumbs_up.get()!=0:
                self.txtarea.insert(END,f"\n Thumbs \t\t\t{self.thumbs_up.get()}\t\t{self.th_p}")

            self.txtarea.insert(END, f"\n ------------------------------------------------")
            if self.cosmetic_tax.get()!="Rs 0":
                self.txtarea.insert(END, f"\n Cosmeitc Tax \t\t\t\t\t{self.cosmetic_tax.get()}")
            if self.grocery_tax.get()!="Rs 0":
                self.txtarea.insert(END, f"\n Grocery Tax \t\t\t\t\t{self.grocery_tax.get()}")
            if self.softdrink_tax.get()!="Rs 0":
                self.txtarea.insert(END, f"\n Soft Drink Tax \t\t\t\t\t{self.softdrink_tax.get()}")
            self.txtarea.insert(END, f"\n ------------------------------------------------")
            self.txtarea.insert(END, f"\n Total Bill =  \t\t\t\t\t{str(self.total_bill)}")
            self.save_bill()

    def save_bill(self):
        op=messagebox.askyesno("Save Bill","Do you wan to save bill ?")
        if op>0:
            self.bill_data=self.txtarea.get('1.0',END)
            f1=open("bills/"+str(self.bill_no.get())+".txt","w")
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("Saved",f"bill no.: {self.bill_no.get()} Saved successfully")
        else:
            return
    def find_bill(self):
        present="no"
        for i in os.listdir("bills/"):
            if i.split('.')[0]==self.search_bill.get():
                f1=open(f"bills/{i}","r")
                self.txtarea.delete('1.0',END)
                for d in f1:
                    self.txtarea.insert(END,d)
                f1.close()
                present="yes"
        if present=="no":
            messagebox.showerror("Error","invalid Bill Number")

    def clear_data(self):
        op=messagebox.askyesno("Clear","Do you really want to Clear ?")
        if op>0:
                # ---------------Variables------------------
                # ---------------Cosmetics var ------------------
                self.bath_soup.set(0)
                self.face_wash.set(0)
                self.hair_cream.set(0)
                self.hair_spray.set(0)
                self.coconut_oil.set(0)
                self.hair_wax.set(0)

                # ---------------Grocery var ------------------
                self.rice.set(0)
                self.sugar.set(0)
                self.wheat.set(0)
                self.pulses.set(0)
                self.kitchen_oil.set(0)
                self.ghee.set(0)

                # ---------------Soft Drink var ------------------
                self.maaza.set(0)
                self.coka_cola.set(0)
                self.thumbs_up.set(0)
                self.limca.set(0)
                self.nimbu_soda.set(0)
                self.pepsi.set(0)

                # --------------------Total product price and tax variable
                self.cosmetic_price.set("")
                self.grocery_price.set("")
                self.softdrink_price.set("")

                self.cosmetic_tax.set("")
                self.grocery_tax.set("")
                self.softdrink_tax.set("")

                # --------------------Customer
                self.c_name.set("")
                self.c_phone.set("")
                self.bill_no.set("")
                x = random.randint(1000, 9999)
                self.bill_no.set(str(x))
                self.search_bill.set("")
                self.welcome_bill()

    def exit_app(self):

        op=messagebox.askyesno("Exit","Do you really want to Exit ?")
        if op>0:
            self.root.destroy()

root=Tk()
obj=Bill_App(root)
root.mainloop()