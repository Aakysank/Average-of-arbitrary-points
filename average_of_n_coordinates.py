#function that computes centroid
from itertools import zip_longest
def compute_centroid(*list_of_coords:list)->list:
    if len(list_of_coords) == 0:
        return []

    centroid = []
    for i,j in zip_longest(*list_of_coords, fillvalue=0):
        number = i+j
        centroid.append(number)

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

    
    
        
        
