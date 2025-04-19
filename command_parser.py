# Starter code for assignment 1 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Nick Riazi
# ncriazi@uci.edu
# 14622762
import shlex
from pathlib import Path
from notebook import Notebook, Diary

def parse_command(command_list, state):
    if command_list[0] == "C":
            try:
                path = command_list[1]
                #you get path
                
                if "-n" in command_list:
                    name_index = command_list.index("-n") + 1
                    
                    notebook_name = command_list[name_index]

                else:
                    print("ERROR")
                    return
                
                dir_path = Path(path)
                if not dir_path.exists():
                    print("ERROR")
                    return

                file_path = dir_path / f"{notebook_name}.json"

                if file_path.exists():
                    print("ERROR")
                    return
                username = input("Enter your username:\n")
                password = input("Enter your password:\n")
                bio = input("Enter your bio:\n")
                nb = Notebook(username, password, bio)
                #able to do this because of the innit method in the Notebook class
                #save method in the Notebook class
                try:
                    nb.save(file_path)
                    print(f'{file_path.absolute()} CREATED')
                except Exception:
                    print("ERROR")
                
            except Exception as e:
                print("ERROR")
            
    elif command_list[0] == "D":
        try:
            
            file_path = Path(command_list[1])
            
            if file_path.suffix != ".json" or not file_path.exists():
                # check if the file exists and if it has the correct suffix
                
                print("ERROR")
                return
            
            file_path.unlink() # deletes the file
            print(f'{file_path.absolute()} DELETED')
        except Exception as e:
            
            print("ERROR")
     
    elif command_list[0] == "O":
        try:
            file_path = Path(command_list[1])
            if file_path.suffix != ".json" or not file_path.exists():
                # check if the file exists and if it has the correct suffix
                print("ERROR")
                return
            nb = Notebook("x", "x", "x")
            # create a new Notebook object with empty username, password, and bio
            # load the notebook file
            data = nb.load(file_path)

            user = input("Enter your username:\n")
            password = input("Enter your password:\n")
            # get the username and password from the user

            if nb.username != user or nb.password != password:
                print("ERROR")
                return
                # check if the username and password match
                # if they don't, print an error message and return



            #pass

            state["notebook"] = nb
            state["path"] = file_path
            print("Notebook loaded.")
            print(nb.username)
            print(nb.bio)

            return nb, file_path

            
        except Exception as e:
            
            print("ERROR:", repr(e))
            return
        
    elif command_list[0] == "E":
        notebook = state.get("notebook")
        path = state.get("path")
        # get the notebook and path from the state
        # check if the notebook and path are not None
        if notebook is None or path is None:
            print("ERROR")
            return
        # check if the notebook is loaded

        i = 1
        while i < len(command_list):
            try:
                if command_list[i] == "-usr":
                    notebook.username = command_list[i + 1]
                    i += 2
                elif command_list[i] == "-pwd":
                    notebook.password = command_list[i + 1]
                    i += 2
                elif command_list[i] == "-bio":
                    notebook.bio = command_list[i + 1]
                    i += 2
                elif command_list[i] == "-add":
                    if i + 1 < len(command_list):
                        diary = Diary(command_list[i + 1])
                        notebook.add_diary(diary)
                        i += 2
                    else:
                        print("ERROR: Missing diary name")
                        return
                elif command_list[i] == "-del":
                    if i + 1 < len(command_list):
                        try:
                            index = int(command_list[i + 1])
                            if not notebook.del_diary(index):
                                print("ERROR: Invalid index")
                                return
                        except ValueError:
                            print("ERROR: Invalid index")
                            return
                        i += 2

                    else:
                        print("ERROR: Missing diary name")
                        return
                else:
                    print("ERROR: Invalid command")
                    return
            except Exception as e:
                print("ERROR:", repr(e))
                return

        notebook.save(path)
        # save the notebook to the file
    
    elif command_list[0] == "P":
        notebook = state.get("notebook")
        if notebook is None:
            print("ERROR")
            return

        i = 1
        while i < len(command_list):
            option = command_list[i]

            if option == "-usr":
                print(notebook.username)
            elif option == "-pwd":
                print(notebook.password)
            elif option == "-bio":
                print(notebook.bio)
            elif option == "-diaries":
                for idx, diary in enumerate(notebook._diaries):
                    print(f"{idx}: {diary.entry}")
            elif option == "-diary":
                i += 1
                if i >= len(command_list):
                    print("ERROR")
                    return
                try:
                    diary_id = int(command_list[i])
                    if 0 <= diary_id < len(notebook._diaries):
                        print(notebook._diaries[diary_id].entry)
                    else:
                        print("ERROR")
                        return
                except ValueError:
                    print("ERROR")
                    return
                i += 1
            elif option == "-all":
                print(notebook.username)
                print(notebook.password)
                print(notebook.bio)
                for idx, diary in enumerate(notebook._diaries):
                    print(f"{idx}: {diary.entry}")
            else:
                print("ERROR")
                return
            i += 1
        
        
    else:
        print("ERROR")

            