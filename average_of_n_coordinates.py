#function that computes centroid
import itertools
#this function will get any number of list with different sizes and computes the centroid
def compute_centroid(*list_of_coords:list)->list:
    if len(list_of_coords) == 0:
        raise BaseException

    #used the itertools module zip_longest function - this function has an argument fillvalue it does the following
    #if i send two list, [1,2,3] and [1,2,3,4,5] as input, it has different size
    #zip longest will find out the list with longest length and the list of short lengths has the remaining indices filled with zero
    # i will be a tuple here in this case.
    centroid = [sum(i)/len(i) for i in itertools.zip_longest(*list_of_coords, fillvalue=0)]
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

    
    
        
        
