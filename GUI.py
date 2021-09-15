#Nama:Teng Tzi Yap
#Tingkatan:3 RED
#Tahun:2021

import tkinter 
from tkinter import *
from tkinter.ttk import*
from tkinter.scrolledtext import ScrolledText
from time import*


window = Tk()
window.geometry("850x430") 
window.maxsize(850,430)
window.title("💰HOME LOAN CALCULATOR💸")
icon=PhotoImage(file="logoGUI.png")
window.iconphoto(True,icon)


#Calculation
def check_dan_calmortage():
    global lblMonthlyRepayment
    global lblMonthly_Repayment
        
    
    Loan=str(strTxtLoan.get())
    try:
        Loan = float(Loan)
        
    except:
        messagebox.showerror('Invalid input',"Anda hanya boleh masukkan nombor yang betul")
        strTxtLoan.set("")
        txtLoan.focus()
        
    if Loan <= 0:
        messagebox.showerror('Invalid input',"Anda hanya boleh masukkan nombor yang betul")
        strTxtLoan.set("")
        txtLoan.focus()
        
        
    Down_Payment=str(strTxtDown_Payment.get())    
    try:
        Down_Payment = float(Down_Payment)
        
    except:
        messagebox.showerror('Invalid input',"Anda hanya boleh masukkan nombor yang betul")
        strTxtDown_Payment.set("")
        txtDown_Payment.focus()
        
    if Down_Payment <=0:
        messagebox.showerror('Invalid input',"Anda hanya boleh masukkan nombor yang betul")
        strTxtDown_Payment.set("")
        txtDown_Payment.focus()
    elif Down_Payment >=100:
        messagebox.showerror('Invalid input',"Anda hanya boleh masukkan nombor yang betul")
        strTxtDown_Payment.set("")
        txtDown_Payment.focus()
        
        
    Interest_Rate=str(strTxtInterest_Rate.get())    
    try:
        Interest_Rate = float(Interest_Rate)
        
    except:
        messagebox.showerror('Invalid input',"Anda hanya boleh masukkan nombor yang betul")
        strTxtInterest_Rate.set("")
        txtInterest_Rate.focus()
        
    if Interest_Rate <= 0:
        messagebox.showerror('Invalid input',"Anda hanya boleh masukkan nombor yang betul")
        strTxtInterest_Rate.set("")
        txtInterest_Rate.focus()
        
        
    Year=str(strTxtYear.get())    
    try:
        Year = float(Year)
        
    except:
        messagebox.showerror('Invalid input',"Anda hanya boleh masukkan nombor yang betul")
        strTxtYear.set("")
        txtYear.focus()
        
    if Year <= 0:
        messagebox.showerror('Invalid input',"Anda hanya boleh masukkan nombor yang betul")
        strTxtYear.set("")
        txtYear.focus()
        
    #Pengiraan ansuran bulanan
    Loan = Loan*((100-Down_Payment)/100)    
    Monthly_Rate = Interest_Rate/100/12
    Total_Month = Year*12
    Monthly_Repay=1-((Monthly_Rate+1)**-Total_Month)
    Monthly_Repayment= Loan*Monthly_Rate/ Monthly_Repay
    
    lblMonthlyRepayment=Label(window,text="Monthly Repayment:")
    lblMonthlyRepayment.config(font=("Copperplate Gothic Bold",13),foreground="#d6ff21",background="#759496")
    lblMonthlyRepayment.place ( x = 10 , y =370  )
    
    lblMonthly_Repayment=Label(window,text="RM"+str(format(Monthly_Repayment,"0.2f")))
    lblMonthly_Repayment.config(font=("Copperplate Gothic Bold",13),foreground="#d6ff21",background="#759496")
    lblMonthly_Repayment.place ( x = 10 , y =390  )
    loantable(Loan, Monthly_Rate,Total_Month,Monthly_Repayment)
    
  
#Reset All
def reset():
    txtLoan.delete(0, END)
    txtDown_Payment.delete(0, END)
    txtInterest_Rate.delete(0, END)
    txtYear.delete(0, END)
    txtTable.configure(state = 'normal')
    txtTable.delete('0.0',END)
    txtTable.configure(state = 'disabled')
    lblMonthlyRepayment.destroy()
    lblMonthly_Repayment.destroy()
    
