# Will convert all the temparature in a list
temps = input('Enter Temparature as Space Separated:').split(' ')
if len(temps)<2:
    print('Please give atleast two values...')
else:    
    # To convert each temparature to floating-point vlaues with 2-decimal place
    for i in range(0, len(temps)):
        try:
            temps[i] = round(float(temps[i]),2)
        except ValueError:
            print(f"Invalid entry at index {i}: '{temps[i]}' is not a valid number.")
            print('Enter all neumeric values')
            exit(0)

    # Logic to check all tempratures all fall in a range or not
    for i in range(0, len(temps)):
        if temps[i] <-100.0 or temps[i] > 60.0:
            print('Please give all the values in range (-100, +60)')
            print(temps)
            exit(0)
    
    # Get display all tempratures
    for i in range(0,len(temps)):
        print(f"{temps[i]}", end=' ')
    print()             
        
    #Find the highest and lowest temparature
    total_temp = min_temp = max_temp = temps[0]
    for i in range(1, len(temps)):
        if min_temp > temps[i]:
            min_temp = temps[i]
        if max_temp < temps[i]:
            max_temp = temps[i]
        total_temp += temps[i]
    print(f"Highest: {max_temp}")
    print(f"Lowest: {min_temp}")
    print(f"Average: {total_temp/len(temps):.2f}")

    #using Python in-built functions
    print(f"Max = {max(temps)}, Min = {min(temps)}, Avg ={sum(temps)/len(temps):.2f}")