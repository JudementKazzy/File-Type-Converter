import tkinter as tk
import tkinter.ttk as ttk
import tkinter.filedialog as filedialog
import Extention_chager as ec

#basic setup
root = tk.Tk()
root.title("File Type Converter")
root.geometry("800x600")
root.configure(bg="lightgrey")

#upload button
def select_path():
    selected_path = filedialog.askopenfilename()
    if selected_path:
        path_entry.delete(0, tk.END)
        path_entry.insert(0, selected_path)


path_entry = tk.Entry(root, width=50, font=("Helvetica", 14))
path_entry.place(relx = 0.1, 
                 rely = 0.1
                )

browse_button = tk.Button(root, text="Upload", font=("Helvetica", 14), command=select_path)
browse_button.place(relx=0.1,
                    rely=0.3)

label_path = tk.Label(root, text="Select Upload File :", font=("Helvetica", 16), bg="lightgrey")
label_path.place(relx=0.1,
                 rely=0.2)

#Seprator
seprator = ttk.Separator(root, orient='horizontal')
seprator.place(relx=0.0, rely=0.5, relwidth=1, relheight=0.001)

#Extention entry
extention_entry = tk.Entry(root, width=20, font=("Helvetica", 14))
extention_entry.place(relx = 0.1, 
                     rely = 0.6
                    )
label_extention = tk.Label(root, text="Enter New File Extention (e.g., txt, jpg):", font=("Helvetica", 16), bg="lightgrey")
label_extention.place(relx=0.1,
                      rely=0.7
                      )

#Done button
def change_extension():
    file_path = path_entry.get()
    new_ext = extention_entry.get().strip()
    if file_path and new_ext:
        success, message = ec.change_extension(file_path, new_ext)
        done_label.config(text=message)
    else:
        done_label.config(text="Please provide both path and new extension.")

done_label = tk.Label(root, text="", font=("Helvetica", 14), bg="lightgrey")
done_label.place(relx=0.1,
                 rely=0.9)

done_button = tk.Button(root, text="Done", font=("Helvetica", 14), command=change_extension)
done_button.place(relx=0.1,
                  rely=0.8)



    

#running mainloop
root.mainloop()