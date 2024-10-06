from tkinter import *
import random


class Bill_App:
    def __init__(self, kh):
        self.kh = kh
        self.kh.geometry("1300x700+0+0")
        self.kh.maxsize(width=1280, height=700)
        self.kh.minsize(width=1180, height=700)
        self.kh.title("COFFEE BEANS CAFE")

        self.cus_name = StringVar()
        self.c_phone = IntVar()
        x = random.randint(110, 999)
        self.c_bill_no = StringVar()
        self.c_bill_no.set(str(x))

        self.Iced_latte = IntVar()
        self.Vanilla_latte = IntVar()
        self.Cappucino = IntVar()
        self.Velvet_coffee = IntVar()
        self.Cinnamon_coffee = IntVar()
        self.Pita_bread = IntVar()
        self.Bread_sticks = IntVar()
        self.garlic_bread = IntVar()
        self.Veg_burger = IntVar()
        self.Veg_pizza = IntVar()
        self.Vanilla_scoop = IntVar()
        self.Red_velvet_cake = IntVar()
        self.Choco_fudge = IntVar()
        self.Brownie = IntVar()
        self.Cheescake = IntVar()
        self.total_coffee = StringVar()
        self.total_snacks = StringVar()
        self.total_dessert = StringVar()
        self.tax_cof = StringVar()
        self.tax_snac = StringVar()
        self.tax_des = StringVar()

        bg_color = "teal"
        fg_color = "black"
        lbl_color = 'black'
        # Title of App
        title = Label(self.kh, text="COFFEE BEANS CAFE", bd=12, relief=GROOVE, fg=fg_color, bg=bg_color,
                      font=("times new roman", 34, "bold","italic"), pady=3).pack(fill=X)

        # ==========Customers Frame==========#
        F1 = LabelFrame(text="Customer Details", font=("time new roman", 12, "bold"), fg="black", bg=bg_color,
                        relief=GROOVE, bd=10)
        F1.place(x=0, y=80, relwidth=1)

        # ===============Customer Name===========#
        cname_lbl = Label(F1, text="Customer Name", bg=bg_color, fg=fg_color,
                          font=("times new roman", 15, "bold")).grid(row=0, column=0, padx=10, pady=5)
        cname_en = Entry(F1, bd=8, relief=GROOVE, textvariable=self.cus_name)
        cname_en.grid(row=0, column=1, ipady=4, ipadx=30, pady=5)

        # =================Customer Phone==============#
        cphon_lbl = Label(F1, text="Phone No", bg=bg_color, fg=fg_color, font=("times new roman", 15, "bold")).grid(
            row=0, column=2, padx=20)
        cphon_en = Entry(F1, bd=8, relief=GROOVE, textvariable=self.c_phone)
        cphon_en.grid(row=0, column=3, ipady=4, ipadx=30, pady=5)

        # ====================Customer Bill No==================#
        cbill_lbl = Label(F1, text="Bill No.", bg=bg_color, fg=fg_color, font=("times new roman", 15, "bold"))
        cbill_lbl.grid(row=0, column=4, padx=20)
        cbill_en = Entry(F1, bd=8, relief=GROOVE, textvariable=self.c_bill_no)
        cbill_en.grid(row=0, column=5, ipadx=30, ipady=4, pady=5)

        # ====================Bill Search Button===============#
        bill_btn = Button(F1, text="Enter", bd=7, relief=GROOVE, font=("times new roman", 12, "bold"), bg=bg_color,
                          fg=fg_color)
        bill_btn.grid(row=0, column=6, ipady=5, padx=60, ipadx=19, pady=5)

        F2 = LabelFrame(self.kh, text='Coffee', bd=10, relief=GROOVE, bg=bg_color, fg="black",
                        font=("times new roman", 13, "bold"))
        F2.place(x=5, y=180, width=325, height=380)

        Iced_lbl = Label(F2, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="Iced latte")
        Iced_lbl.grid(row=0, column=0, padx=10, pady=20)
        Iced_en = Entry(F2, bd=8, relief=GROOVE, textvariable=self.Iced_latte)
        Iced_en.grid(row=0, column=1, ipady=5, ipadx=5)

        Vanilla_lbl = Label(F2, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="Vanilla latte")
        Vanilla_lbl.grid(row=1, column=0, padx=10, pady=20)
        Vanilla_en = Entry(F2, bd=8, relief=GROOVE, textvariable=self.Vanilla_latte)
        Vanilla_en.grid(row=1, column=1, ipady=5, ipadx=5)

        cap_lbl = Label(F2, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="Cappucino")
        cap_lbl.grid(row=2, column=0, padx=10, pady=20)
        cap_en = Entry(F2, bd=8, relief=GROOVE, textvariable=self.Cappucino)
        cap_en.grid(row=2, column=1, ipady=5, ipadx=5)

        Velvet_lbl = Label(F2, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="Velvet coffee")
        Velvet_lbl.grid(row=3, column=0, padx=10, pady=20)
        Velvet_en = Entry(F2, bd=8, relief=GROOVE, textvariable=self.Velvet_coffee)
        Velvet_en.grid(row=3, column=1, ipady=5, ipadx=5)

        Cinn_lbl = Label(F2, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="Cinnamon coffee")
        Cinn_lbl.grid(row=4, column=0, padx=10, pady=20)
        Cinn_en = Entry(F2, bd=8, relief=GROOVE, textvariable=self.Cinnamon_coffee)
        Cinn_en.grid(row=4, column=1, ipady=5, ipadx=5)

        F2 = LabelFrame(self.kh, text='snacks', bd=10, relief=GROOVE, bg=bg_color, fg="black",
                        font=("times new roman", 13, "bold"))
        F2.place(x=330, y=180, width=325, height=380)

        Pita_lbl = Label(F2, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="Pita bread")
        Pita_lbl.grid(row=0, column=0, padx=10, pady=20)
        Pita_en = Entry(F2, bd=8, relief=GROOVE, textvariable=self.Pita_bread)
        Pita_en.grid(row=0, column=1, ipady=5, ipadx=5)

        Bread_lbl = Label(F2, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="Bread sticks")
        Bread_lbl.grid(row=1, column=0, padx=10, pady=20)
        Bread_en = Entry(F2, bd=8, relief=GROOVE, textvariable=self.Bread_sticks)
        Bread_en.grid(row=1, column=1, ipady=5, ipadx=5)

        garlic_lbl = Label(F2, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="garlic bread")
        garlic_lbl.grid(row=2, column=0, padx=10, pady=20)
        garlic_en = Entry(F2, bd=8, relief=GROOVE, textvariable=self.garlic_bread)
        garlic_en.grid(row=2, column=1, ipady=5, ipadx=5)

        Veg_lbl = Label(F2, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="Veg burger")
        Veg_lbl.grid(row=3, column=0, padx=10, pady=20)
        Veg_en = Entry(F2, bd=8, relief=GROOVE, textvariable=self.Veg_burger)
        Veg_en.grid(row=3, column=1, ipady=5, ipadx=5)

        Veg_lbl = Label(F2, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="Veg pizza")
        Veg_lbl.grid(row=4, column=0, padx=10, pady=20)
        Veg_en = Entry(F2, bd=8, relief=GROOVE, textvariable=self.Veg_pizza)
        Veg_en.grid(row=4, column=1, ipady=5, ipadx=5)

        F2 = LabelFrame(self.kh, text='dessert', bd=10, relief=GROOVE, bg=bg_color, fg="black",
                        font=("times new roman", 13, "bold"))
        F2.place(x=655, y=180, width=325, height=380)

        
        Vanilla_lbl = Label(F2, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="Vanilla scoop")
        Vanilla_lbl.grid(row=0, column=0, padx=10, pady=20)
        Vanilla_en = Entry(F2, bd=8, relief=GROOVE, textvariable=self.Vanilla_scoop)
        Vanilla_en.grid(row=0, column=1, ipady=5, ipadx=5)

        Red_lbl = Label(F2, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="Red velvet cake")
        Red_lbl.grid(row=1, column=0, padx=10, pady=20)
        Red_en = Entry(F2, bd=8, relief=GROOVE, textvariable=self.Red_velvet_cake)
        Red_en.grid(row=1, column=1, ipady=5, ipadx=5)

        Choco_lbl = Label(F2, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="Choco fudge")
        Choco_lbl.grid(row=2, column=0, padx=10, pady=20)
        Choco_en = Entry(F2, bd=8, relief=GROOVE, textvariable=self.Choco_fudge)
        Choco_en.grid(row=2, column=1, ipady=5, ipadx=5)

        Brownie_lbl = Label(F2, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="Brownie")
        Brownie_lbl.grid(row=3, column=0, padx=10, pady=20)
        Brownie_en = Entry(F2, bd=8, relief=GROOVE, textvariable=self.Brownie)
        Brownie_en.grid(row=3, column=1, ipady=5, ipadx=5)

        Cheescake_lbl = Label(F2, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="Cheescake")
        Cheescake_lbl.grid(row=4, column=0, padx=10, pady=20)
        Cheescake_en = Entry(F2, bd=8, relief=GROOVE, textvariable=self.Cheescake)
        Cheescake_en.grid(row=4, column=1, ipady=5, ipadx=5)

        F3 = Label(self.kh, bd=10, relief=GROOVE)
        F3.place(x=960, y=180, width=325, height=380)
        bill_title = Label(F3, text="Bill Area", font=("Lucida", 13, "bold"), bd=7, relief=GROOVE)
        bill_title.pack(fill=X)

        scroll_y = Scrollbar(F3, orient=VERTICAL)
        self.txt = Text(F3, yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=self.txt.yview)
        self.txt.pack(fill=BOTH, expand=1)

        F4 = LabelFrame(self.kh, text='Bill Menu', bd=10, relief=GROOVE, bg=bg_color, fg="black",
                        font=("times new roman", 13, "bold"))
        F4.place(x=0, y=560, relwidth=1, height=145)

        cof_lbl = Label(F4, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="Total coffee")
        cof_lbl.grid(row=0, column=0, padx=10, pady=0)
        cof_en = Entry(F4, bd=8, relief=GROOVE, textvariable=self.total_coffee)
        cof_en.grid(row=0, column=1, ipady=2, ipadx=5)

        snac_lbl = Label(F4, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="Total snacks")
        snac_lbl.grid(row=1, column=0, padx=10, pady=5)
        snac_en = Entry(F4, bd=8, relief=GROOVE, textvariable=self.total_snacks)
        snac_en.grid(row=1, column=1, ipady=2, ipadx=5)

        des_lbl = Label(F4, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="Dessert Total")
        des_lbl.grid(row=2, column=0, padx=10, pady=5)
        des_en = Entry(F4, bd=8, relief=GROOVE, textvariable=self.total_dessert)
        des_en.grid(row=2, column=1, ipady=2, ipadx=5)

        cof_lbl = Label(F4, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="coffee Tax")
        cof_lbl.grid(row=0, column=2, padx=30, pady=0)
        cof_en = Entry(F4, bd=8, relief=GROOVE, textvariable=self.tax_cof)
        cof_en.grid(row=0, column=3, ipady=2, ipadx=5)

        snac_lbl = Label(F4, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="snacks Tax")
        snac_lbl.grid(row=1, column=2, padx=30, pady=5)
        snac_en = Entry(F4, bd=8, relief=GROOVE, textvariable=self.tax_snac)
        snac_en.grid(row=1, column=3, ipady=2, ipadx=5)

        des_lbl = Label(F4, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="dessert Tax")
        des_lbl.grid(row=2, column=2, padx=10, pady=5)
        des_en = Entry(F4, bd=8, relief=GROOVE, textvariable=self.tax_des)
        des_en.grid(row=2, column=3, ipady=2, ipadx=5)

        total_btn = Button(F4, text="Total", bg=bg_color, fg=fg_color, font=("lucida", 12, "bold"), bd=7, relief=GROOVE,
                           command=self.total)
        total_btn.grid(row=1, column=4, ipadx=20, padx=30)

        genbill_btn = Button(F4, text="Generate Bill", bg=bg_color, fg=fg_color, font=("lucida", 12, "bold"), bd=7,
                             relief=GROOVE, command=self.bill_area)
        genbill_btn.grid(row=1, column=5, ipadx=20)

        clear_btn = Button(F4, text="Clear", bg=bg_color, fg=fg_color, font=("lucida", 12, "bold"), bd=7, relief=GROOVE,
                           command=self.clear)
        clear_btn.grid(row=1, column=6, ipadx=20, padx=30)

        exit_btn = Button(F4, text="Exit", bg=bg_color, fg=fg_color, font=("lucida", 12, "bold"), bd=7, relief=GROOVE,
                          command=self.exit)
        exit_btn.grid(row=1, column=7, ipadx=20)

    def total(self):
        self.total_coffee_prices = (
                (self.Iced_latte.get() * 535) +
                (self.Vanilla_latte.get() * 650) +
                (self.Cappucino.get() * 555) +
                (self.Velvet_coffee.get() * 530) +
                (self.Cinnamon_coffee.get() * 615)
        )
        self.total_coffee.set("Rs. " + str(self.total_coffee_prices))
        self.tax_cof.set("Rs. " + str(round(self.total_coffee_prices * 0.05))) 

        self.total_snacks_prices = (
                (self.Pita_bread.get() * 100) +
                (self.Bread_sticks.get() * 180) +
                (self.garlic_bread.get() * 300) +
                (self.Veg_burger.get() * 500) +
                (self.Veg_pizza.get() * 800)

        )
        self.total_snacks.set("Rs. " + str(self.total_snacks_prices))
        self.tax_snac.set("Rs. " + str(round(self.total_snacks_prices * 0.05)))

        self.total_dessert_prices = (
                (self.Vanilla_scoop.get() * 400) +
                (self.Red_velvet_cake.get() * 500) +
                (self.Choco_fudge.get() * 650) +
                (self.Brownie.get() * 150) +
                (self.Cheescake.get() * 670)
        )
        self.total_dessert.set("Rs. " + str(self.total_dessert_prices))
        self.tax_des.set("Rs. " + str(round(self.total_dessert_prices * 0.05)))

    def welcome_soft(self):
        self.txt.delete('1.0', END)
        self.txt.insert(END, "       Welcome To COFFEE BEANS CAFE\n")
        self.txt.insert(END, f"\nBill No. : {str(self.c_bill_no.get())}")
        self.txt.insert(END, f"\nCustomer Name : {str(self.cus_name.get())}")
        self.txt.insert(END, f"\nPhone No. : {str(self.c_phone.get())}")
        self.txt.insert(END, "\n===================================")
        self.txt.insert(END, "\nProduct          Qty         Price")
        self.txt.insert(END, "\n===================================")

    def clear(self):
        self.txt.delete('1.0', END)

    def bill_area(self):
        self.welcome_soft()
        if self.Iced_latte.get() != 0:
            self.txt.insert(END, f"\nIced latte         {self.Iced_latte.get()}           {self.Iced_latte.get() * 535}")
        if self.Vanilla_latte.get() != 0:
            self.txt.insert(END, f"\nVanilla latte        {self.Vanilla_latte.get()}           {self.Vanilla_latte.get() * 650}")
        if self.Cappucino.get() != 0:
            self.txt.insert(END, f"\nCappucino         {self.Cappucino.get()}           {self.Cappucino.get() * 555}")
        if self.Velvet_coffee.get() != 0:
            self.txt.insert(END, f"\nVelvet coffee       {self.Velvet_coffee.get()}           {self.Velvet_coffee.get() * 530}")
        if self.Cinnamon_coffee.get() != 0:
            self.txt.insert(END,f"\nCinnamon coffee       {self.Cinnamon_coffee.get()}           {self.Cinnamon_coffee.get() * 615}")
        if self.Pita_bread.get() != 0:
            self.txt.insert(END, f"\nPita bread             {self.Pita_bread.get()}           {self.Pita_bread() * 100}")
        if self.Bread_sticks.get() != 0:
            self.txt.insert(END, f"\nBread sticks          {self.Bread_sticks.get()}           {self.Bread_sticks.get() * 180}")
        if self.garlic_bread.get() != 0:
            self.txt.insert(END, f"\ngarlic bread              {self.garlic_bread.get()}           {self.garlic_bread.get() * 300}")
        if self.Veg_burger.get() != 0:
            self.txt.insert(END, f"\nVeg burger              {self.Veg_burger.get()}           {self.Veg_burger.get() * 500}")
        if self.Veg_pizza.get() != 0:
            self.txt.insert(END, f"\nVeg pizza             {self.Veg_pizza.get()}           {self.Veg_pizza.get() * 800}")
        if self.Vanilla_scoop.get() != 0:
            self.txt.insert(END, f"\nVanilla scoop         {self.Vanilla_scoop.get()}           {self.Vanilla_scoop.get() * 400}")
        if self.Red_velvet_cake.get() != 0:
            self.txt.insert(END, f"\nRed velvet cake            {self.Red_velvet_cake.get()}           {self.Red_velvet_cake.get() * 500}")
        if self.Choco_fudge.get() != 0:
            self.txt.insert(END, f"\nChoco fudge              {self.Choco_fudge.get()}           {self.Choco_fudge.get() * 650}")
        if self.Brownie.get() != 0:
            self.txt.insert(END, f"\nBrownie             {self.Brownie.get()}           {self.Brownie.get() * 150}")
        if self.Cheescake.get() != 0:
            self.txt.insert(END, f"\nCheesecake          {self.Cheescake.get()}           {self.Cheescake.get() * 670}")
        self.txt.insert(END, "\n===================================")
        self.txt.insert(END,
                        f"\n                      Total : {self.total_coffee_prices + self.total_snacks_prices + self.total_dessert_prices + self.total_coffee_prices * 0.05 + self.total_snacks_prices * 0.05 + self.total_dessert_prices * 0.05}")

    def exit(self):
        self.kh.destroy()



kh = Tk()
object = Bill_App(kh)
kh.mainloop()