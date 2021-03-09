def falsi(f, interval):
    a = interval[0]
    b = interval[1]
    MAX_ITER = 1000

    if f(a) * f(b) >= 0: 
        print("You have not assumed right a and b") 
        return -1
      
    c = a # Initialize result 
      
    for i in range(MAX_ITER): 
          
        # Find the point that touches x axis 
        c = (a * f(b) - b * f(a))/ (f(b) - f(a)) 
          
        # Check if the above found point is root 
        if f(c) == 0: 
            break
          
        # Decide the side to repeat the steps 
        elif f(c) * f(a) < 0: 
            b = c 
        else: 
            a = c 
    return c