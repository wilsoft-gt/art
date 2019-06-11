import json
import os

# kivy load
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from functools import partial  # pass arguments from buttons
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window

kivy.require("1.11.0")
sm = ScreenManager()

################################################
####    This is the main program (no gui)   ####
################################################

# Clear the screen


def cls():
    os.system("clear")

# Show the specific info from every entry


def ShowInfo():
    cls()
    ShowData("no")
    entry = input("\nEnter a valid ID: ")
    if entry in data["id"]:
        selct = data["id"][entry]
        cls()
        print("This is the data from id %s: \n" % entry)
        print("\tTitle: ", selct["title"])
        print("\tDescription: ", selct["description"])
        print("\tSoftware used: ", selct["software"])
        print("\tTags: ", selct["tags"])
        ContOrExit()
    else:
        print("No valid Id selected, please choose a valid one.")
        ContOrExit()

# Show all data from the jsonfile


def ShowData(param):
    cls()
    info = ['Id  ', "Name"]
    print("Showing all data available \n")
    print("\t", info)
    for i in data["id"]:
        infodata = []
        infodata.append(i)
        infodata.append(data["id"][i]["title"])
        print("\t", infodata)
    if param.lower() == "si":
        ContOrExit()

# open the file we're going to wori with


def OpenFiles():
    global data
    with open('data/data.json') as json_file:
        data = json.load(json_file)

# save the file we're working with with the changes on the global class data


def SaveFile():
    with open('data/data.json', 'w') as jsonfile:
        json.dump(data, jsonfile)
    print("Se ha creado una nueva entrada")


# delete an entry from the data
""" def DeleteEntry(self, *args):
    ShowData("no")
    
    ids = input("\nIngrese el Id a eliminar: ")
    entry = input("seguro que desea eliminar la entrada %s? [Y][N]" % ids)
    if args[0].lower() == "y":
    cls()
    print(args)
    print("La entrada % ha sido eliminada!" % args)
    del data["id"][todel]
    
    SaveFile()
    MainMenu()
    else:
        cls()
        print("no cambios realizados")
        MainMenu() """

# add a new entry and add it to the data dictionary


def AddEntry():
    cls()
    print("Agregar nueva entrada! \n")
    newdic = {input("\tEnter ID: "): {
        "title": input("\tEnter Name: "),
        "description": input("\tEnter Description: "),
        "software": input("\tEnter Software: "),
        "tags": input("\tEnter Tags: ")
    }}
    data["id"].update(newdic)
    SaveFile()
    print("La entrada % ha sido ingresada con exito" % list(newdic.keys())[0])
    ContOrExit()

# show option to exti or continue working


def ContOrExit():
    z = input("\nPress [Enter] to Go to Main Menu [Q] to exit")
    if z.lower() == "q":
        quit()
    else:
        cls()
        MainMenu()

# run the main menu


def MainMenu():

    print(
        "Please select from the following Options: \n\n\t [S] Show Id's \n\t [I] Show ID Info \n\t [A] Add new entry \n\t [R] Remove entry \n\t [Q] Quit ")
    sel = input("\nSelection: ")
    if sel.lower() == "s":
        ShowData("si")
    if sel.lower() == "i":
        ShowInfo()
    if sel.lower() == "a":
        AddEntry()
#    if sel.lower() == "r":
#        DeleteEntry()
    if sel.lower() == "q":
        quit()
    else:
        print("Select a valid Option: ")
        ContOrExit()


""" OpenFiles()
MainMenu() """


##############################################
######  this section will be for kivy  #######
##############################################

