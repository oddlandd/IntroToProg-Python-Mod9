# ------------------------------------------------------------------------ #
# Title: Assignment 09
# Description: Working with Modules

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 9
# KOdland,6.14.2020,Modified code to complete assignment 9
# ------------------------------------------------------------------------ #
if __name__ == "__main__":
    from ProcessingClasses import FileProcessor as Fp
    from IOClasses import EmployeeIO as Eio
else:
    raise Exception("This file was not created to be imported")

strFileName = "EmployeeData.txt"
lstEmployeeData = []

# Main Body of Script  ---------------------------------------------------- #
# Load data from file into a list of employee objects when script starts
lstEmployeeData = Fp.read_data_from_file(strFileName)

while True:
    # Show user a menu of options
    Eio.print_menu_items()
    # Get user's menu option choice
    strChoice = Eio.input_menu_options()  # get menu option

    # Show user current data in the list of employee objects
    if strChoice == "1":
        Eio.print_current_list_items(lstEmployeeData)
    # Let user add data to the list of employee objects
    elif strChoice == "2":
        objEmp = Eio.input_employee_data()  # create new employee object
        lstEmployeeData.append(objEmp)  # append to existing list of employee objects
    # let user save current data to file
    elif strChoice == "3":
        Fp.save_data_to_file(strFileName, lstEmployeeData)
        print("Data Saved")
    # Let user exit program
    elif strChoice == "4":
        print("Ending Program")
        break
    else:
        print("Make a choice from 1 to 4")
        continue

# Main Body of Script  ---------------------------------------------------- #
