from experiment import *
from tkinter import *
from tkinter import messagebox
def Inventory():
    Product.instantiate_from_csv()

    OID = Label(inventory_frame, text='Product ID', bg='#e6bf65')
    OID.grid(row=0, column=0, padx=5)

    Name = Label(inventory_frame, text='Product Name', bg='#e6bf65')
    Name.grid(row=0, column=1, padx=5)

    Stock = Label(inventory_frame, text='Product Stock', bg='#e6bf65')
    Stock.grid(row=0, column=2, padx=5)

    Trigger = Label(inventory_frame, text='Product Trigger', bg='#e6bf65')
    Trigger.grid(row=0, column=3, padx=5)

    Status = Label(inventory_frame, text='Product Status', bg='#e6bf65')
    Status.grid(row=0, column=4, padx=5)

    for items in Product.all:
        oid = Label(inventory_frame, text=items.oid, bg='#e6bf65')
        oid.grid(row=items.oid, column=0)

        name = Label(inventory_frame, text=items.name, bg='#e6bf65', height=1)
        name.grid(row=items.oid, column=1)

        stock = Label(inventory_frame, text=items.stock, bg='#e6bf65', height=1)
        stock.grid(row=items.oid, column=2)

        trigger = Label(inventory_frame, text=items.trigger, bg='#e6bf65', height=1)
        trigger.grid(row=items.oid, column=3)

        if items.status == 'restock':
            restock_status = Label(inventory_frame, text=items.status, fg = '#FF5F1F', bg='#e6bf65', height=1)
            restock_status.grid(row=items.oid, column=4)
        elif items.status == 'sold out':
            sold_out_status = Label(inventory_frame, text=items.status, fg='red', bg='#e6bf65', height=1)
            sold_out_status.grid(row=items.oid, column=4)
        elif items.status == 'good':
            status = Label(inventory_frame, text=items.status, fg='green', bg='#e6bf65', height=1)
            status.grid(row=items.oid, column=4, ipadx=5)

def Add_Item():
    global p_name
    global p_stock
    global p_trigger

    def Add():

        n = p_name.get()
        s = p_stock.get()
        t = p_trigger.get()
        try:
            Product.add_item(n, int(s), int(t))
            p_name.delete(0, END)
            p_stock.delete(0, END)
            p_trigger.delete(0, END)
            Product.instantiate_from_csv()
            add_frame.destroy()
            root.destroy()
            Main_Menu()
        except ValueError:
            messagebox.showwarning("ERROR", 'stock and trigger must be integer')


    def back():
        root.destroy()
        Main_Menu()

    canvas.destroy()
    inventory_frame.destroy()
    inventory.destroy()
    yscrollbar.destroy()
    buttons.destroy()
    add_frame = LabelFrame(root, text="Add Item", padx=5, pady=5, bg='#e6bf65')
    add_frame.grid(sticky=NW, pady=20, padx=20, column=0, row=0)

    p_name_label = Label(add_frame, text='Product Name: ', bg='#e6bf65')
    p_name_label.grid(row=0, column=0, padx=(20,5), pady=(20,5))
    p_stock_label = Label(add_frame, text='Product Stock: ', bg='#e6bf65')
    p_stock_label.grid(row=1, column=0, padx=(20, 5), pady=5)
    p_trigger_label = Label(add_frame, text='Product Trigger: ', bg='#e6bf65')
    p_trigger_label.grid(row=2, column=0, padx=(20, 5), pady=5)

    p_name = Entry(add_frame, width=40)
    p_name.grid(row=0, column=1, padx=(5, 20), pady=(20,5))
    p_stock = Entry(add_frame, width=40)
    p_stock.grid(row=1, column=1, padx=(5, 20), pady=5)
    p_trigger = Entry(add_frame, width=40)
    p_trigger.grid(row=2, column=1, padx=(5, 20), pady=5)

    add_button_frame = LabelFrame(root, text="options", pady=5, padx=5, bg='#e6bf65')
    add_button_frame.grid(row=0, column=1, sticky=NE, pady=20, padx=(5,20))

    add_button = Button(add_button_frame, text="Add Item", command=Add, bg='#b8edb2')
    add_button.grid(row=0, padx=5, pady=5)
    return_btn = Button(add_button_frame, text="back", command=back, bg= '#edbab2')
    return_btn.grid(row=1, padx=5, pady=5)

