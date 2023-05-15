from tkinter import*
import random
root=Tk()
root.title("Picnic bag pack")
root.geometry("500x500")

label1=Label(root)
label2=Label(root)
list1=["water bottle","id card","napkin","chocolate","cap","lunch box","bandage"]
label1["text"]="listed items : "+str(list1)
def bagcontent():
    random_list=random.sample(range(0,6),1)
    label2["text"]="put item number : "+str(random_list)+"  in bag"  
label1.place(relx=0.5,rely=0.4,anchor=CENTER)
label2.place(relx=0.5,rely=0.6,anchor=CENTER)
btn=Button(root,text="which item to put in bag ? ",command=bagcontent,bg="orange",fg="white")
btn.place(relx=0.5,rely=0.5,anchor=CENTER)

root.mainloop()