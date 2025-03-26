from customtkinter import *
from CreatingQR import creatingQR
from encrypted_gen import main_gen
# Initialising customtkinter window
window = CTk()
set_appearance_mode('dark')
window.title('CreatingQR')

h = 500
w = 700

bg_color = '#2C3930'
frame_color = '#3F4F44'
accent_color = '#A27B5C'
text_color = '#DCD7C9'
std_font = 'Arial Bold'
window.geometry(f'{w}x{h}')
window.resizable(width=False, height=False)
mode = True
window.configure(fg_color= bg_color)

# Pattern for creating text in a box
def TextinBox(master=window, text='some text', height=50, width=250, font_size=20, anchor='n', fpady=0, text_color='#DCD7C9', fg_color='#3F4F44', side='left' ):
    title = CTkFrame(master=master, fg_color= fg_color,  corner_radius=10, height= height, width=width)
    title.pack_propagate(False)
    title.pack(anchor=anchor, pady=fpady, side=side, padx=15)
    CTkLabel(master=title, text=text, font = (std_font, font_size), text_color=text_color, fg_color=fg_color).pack(anchor='n', pady=10)
# Actions after clicking on "Create" button
def on_btn():
    if mode: # setting text in functions
        # Using function from encrypted_gen.py to encrypt text and create QR-code with encrypted data
        main_gen(name= par_input1.get(), processor = par_input2.get(), display = par_input3.get(), ram = par_input4.get(), hdd =par_input5.get(), power_supply = par_input6.get())
    else:
        # Using function from CreatingQR.py to create QR-code with HTML code inside
        creatingQR(name= par_input1.get(), processor = par_input2.get(), display = par_input3.get(), ram = par_input4.get(), hdd =par_input5.get(), power_supply = par_input6.get())
    txt = 'Saved qr.png ...'
    # print(txt)
    frame = CTkFrame(master=main_frame, fg_color=frame_color, height=30, width=600)
    frame.pack(anchor='w', side='right', padx=7)
    frame.pack_propagate(False)
    CTkLabel(master= frame, text=txt, font=(std_font, 15), text_color=text_color).pack(anchor='ne')
    window.after(10000, frame.destroy)
def checkbox_event():
    global mode
    # print("checkbox toggled, current value:", check_var.get())
    mode = check_var.get()
check_var = BooleanVar(value=False)

# Main frontend structure:

TextinBox(text='Creating QR-code', side='top', fpady=20) # Top label

main_frame = CTkFrame(master= window, fg_color=frame_color, height= 375, width= 600)
main_frame.pack(anchor= 's', padx= 30)
main_frame.pack_propagate(False)
# Text inputs with nametags
frame1 = CTkFrame(master= main_frame, fg_color=frame_color, height= 40, width= 600)
frame1.pack(anchor= 's', pady=10)
frame1.pack_propagate(False)
TextinBox(master= frame1, height=35, width=100, fg_color=bg_color, font_size=16, text='Name', anchor='nw')
par_input1 = CTkEntry(master= frame1, height=35, width=450, corner_radius=10, fg_color=bg_color, border_color=bg_color, text_color=text_color, placeholder_text="Enter the parameter:", placeholder_text_color=text_color, font=(std_font, 16))
par_input1.pack(anchor='w')

frame2 = CTkFrame(master= main_frame, fg_color=frame_color, height= 40, width= 600)
frame2.pack(anchor= 's')
frame2.pack_propagate(False)
TextinBox(master= frame2, height=35, width=100, fg_color=bg_color, font_size=16, text='Processor', anchor='nw')
par_input2 = CTkEntry(master= frame2, height=35, width=450, corner_radius=10, fg_color=bg_color, border_color=bg_color, text_color=text_color, placeholder_text="Enter the model of the processor:", placeholder_text_color=text_color, font=(std_font, 16))
par_input2.pack(anchor='w')

frame3 = CTkFrame(master= main_frame, fg_color=frame_color, height= 40, width= 600)
frame3.pack(anchor= 's', pady=10)
frame3.pack_propagate(False)
par_text3 = TextinBox(master= frame3, height=35, width=100, fg_color=bg_color, font_size=16, text='Display', anchor='nw')
par_input3 = (CTkEntry(master= frame3, height=35, width=450, corner_radius=10, fg_color=bg_color, border_color=bg_color, text_color=text_color, placeholder_text="Enter the display resolution:", placeholder_text_color=text_color, font=(std_font, 16)))
par_input3.pack(anchor='w')

frame4 = CTkFrame(master= main_frame, fg_color=frame_color, height= 40, width= 600)
frame4.pack(anchor= 's')
frame4.pack_propagate(False)
par_text4 = TextinBox(master= frame4, height=35, width=100, fg_color=bg_color, font_size=16, text='RAM', anchor='nw')
par_input4 = CTkEntry(master= frame4, height=35, width=450, corner_radius=10, fg_color=bg_color, border_color=bg_color, text_color=text_color, placeholder_text="Enter the size of RAM:", placeholder_text_color=text_color, font=(std_font, 16))
par_input4.pack(anchor='w')

frame5 = CTkFrame(master= main_frame, fg_color=frame_color, height= 40, width= 600)
frame5.pack(anchor= 's', pady=10)
frame5.pack_propagate(False)
par_text5 = TextinBox(master= frame5, height=35, width=100, fg_color=bg_color, font_size=16, text='HDD', anchor='nw')
par_input5 = CTkEntry(master= frame5, height=35, width=450, corner_radius=10, fg_color=bg_color, border_color=bg_color, text_color=text_color, placeholder_text="Enter the size of HDD:", placeholder_text_color=text_color, font=(std_font, 16))
par_input5.pack(anchor='w')

frame6 = CTkFrame(master= main_frame, fg_color=frame_color, height= 40, width= 600)
frame6.pack(anchor= 's')
frame6.pack_propagate(False)
par_text6 = TextinBox(master= frame6, height=35, width=100, fg_color=bg_color, font_size=16, text='Power', anchor='nw')
par_input6 = CTkEntry(master= frame6, height=35, width=450, corner_radius=10, fg_color=bg_color, border_color=bg_color, text_color=text_color, placeholder_text="Enter the parameter:", placeholder_text_color=text_color, font=(std_font, 16))
par_input6.pack(anchor='w')
# Encryption mode switch
frame_interactive = CTkFrame(master= main_frame, fg_color=frame_color, height= 60, width= 600)
frame_interactive.pack(anchor= 's')
frame_interactive.pack_propagate(False)
mode_sw = CTkCheckBox(master= frame_interactive, width=180,corner_radius=10, hover_color=accent_color, fg_color=bg_color, text_color=text_color, text = 'Encryption', font=(std_font, 15), command=checkbox_event, variable=check_var, onvalue=True, offvalue=False)
mode_sw.pack(anchor='w', side='left', padx=20)
mode_sw.select()
entry_btn = CTkButton(master= frame_interactive, height=45, width=100, corner_radius=10, hover_color=accent_color, fg_color=bg_color, text_color=text_color, text='Generate QR-code', font=(std_font, 20), command=on_btn).pack(anchor='w', side='left', pady=5)
#CTkLabel(master= main_frame, text_color=text_color, height=20, width=100, text='Введите параметры устройства:', font=(std_font, 15)).pack(anchor='nw', padx=5, pady=5)par_input3 = CTkEntry(master= main_frame, height= 35, width=575, corner_radius= 10, fg_color=bg_color, border_color=bg_color, text_color=text_color, placeholder_text="Введите парaметр:", placeholder_text_color=text_color, font=(std_font, 15)).pack(anchor='nw', padx=15, pady=15)

window.mainloop()