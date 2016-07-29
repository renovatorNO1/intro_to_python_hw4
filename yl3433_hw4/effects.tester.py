##############################
# UNI:yl3433
# Name: Lucas Liu
# Assignment4
#####################
import effects
import os

def main():
    """Prompt the user to input image files and preferred effects""" 
    #Create the directory if it is not existent
    if not os.path.exists("D://pythonHW"):
        os.makedirs("D://pythonHW")
    
    print ("Please choose what effects you want to have on your picture")
    print ('1) object_filter')
    print ('2) shades_of_gray')
    print ('3) negate_red')
    print ('4) negate_green')
    print ('5) negate_blue')
    print ('6) mirror')
   
    effect_num = input("Please enter a number")
    effects_list = [False]*6
    effects_list[int(effect_num)-1] = True #Change the value to be True for selected index
    
    #Prompt the user to input primary file name
    in_file_name = input("Enter the primary input file name")
    in_file = "D://pythonHW//" + in_file_name +".PPM"
    
    if "1" in effect_num:
        #Prompt the user to input additional file names
        filter_file_name1 = input("Enter one more input file name for filter")
        filter_file_name2 = input("Please enter one more input file name for filter")

        filter_file1 = "D://pythonHW//" + filter_file_name1+".PPM"
        filter_file2 = "D://pythonHW//" + filter_file_name2+".PPM"
        
        #Prompt the user to input out file name
        out_file_name = input("Enter name of output file")
        out_file = "D://pythonHW//" + out_file_name +".PPM"
        #Apply the effect
        effects.apply_effects(in_file, out_file, effects_list,\
                              filter_file1, filter_file2)
                
    else:
        #Prompt the user to input out file name
        out_file_name = input("Enter name of output file")
        out_file = "D://pythonHW//" + out_file_name +".PPM"
        #Apply the effect
        effects.apply_effects(in_file, out_file, effects_list)
        
    print ("{:s} now created". format(out_file_name))
        
# Call the main function
main()