def Edit():
    def edit_inventory():

        global inv
        
        inv = LabelFrame(edit_inv_frame, text="Inventory", bg='#e6bf65')
        inv.grid(row=3, columnspan=3, padx=10, pady=10, sticky=W, ipadx=20)
        Product.instantiate_from_csv()
        OID = Label(inv, text='Product ID', bg='#e6bf65')
        OID.grid(row=0, column=0, padx=6)

        Name = Label(inv, text='Product Name', bg='#e6bf65')
        Name.grid(row=0, column=1, padx=6)

        Stock = Label(inv, text='Product Stock', bg='#e6bf65')
        Stock.grid(row=0, column=2, padx=6)

        Trigger = Label(inv, text='Product Trigger', bg='#e6bf65')
        Trigger.grid(row=0, column=3, padx=6)

        Status = Label(inv, text='Product Status', bg='#e6bf65')
        Status.grid(row=0, column=4, padx=6)

        Product.instantiate_from_csv()
        for items in Product.all:
            oid = Label(inv, text=items.oid, bg='#e6bf65')
            oid.grid(row=items.oid, column=0)

            name = Label(inv, text=items.name, bg='#e6bf65')
            name.grid(row=items.oid, column=1)

            stock = Label(inv, text=items.stock, bg='#e6bf65')
            stock.grid(row=items.oid, column=2)

            trigger = Label(inv, text=items.trigger, bg='#e6bf65')
            trigger.grid(row=items.oid, column=3)

            status = Label(inv, text=items.status, bg='#e6bf65')
            status.grid(row=items.oid, column=4)





    def Ex():
        root.destroy()
        Main_Menu()
    def delete_item():
        try:
            oid = id_entry.get()
            Product.delete_item(oid)
            Product.instantiate_from_csv()
            inv.destroy()
            edit_inventory()
        except ValueError:
            messagebox.showwarning("ERROR", 'Enter Valid Product ID')

    def search():
        def edit():
            iod = int(id_entry.get())
            n = Name_entry.get()
            s = int(Stock_entry.get())
            t = int(trigger_entry.get())
            try:
                Product.edit_item(iod, n, s, t)
                edit_inventory()
                edit_item_frame.destroy()
            except ValueError:
                messagebox.showwarning("ERROR", 'stock and trigger must be integer')
        #row3
        item = Product.all[int(id_entry.get())-1]

        edit_item_frame= LabelFrame(root, text="editing item", bg='#654321', fg='white')
        edit_item_frame.grid(row=0, column=3, pady=20, padx=(10, 20), sticky=NE)


        Prompt = LabelFrame(edit_item_frame, text='Enter new data', pady=5, padx=5, bg='#e6bf65')
        Prompt.grid(row=2, columnspan=4, padx=5, pady=10)

        Name = Label(Prompt, text='Product Name:', bg='#e6bf65')
        Name.grid(row=0, column=0, padx=5)
        Name_entry = Entry(Prompt, width=40)
        Name_entry.grid(row=0, column=1)
        stock = Label(Prompt, text='Product stock:', bg='#e6bf65')
        stock.grid(row=1, column=0, padx=5)
        Stock_entry = Entry(Prompt, width=40)
        Stock_entry.grid(row=1, column=1)
        trigger = Label(Prompt, text='Product trigger:', bg='#e6bf65')
        trigger.grid(row=2, column=0, padx=5)
        trigger_entry = Entry(Prompt, width=40)
        trigger_entry.grid(row=2, column=1)

        updt = Button(Prompt, text="update", command=edit, bg="#b8edb2")
        updt.grid(row=3, column=1, sticky=E, padx=5, pady=5)
        esc = Button(Prompt, text="close tab", command=edit_item_frame.destroy, bg='#edbab2')
        esc.grid(row=4, column=1, sticky=E, padx=5, pady=5)


        Name_entry.insert(0, item.name)
        Stock_entry.insert(0, item.stock)
        trigger_entry.insert(0, item.trigger)
    def reformat():
        Product.delete_all_item()
        root.destroy()
        Main_Menu()

    canvas.destroy()
    inventory_frame.destroy()
    inventory.destroy()
    yscrollbar.destroy()
    buttons.destroy()

    edit_inv_frame = LabelFrame(root, text="edit", bg='#654321', fg='white')
    edit_inv_frame.grid(row=0, columnspan=3, sticky=SW, pady=20, padx=20)

    Custom_Frame = LabelFrame(edit_inv_frame, pady=5, padx=5, bg='#e6bf65')
    Custom_Frame.grid(row=0, column=0, padx=10, pady=10)

    id_label = Label(Custom_Frame, text="Item ID: ", bg='#e6bf65')
    id_label.grid(row=0, column=0, pady=(10,0), padx=(20, 5), sticky=W)
    id_entry = Entry(Custom_Frame, width=50)
    id_entry.grid(row=0, column=1, pady=(10,0), padx=5, sticky=W)

    srch_button = Button(Custom_Frame, text="search item", command=search, bg='#b8edb2')
    srch_button.grid(row=0, column=2, pady=(10, 0), padx=(5, 20), sticky=NW)

    delete_button = Button(Custom_Frame, text="delete item", command=delete_item, bg= '#edbab2')
    delete_button.grid(row=1, column=2, pady=5, padx=(5, 20), sticky=NW)

    reformat_button = Button(Custom_Frame, text="delete all", command=reformat, bg='red', fg='white')
    reformat_button.grid(row=2, column=2, pady=(0,5), padx=(5, 20), sticky=NW)

    edit_inventory()

    Ex = Button(edit_inv_frame, text="back", command=Ex, bg= '#edbab2')
    Ex.grid(row=4, column=0, sticky=SE, pady=5, padx=20)

