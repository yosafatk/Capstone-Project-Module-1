# DATA AWAL
emp_list = [{'Emp_no': 7 ,'Name': 'Ronaldo', 'Department': 'Marketing'}, 
            {'Emp_no': 10 ,'Name': 'Messi', 'Department': 'Finance'}]

# MAIN MENU
def main_menu() :
    input_menu = input('''---------------------------------------------
Welcome to PT. ABC Human Resources Management
          
Menu :
1. Read Employee Data
2. Create Employee Data
3. Update Employee Data
4. Delete Employee Data      
5. Exit

Enter the Menu Number: ''')

    return input_menu

# 1. READ DATA
def readData() :
    while True :
        menu1 = input('''----------------------
Read Employee Data

Menu:
1. Show All Employees
2. Choose One Employee
3. Back to Main Menu

Enter the Menu Number: ''')
            
        if menu1 == '1' :
            if emp_list == [] :
                print('\nNo Data')
            elif emp_list != []:
                print('\nEmployee List\n')
                print('Emp_no\t| Name   \t| Department')
                for i in range(len(emp_list)) :
                    print('{}\t| {}   \t| {}'.format(emp_list[i]['Emp_no'], emp_list[i]['Name'], emp_list[i]['Department']))
            
        elif menu1 == '2' :
            if emp_list == [] :
                print('\nNo Data')
                    
            elif emp_list != []:
                emp_no_inp = int(input('Enter employee number: '))
                    
                emp_no_list = []
                for i in emp_list:
                    emp_no_list.append(i['Emp_no'])
                    
                if emp_no_inp not in emp_no_list :
                    print('\nNo Data')
                        
                for i in emp_list :
                    if i['Emp_no'] == emp_no_inp :
                        print('Emp_no\t| Name   \t| Department')
                        print('{}\t| {}   \t| {}'.format(i['Emp_no'], i['Name'], i['Department']))
            
        elif menu1 == '3' :
            break

# 2. CREATE DATA
def createData() :
    while (True) :
        menu2 = input('''---------------------
Create Employee Data

Menu:
1. Add Employee
2. Back to Main Menu

Enter the Menu Number: ''')
            
        if menu2 == '1' :
            add_emp_no = int(input('Enter employee number: '))
                    
            emp_no_list = []
            for i in emp_list:
                emp_no_list.append(i['Emp_no'])
                        
            if add_emp_no in emp_no_list:
                print('Employee number already exist')

            else :    
                add_emp_name = input('Enter employee name: ')
                add_emp_dept = input(''' 
Department:
1. Marketing
2. Production
3. Finance
4. Procurement

Enter department name: ''')
                while (True) :
                    save = input('Are you sure to save this data? (Yes/No) ')
                                    
                    if save == 'Yes':
                        emp_list.append({'Emp_no': add_emp_no, 'Name': add_emp_name, 'Department': add_emp_dept})
                        print('Data has been saved')
                        break
                    elif save == 'No':
                        print('Data is not saved')
                        break                    
                    
        elif menu2 == '2' :
            break
        
# 3. UPDATE DATA
def updateData() :
    while (True):
        menu3 = input('''----------------------
Update Employee Data

Menu:
1. Update Employee
2. Back to Main Menu

Enter the Menu Number: ''')

        if menu3 == '1' :
            while (True) : 
                upd_emp_no = int(input('Enter employee number: '))
                    
                emp_no_list = []
                for i in emp_list:
                    emp_no_list.append(i['Emp_no'])
                    
                if upd_emp_no not in emp_no_list :
                    print('No employee found')
                    break
                    
                else :
                    for i in range(len(emp_list)) :
                        if emp_list[i]['Emp_no'] == upd_emp_no :
                            upd_idx = i
                            print('Emp_no\t| Name   \t| Department')
                            print('{}\t| {}   \t| {}'.format(emp_list[i]['Emp_no'], emp_list[i]['Name'], emp_list[i]['Department']))
                    
                    while (True) :    
                        update1 = input('Are you sure to update this data? (Yes/No) ')
                            
                        if update1 == 'Yes' :
                            while (True) :
                                inp_field = input('''Which field do you want to update? (Please enter the number)
1. Name
2. Department
''')
                                if inp_field == '1' :
                                    field = 'Name'
                                    break
                                elif inp_field == '2':
                                    field = 'Department'
                                    break
                                
                            inp_value = input('Please input the new value: ')
                                    
                            update2 = input('Are you sure to update this data? (Yes/No) ')
                                
                            if update2 == 'Yes' :
                                emp_list[upd_idx][field] = inp_value
                                print('Data has been updated')
                                break
                                        
                            elif update2 == 'No' :
                                break
                                    
                        elif update1 == 'No' :
                            break           
                    break
                            
        elif menu3 == '2' :
            break        

# 4. DELETE DATA
def deleteData() :
    while (True) :
        menu4 = input('''--------------------
Delete Employee Data

Menu:
1. Delete Employee
2. Back to Main Menu

Enter the Menu Number: ''')
        if menu4 == '1' :
            del_emp_no = int(input('Enter employee number: '))
                
            emp_no_list = []
            for i in emp_list:
                emp_no_list.append(i['Emp_no'])
                
            if del_emp_no not in emp_no_list :
                print('No employee found')

            else :
                while (True) :
                    del_con = input('Are you sure to delete this data? (Yes/No) ')
                    if del_con == 'Yes' :
                        for i in range(len(emp_list)) :
                            if emp_list[i]['Emp_no'] == del_emp_no :
                                del_idx = i
                                emp_list.pop(del_idx)
                                print('Employee data has been deleted')
                                break
                        break                         
                    elif del_con == 'No' :
                        break 
                
        elif menu4 == '2' :
            break


while (True) :
    menu = main_menu()
    if menu == '1' :
        readData()
    elif menu == '2' :
        createData()
    elif menu == '3' :
        updateData()
    elif menu == '4' :
        deleteData()            
    elif menu == '5' :
        break
    else:
        print('Please enter the right menu number\n')