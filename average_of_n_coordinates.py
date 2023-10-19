#function that computes centroid
def compute_centroid(*list_of_coords:list)->list:
    if len(list_of_coords):
        return []
    
    size_list = []
    for i in range(len(list_of_coords)):
        size_list.append(len(list_of_coords[i]))

    max_size = max(*size_list)#finding the maximum size of the given list, first the length of each list is stored into another list and max function is called.
    #filling zeros for max size
    centroid = [0 for i in range(max_size)]

    #computing average
    for i in range(len(list_of_coords)):
        for j in range(len(list_of_coords[i])):
            centroid[j] += list_of_coords[i][j]


    centroid = [x/len(list_of_coords) for x in centroid]
    return centroid


#function execution begins
print(''' ____ ___  __  __ ____  _   _ _____ _____    
 / ___/ _ \|  \/  |  _ \| | | |_   _| ____|   
| |  | | | | |\/| | |_) | | | | | | |  _|     
| |__| |_| | |  | |  __/| |_| | | | | |___    
 \____\___/|_|  |_|_|___ \___/  |_| |_____|_  
 / ___| ____| \ | |_   _|  _ \ / _ \_ _|  _ \ 
| |   |  _| |  \| | | | | |_) | | | | || | | |
| |___| |___| |\  | | | |  _ <| |_| | || |_| |
 \____|_____|_| \_| |_| |_| \_\\___/___|____/ ''')



#getting list of points from infinite loop that can be terminated by *
point_list = []
while (1):
    dimension = input("Enter the number of points. Enter * to exit ")
    
    if (dimension == '*' or len(dimension) == 0):
        break;

    points = []
    print('Specify the points.')
    for i in range(int(dimension)):
        points.append(float(input(f'Specify point {i+1}')))

    point_list.append(points)

#printing the average
print(f"The centroid of given points is {compute_centroid(*point_list)}")

    
    
        
        