def Update():
    def Ex():
        root.destroy()
        Main_Menu()
    def Search():
        def Subtract():
            def updt():
                try:
                    id = int(ID_Entry.get())
                    Product.subtract(id, s_entry.get())
                    Inventory()
                    update_frame.destroy()
                    Update()
                except ValueError:
                    messagebox.showwarning("ERROR", 'please enter an integer')

            s_btn = Button(item_entry_frame, text="Sold Item", state=DISABLED, bg='gold')
            s_btn.grid(row=3, column=0, sticky=W, padx=5, pady=5)
            r_btn = Button(item_entry_frame, text="resupply Item", state=DISABLED, bg='#b8edb2')
            r_btn.grid(row=4, column=0, sticky=W, padx=5, pady=5)
            s_entry = Entry(item_entry_frame, width=20)
            s_entry.grid(row=3, column=1, sticky=W, padx=5, pady=5)
            update_btn = Button(item_entry_frame, text="Update", command=updt, bg='#b8edb2')
            update_btn.grid(row=3, column=2, sticky=W, padx=5, pady=5)

        def Add():
            def updt():
                try:
                    id = int(ID_Entry.get())
                    Product.add(id, s_entry.get())
                    Product.instantiate_from_csv()
                    Inventory()
                    update_frame.destroy()
                    Update()
                except ValueError:
                    messagebox.showwarning("ERROR", 'please enter an  integer')

            s_btn = Button(item_entry_frame, text="Sold Item", state=DISABLED, bg='gold')
            s_btn.grid(row=3, column=0, sticky=W, padx=5, pady=5)
            r_btn = Button(item_entry_frame, text="resupply Item", state=DISABLED, bg='#b8edb2')
            r_btn.grid(row=4, column=0, sticky=W, padx=5, pady=5)

            s_entry = Entry(item_entry_frame, width=20)
            s_entry.grid(row=4, column=1, sticky=W, padx=5, pady=5)
            update_btn = Button(item_entry_frame, text="Update", command=updt, bg='#b8edb2')
            update_btn.grid(row=4, column=2, sticky=W, padx=5, pady=5)

        item = Product.all[int(ID_Entry.get())-1]

        item_name = Label(item_entry_frame, text=item.name, bg='#e6bf65')
        item_name.grid(row=0, column=1, sticky=W, padx=5, pady=5)
        item_stock = Label(item_entry_frame, text=item.stock, bg='#e6bf65')
        item_stock.grid(row=1, column=1, sticky=W, padx=5, pady=5)
        item_trigger = Label(item_entry_frame, text=item.trigger, bg='#e6bf65')
        item_trigger.grid(row=2, column=1, sticky=W, padx=5, pady=5)

        s_btn_dummy.destroy()
        r_btn_dummy.destroy()

        s_btn = Button(item_entry_frame, text="Sold Item", command=Subtract, bg='gold')
        s_btn.grid(row=3, column=0, sticky=W, padx=5, pady=5)
        r_btn = Button(item_entry_frame, text="resupply Item", command=Add, bg='#b8edb2')
        r_btn.grid(row=4, column=0, sticky=W, padx=5, pady=5)

    # Search
    update_frame = LabelFrame(root, text="Update Window", pady=5, padx=5, bg='#654321', fg='white')
    update_frame.grid(row=0, column=1, sticky=NE, pady=20, padx=(5, 20))

    ID_label = Label(update_frame, text="Item ID: ", bg='#654321', fg='white')
    ID_label.grid(row=0, column=0, padx=5, pady=5)
    ID_Entry = Entry(update_frame, width=40)
    ID_Entry.grid(row=0, column=1, pady=5, padx=5)
    search_btn = Button(update_frame, text="search", command=Search, bg='green', fg='white')
    search_btn.grid(row=0, column=2, padx=5, pady=5)

    # Entry
    item_entry_frame = LabelFrame(update_frame, pady=5, padx=5, bg='#e6bf65')
    item_entry_frame.grid(row=1, columnspan=3, padx=5, pady=5, sticky=W)

    item_name_label = Label(item_entry_frame, text="Item Name: ", bg='#e6bf65')
    item_name_label.grid(row=0, column=0, sticky=W, padx=5, pady=5)
    item_stock_label = Label(item_entry_frame, text="Item stock: ", bg='#e6bf65')
    item_stock_label.grid(row=1, column=0, sticky=W, padx=5, pady=5)
    item_trigger_label = Label(item_entry_frame, text="Item trigger: ", bg='#e6bf65')
    item_trigger_label.grid(row=2, column=0, sticky=W, padx=5, pady=5)

    s_btn_dummy = Button(item_entry_frame, text="Sold Item", state=DISABLED, bg='gold')
    s_btn_dummy.grid(row=3, column=0, sticky=W, padx=5, pady=5)
    r_btn_dummy = Button(item_entry_frame, text="Resupply Item", state=DISABLED, bg='#b8edb2', fg='white')
    r_btn_dummy.grid(row=4, column=0, sticky=W, padx=5, pady=5)

    exit = Button(update_frame, text='close window', command=Ex, bg= '#edbab2')
    exit.grid(row=3, column=2, pady=20, padx=20)

