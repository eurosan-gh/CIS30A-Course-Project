

def open_txt():
    f=open("yogastyle.txt").read()
    text_display.insert(0.0, f)
        

        
    

'''window = tk.Tk()
window.title("Text File Viewer")
text_display = tk.Text(window, wrap='word')  
text_display.pack(expand=True, fill="both")
open_button = tk.Button(window, text="Open Text File", command=open_txt)
open_button.pack(pady=10)


window.mainloop()'''
