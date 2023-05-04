from tkinter import *
import tkinter.font as font


root = Tk()
root.geometry("500x600")
root.title("Calc")
root.resizable(50,50)
inp = StringVar()
myFont = font.Font(size=12)

screen = Entry(root, text=inp, width=46, justify='right', font=10, bd=4)
screen.grid(row=0, columnspan=4, padx=5, pady=30, ipady=30) 
key_matrix = [["Clear", u"\u221A", "/", "Del"],  
              ["7", "8", "9", "*"], 
              ["4", "5", "6", "-"],  
              ["1", "2", "3", "+"], 
              ["!", 0, ".", "="]] 

btn_dict = {} 
ans_to_print = 0
def Calculate(event): 
    
    
    button = event.widget.cget("text") 
  
    
    global key_matrix, inp, ans_to_print 
  
    try:
        if button == u"\u221A":
            ans = float(inp.get())**(0.5) 
            ans_to_print = str(ans) 
            inp.set(str(ans)) 
        elif button == "Clear":
            inp.set("") 
        elif button == "!":
            def fact(n): return 1 if n == 0 else n*fact(n-1) 
            inp.set(str(fact(int(inp.get())))) 
        elif button == "Del":
            inp.set(inp.get()[:len(inp.get())-1]) 
        elif button == "=":  
            ans_to_print = str(eval(inp.get())) 
            inp.set(ans_to_print) 
        else: 
            inp.set(inp.get()+str(button)) 
  
    except: 
      inp.set("Wrong Operation") 
  
  
  
for i in range(len(key_matrix)):   
    
    for j in range(len(key_matrix[i])):   
        btn_dict["btn_"+str(key_matrix[i][j])] = Button( 
          root, bd=1, text=str(key_matrix[i][j]), font=myFont) 
        
        btn_dict["btn_"+str(key_matrix[i][j])].grid( 
          row=i+1, column=j, padx=2, pady=2, ipadx=25, ipady=25) 
        
        btn_dict["btn_"+str(key_matrix[i][j])].bind('<Button-1>', Calculate) 

root.mainloop()