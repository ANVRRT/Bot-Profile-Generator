# Python_Libraries-For-Begginers     <--- IN DEVELOPMENT --->   <--- DISPLAY MESSAGES IN SPANISH --->

Modules for simple tasks, made easier for begginers.

Currently in the repo:

input_manager.py -> InputManager class:
  
    Methods:
    
        is_number(number, typeOfNumber = int)
        
            Functionality:

                Returns a number casted with the specified dataType (DEFAULT: int), if is not a number, returns False.
        
            Arguments:
            
                number: Variable to check
                typeOfNumber: Data type, (Only supports int and float)
    
        define_numbers(message = "", messageKey="", infLimit = None, supLimit = None, quantity = 1, typeOfNumber= int)

            Functionality:

                Returns a single number or a list of numbers.
        
            Arguments:
            
                message: Message displayed while taking the input
                messageKey: If assigned, will appear the number of the current iteration while  taking the current input number.
                    Example: "Example Number [{messageKey} {iter}]"
                infLimit: Inferior limit for number assignment.
                supLimit: Superior limit for number assignment.
                quantity: Number of numbers (iterations) you want to take as input
                typeOfNumber: Data type of numbers you want to input (int of float)
    
        define_string(message = "", infLimit = None, supLimit = None)
        
            Functionality:

                Returns a string received by manual input.
      
            Arguments:
                
                message: Message while taking the input
                infLimit: Inferior number of characters limit for a string input
                supLimit: Superior number of characters limit for a string input
        
        
os_manager.py -> OsManager class:

    Methods:

        clear_console_log(): Clears current using console log
        
            Arguments: No arguments needed