def export():
    filename=filedialog.asksaveasfilename()
    files=open(filename,"w")
    receipt=txtTable.get("1.0",END)
    files.write(receipt)
    files.close()
    
#Loan Analisis Table     
def loantable(Loan, Monthly_Rate,Total_Month,Monthly_Repayment) :
    Balance = Loan
    Principal = 0.00
    InterestRate = 0.00
    Total_Principal=0.00
    Total_Interest=0.00
    Period=0
    
    txtTable.configure(state='normal')
    txtTable.delete('1.0',END)
    txtTable.update()
    
    Line1="======".rjust(3)+ "=========".rjust(12)+ "===============".rjust(17)+ "=============".rjust(15)
    LHead="\n"+"Period".rjust(3)+ "Principle".rjust(12)+ " Interest Rate ".rjust(17)+ "Balance   ".rjust(15)
    Line2="\n"+"======".rjust(3)+ "=========".rjust(12)+ "===============".rjust(17)+ "=============".rjust(15)
    
    txtTable.insert('insert',Line1)
    txtTable.insert('insert',LHead)
    txtTable.insert('insert',Line2)
    
    while Period < Total_Month:
        Period=Period+1 
        InterestRate = Balance * Monthly_Rate
        Principal = Monthly_Repayment - InterestRate
        Balance = Balance - Principal

        if Balance<=0:
            Balance=0.00
    
        Total_Principal = Total_Principal+Principal
        Total_Interest = Total_Interest+InterestRate
        
        LoanAnalisis="\n"+str(Period).rjust(3)+ str(format(Principal,"0.2f")).rjust(12)+str(
            format(InterestRate, "0.2f")).rjust(17)+str(format(Balance, "0.2f")).rjust(15)
        txtTable.insert('insert',LoanAnalisis)
        
    Line3="\n"+"=====".rjust(3)+ "=========".rjust(12)+ "===============".rjust(17)
    Total="\n"+"Total".rjust(3)+ str(format(Total_Principal, "0.2f")).rjust(11)+str(
        format(Total_Interest, "0.2f")).rjust(16)
    Line4="\n"+"=====".rjust(3)+ "=========".rjust(12)+ "===============".rjust(17)
    txtTable.insert('insert',Line3)
    txtTable.insert('insert',Total)
    txtTable.insert('insert',Line4)
    
    btnExport =Button(window,text="EXPORT",command= export)
    btnExport.place( x=725, y=380, width=80, height=30 )
    btnExport.config(state=NORMAL)
    
    
    
#Main Program

background=PhotoImage(file="Gui4.png")
lblBackground=Label(window,image=background)
lblBackground.place(x=0,y=0)


#Loan
strTxtLoan = StringVar()
txtLoan = Entry(window,textvariable =strTxtLoan )
txtLoan.place (x = 11, y = 95 , width = 170 , height = 35)

#Down Payment
strTxtDown_Payment = StringVar()
txtDown_Payment = Entry(window,textvariable =strTxtDown_Payment )
txtDown_Payment.place (x = 11, y = 153 , width = 170 , height = 35)

#Interest Rate
strTxtInterest_Rate = StringVar()
txtInterest_Rate = Entry(window,textvariable =strTxtInterest_Rate )
txtInterest_Rate.place (x = 11, y = 211 , width = 170 , height = 35)

#Year
strTxtYear = StringVar() 
txtYear = Entry(window,textvariable =strTxtYear )
txtYear.place (x = 11, y = 269 , width = 170 , height = 35)

#Button Calculate
btnCalculate =Button(window,text="CALCULATE",command=check_dan_calmortage)
btnCalculate.place( x=11, y=320, width=100, height=35 )
btnCalculate.config(state=NORMAL)

#Button Reset
btnReset =Button(window,text="RESET",command=reset)
btnReset.place( x=140, y=320, width=100, height=35 )
btnReset.config(state=NORMAL)

#Scrolled Text
txtTable=ScrolledText(window,width=59,height=20.5)
txtTable.place(x=150,y=290)
txtTable.grid(column=0, row=100, pady=74, padx=338)
txtTable.configure(state ='disabled')

window.mainloop()