def Main_Menu():
    global sellable_frame
    global root
    global inventory_frame
    global buttons
    global canvas
    global yscrollbar
    global inventory
    root = Tk()
    root.title("inventory app")
    root.iconbitmap('mainIcon.ico')
    root.configure(bg='#7d7761')
    root.resizable(True, False)

    inventory = LabelFrame(root,bg='#481F01', highlightbackground='#481F01' )

    buttons = LabelFrame(root, bg='#e6bf65')
    update_button = Button(buttons, text="Update Item", command=Update, activebackground='green',
                           background='#b8edb2')
    update_button.grid(row=0, pady=5, ipadx=100)
    add_product = Button(buttons, text="Add Item", command=Add_Item, activebackground='green',
                         background='#fcb530')
    add_product.grid(row=1, pady=5, ipadx=85)
    edit_product = Button(buttons, text="Edit Item", command=Edit, activebackground='green', background='#8fb8ff')
    edit_product.grid(row=2, pady=5, ipadx=70)
    exit = Button(buttons, text="Exit", command=root.quit, activebackground='red', bg='#edbab2')
    exit.grid(row=3, pady=5, ipadx=65)

    canvas = Canvas(inventory, width=450, bg='#481F01')
    canvas.pack(side=LEFT)

    yscrollbar = Scrollbar(inventory, orient='vertical', command=canvas.yview, bg='#e6bf65')
    yscrollbar.pack(side=RIGHT, fill='y')

    canvas.configure(yscrollcommand=yscrollbar.set)

    canvas.bind('<Configure>', lambda e:canvas.configure(scrollregion=canvas.bbox('all')))

    inventory_frame = Frame(canvas, bg='#e6bf65', highlightbackground='#481F01', highlightthickness=1)
    Inventory()
    canvas.create_window((0,0), window=inventory_frame)

    inventory.grid(row=0, column=0, sticky=NW, pady=20, padx=20)
    buttons.grid(row=1, column=0, sticky=SW, pady=20, padx=20)
    root.mainloop()

Main_Menu()