class MainMenuKV(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.cols = 1
        self.view_all = Button(text="View all entries")
        self.view_all.bind(on_press=self.go_to_ShowIdsKV)
        self.add_widget(self.view_all)

        self.view_all = Button(text="Add new")
        self.view_all.bind(on_press=self.go_to_AddEntryKV)
        self.add_widget(self.view_all)

        self.view_all = Button(text="Quit")
        self.view_all.bind(on_press=self.salir)
        self.add_widget(self.view_all)

    def go_to_ShowIdsKV(self, *args):
        ShowIdsKV()
        main_class_instance.screen_manager.transition.direction = "left"
        main_class_instance.screen_manager.current = "show_ids"

    def go_to_AddEntryKV(self, *args):
        main_class_instance.screen_manager.transition.direction = "left"
        main_class_instance.screen_manager.current = "add_entry"

    def salir(self, *args):
        quit()


class ShowIdsKV(GridLayout):
    def __init__(self, **kwargs):
        self.clear_widgets()
        super().__init__(**kwargs)

        OpenFiles()
        self.sho_data()

    def sho_data(self, *args):
        # self.update()
        self.cols = 4
        OpenFiles()
        self.row_force_default = True
        self.row_default_height = 40
        self.add_widget(Label(text="Id", size_hint_x=None,
                              width=175, padding=(0, 0)))
        self.add_widget(Label(text="Title", size_hint_x=None,
                              width=175, padding=(0, 0)))
        self.add_widget(Label(text="Modify", width=15, padding=(0, 0)))
        self.add_widget(Label(text="Delete", width=15, padding=(0, 0)))

        # print(data["id"])
        i = {}
        for i in data["id"]:
            print(i)
            self.add_widget(Label(text=i))
            self.add_widget(Label(text=data["id"][i]["title"]))

            self.i = Button(text="editar")
            #self.i.bind(on_press=partial(self.showspecific, i))
            self.add_widget(self.i)

            self.dele = Button(text="eliminar")
            self.dele.bind(on_press=partial(self.deletespecific, i))
            self.add_widget(self.dele)

        self.gotomenu = Button(text="Menu")
        self.gotomenu.bind(on_press=self.go_to_MenuKV)
        self.add_widget(self.gotomenu)

        self.salir = Button(text="Update")
        self.salir.bind(on_press=self.update)
        self.add_widget(self.salir)

    def go_to_MenuKV(self, *args):
        self.clear_widgets()
        self.__init__()
        main_class_instance.screen_manager.transition.direction = "right"
        main_class_instance.screen_manager.current = "menu"

    def deletespecific(self, *args):
        del data["id"][args[0]]
        SaveFile()
        self.clear_widgets()
        self.__init__()

    def update(self, *args):
        self.clear_widgets()
        self.__init__()


class AddEntryKV(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        OpenFiles()
        self.clear_widgets()
        self.cols = 2

        self.row_force_default = True
        self.row_default_height = 40

        self.add_widget(Label(text="Add new entry"))
        self.add_widget(Label())

        self.add_widget(Label(text="Id"))
        self.entry_id = TextInput()
        self.add_widget(self.entry_id)

        self.add_widget(Label(text="Title"))
        self.entry_title = TextInput()
        self.add_widget(self.entry_title)

        self.add_widget(Label(text="Description"))
        self.entry_description = TextInput()
        self.add_widget(self.entry_description)

        self.add_widget(Label(text="Root url"))
        self.entry_root_url = TextInput()
        self.add_widget(self.entry_root_url)

        self.add_widget(Label(text="Image names"))
        self.entry_image_names = TextInput()
        self.add_widget(self.entry_image_names)

        self.add_widget(Label(text="Software"))
        self.entry_software = TextInput()
        self.add_widget(self.entry_software)

        self.add_widget(Label(text="Tags"))
        self.entry_tags = TextInput()
        self.add_widget(self.entry_tags)

        self.savefile = Button(text="Save")
        self.savefile.bind(on_press=self.save_file)
        self.add_widget(self.savefile)

        self.gotomenu = Button(text="Menu")
        self.gotomenu.bind(on_press=self.go_to_MenuKV)
        self.add_widget(self.gotomenu)

    def save_file(self, *args):
        newdic = {self.entry_id.text: {
            "title": self.entry_title.text,
            "description": self.entry_description.text,
            "mainImage": self.entry_root_url.text,
            "extraImages": self.entry_image_names.text,
            "software": self.entry_software.text,
            "tags": self.entry_tags.text
        }}

        data["id"].update(newdic)
        SaveFile()
        OpenFiles()
        self.clear_widgets()
        self.__init__()
        main_class_instance.screen_manager.transition.direction = "right"
        main_class_instance.screen_manager.current = "menu"

    def go_to_MenuKV(self, *args):
        main_class_instance.screen_manager.transition.direction = "right"
        main_class_instance.screen_manager.current = "menu"


class MainClass(App):
    def build(self):
        OpenFiles()
        self.screen_manager = ScreenManager()

        self.menuKV = MainMenuKV()
        screen = Screen(name="menu")
        screen.add_widget(self.menuKV)
        self.screen_manager.add_widget(screen)

        self.show_idsKV = ShowIdsKV()
        screen = Screen(name="show_ids")
        screen.add_widget(self.show_idsKV)
        self.screen_manager.add_widget(screen)

        self.add_entryKV = AddEntryKV()
        screen = Screen(name="add_entry")
        screen.add_widget(self.add_entryKV)
        self.screen_manager.add_widget(screen)

        return self.screen_manager


if __name__ == "__main__":
    main_class_instance = MainClass()
    main_class_instance.run()
