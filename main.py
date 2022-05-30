#
#   Pranit Arya
#   PokeDex Search

from requests import get
import json
import tkinter as tk
from tkinter import ttk
import pokemon
import pokedex
import testing
import unittest

api_response = ""
pokemon_name = ""

narrow_down_attribute = ""

api_response_attributes =[]

pokemon_storage = pokemon.Pokemon()
pokemon_search = pokedex.Pokedex()

def ui_start():
    def search_button_handle():
        global pokemon_name
        global api_response
        global api_response_attributes

        api_response = pokemon_search.search_pokemon(pokemon_name_entry.get())
        api_response_attributes = []
        #results_label.config(text=api_response)
        i = 1
        results_label.config(text="")
        for result_name in api_response:
            results_label.config(text=results_label.cget("text")+'\n'+str(i)+". "+result_name)
            api_response_attributes.append(result_name)
            i+=1
        pokemon_storage.store_json_as_dict(api_response)
        print(api_response)
        return api_response

    def narrow_down_button_handle():
        global api_response
        global api_response_attributes
        global narrow_down_attribute

        narrow_down_attribute_index = pokemon_narrow_entry.get() #Should be integer >= 1
        narrow_down_attribute = api_response_attributes[int(narrow_down_attribute_index)-1]

        print(narrow_down_attribute)

       # narrow_down_text.config(text=json.dumps(api_response[narrow_down_attribute], indent=4))
        narrow_down_text.delete("1.0", "end")
        narrow_down_text.insert(tk.INSERT, json.dumps(api_response[narrow_down_attribute], indent=4))


        # i = 1
        # #for narrow_down_attribute_value in api_response[narrow_down_attribute]:
        #     #results_label.config(text=results_label.cget("text") + '\n' + str(i) + ". " + narrow_down_attribute_value["name"])
        #     i += 1

        return narrow_down_text

    global pokemon_name
    global api_response

    root = tk.Tk(screenName=None, baseName=None, className='Tk', useTk=1)

    main_message = tk.Label(root, text="Pokedex Project")
    main_message.pack()

    root.geometry('1000x1000')

    instructions = tk.Label(root, text="Enter desired Pokemon below and press the button to search!")
    instructions.pack()

    pokemon_name_entry = tk.Entry(root, width=50)
    pokemon_name_entry.pack()
    pokemon_name = pokemon_name_entry.get()

    ttk.Button(root, text="Search", width=20, command=search_button_handle).pack()

    results_label = tk.Label(root, text="")
    results_label.pack()

    narrow_down_instructions = tk.Label(root, text="Enter the number of the desired attribute below and press the button to narrow down!")
    narrow_down_instructions.pack()

    pokemon_narrow_entry = tk.Entry(root, width=50)
    pokemon_narrow_entry.pack()

    # canvas = tk.Canvas(root)
    # canvas.pack()

    ttk.Button(root, text="Narrow Down", width=20, command=narrow_down_button_handle).pack()

    narrow_down_text = tk.Text(root)
    # narrow_down_label.grid(sticky='w') #Align text to left
    narrow_down_text.pack()

    # scrollbar = tk.Scrollbar(canvas, orient=tk.VERTICAL, command=canvas.yview)
    # #scrollbar.place()
    # #scrollbar.config(command=canvas.yview)
    # scrollbar.place(relx=1, rely=0, relheight=1, anchor=tk.NE)
    # canvas.config(yscrollcommand=scrollbar.set, scrollregion=(0, 0, 0, (root.winfo_screenheight() / 2) - 500))
    # canvas.config(yscrollcommand=scrollbar.set)

    root.mainloop()
    
    z = 0
    if api_response != None and narrow_down_attribute != None: #For testiing purposes
        z = 1
    return z

ui_start() #Handle UI Stuff

#pokemon_name = input("Pokemon Name: ")
#attribute_name = input("What attribute do you want to know about: ")

#print(api_response)