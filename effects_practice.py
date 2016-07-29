# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 11:48:09 2015

@author: Yuxuan
"""

def apply_effects(in_file, out_file, effects, *filter_files):
    if effects[0]:
        in_file_list = [in_file]
        in_file_list.extend(filter_files)
        object_filter(in_file_list, out_file)
    elif effects[1]:
        shades_of_gray(in_file, out_file)
    elif effects[2]:
        negate_red(in_file, out_file)
    elif effects[3]:
        negate_green(in_file, out_file)
    elif effects[4]:
        negate_blue(in_file, out_file)
    elif effects[5]:
        mirror(in_file, out_file)

def object_filter(in_file_list, out_file):
    file_in1 = open(in_file_list[0], "r")
    file_in2 = open(in_file_list[1], "r")
    file_in3 = open(in_file_list[2], "r")
    out_file = open(out_file, "w")
    
    line1 = file_in1.readline()
    line2 = file_in2.readline()
    line3 = file_in3.readline()


    while line1 != "" and line2 != "" and line3 != "":
        
        for i in range(len(line1)):
            if line1[i] == line2[i]:
                out_file.write(line1[i])
                
            elif line1[i] == line3[i]:

                out_file.write(line1[i])
                
            elif line2[i] == line3[i]:
                out_file.write(line2[i])
                
        
        line1 = file_in1.readline()
        line2 = file_in2.readline()
        line3 = file_in3.readline()
        
    file_in1.close()
    file_in2.close()
    file_in3.close()
    out_file.close()

def shades_of_gray(in_file, out_file):
    in_file = open(in_file, "r")
    out_file = open(out_file, "w")
    
    line = in_file.readline() 
    line_counter = 0 
    while line != "":
        line_counter += 1 
        
        if line_counter < 4:
            out_file.write(line)
            
           
        else:
            
            line_list = line.rstrip().split(" ")
            
            line_num_list = [int(x) for x in line_list] 
            
            
            new_line_num_list = [] 
            for i in range(len(line_num_list)):
                if i % 3 == 0:
                    
                    average = sum(line_num_list[i:i+3])//3 
                    new_line_num_list.extend([average]*3)
            
            
            new_line_list = [str(x) for x in new_line_num_list]
            
            new_line = ' '.join(new_line_list)+'\n'
            out_file.write(new_line) 
            
        line = in_file.readline() 
        
    
    in_file.close()
    out_file.close()  

def negate_red(in_file, out_file):
    in_file = open(in_file, "r")
    out_file = open(out_file, "w")
    
    line = in_file.readline() 
    line_counter = 0 
    while line != "":
        line_counter += 1 
        
        
        if line_counter < 3:
            out_file.write(line)
        elif line_counter == 3:
            
            max_color_depth = int(line.rstrip())
            out_file.write(line)
            
           
        else:
           
            line_list = line.rstrip().split(" ") 
            
            line_num_list = [int(char) for char in line_list] 
            
           
            for i in range(len(line_num_list)):
                if i % 3 == 0:
                    line_num_list[i] = max_color_depth - line_num_list[i]
                    
               
            new_line_list = [str(num) for num in line_num_list]
            
            new_line = " ".join(new_line_list)+"\n"
            out_file.write(new_line) 

        line = in_file.readline()
        
   
    in_file.close()
    out_file.close()
    
def negate_green(in_file, out_file):
    in_file = open(in_file, "r")
    out_file = open(out_file, "w")
    
    line = in_file.readline()
    line_counter = 0 
    while line != "":
        line_counter += 1 
        
        
        if line_counter < 4:
            out_file.write(line)       
            if line_counter == 3:
                max_color_depth = int(line)
                   
        else:
            
            line_list = line.rstrip().split(" ") 

            line_num_list = [int(char) for char in line_list] 
            
            
            for i in range(len(line_num_list)):
                if i % 3 == 1:
                    new_G_value = max_color_depth - line_num_list[i]
                    line_num_list[i] = new_G_value
             
            new_line_list = [str(num) for num in line_num_list]
           
            new_line = " ".join(new_line_list)+"\n"
            out_file.write(new_line) 

        line = in_file.readline()
        
  
    in_file.close()
    out_file.close()
    
def negate_blue(in_file, out_file):

    in_file = open(in_file, "r")
    out_file = open(out_file, "w")
    
    line = in_file.readline() 
    line_counter = 0 
    while line != "":
        line_counter += 1 
        
        if line_counter < 3:
            out_file.write(line)
        elif line_counter == 3:
            
            max_color_depth = int(line.rstrip())
            out_file.write(line)
              
        else:
            
            line_list = line.rstrip().split(" ") 
          
            line_num_list = [int(char) for char in line_list] 
            for i in range(len(line_num_list)):
                if i % 3 == 2:
                    new_B_value = max_color_depth - line_num_list[i]
                    line_num_list[i] = new_B_value
            
            new_line_list = [str(num) for num in line_num_list]
            
            new_line = " ".join(new_line_list)+"\n"
            out_file.write(new_line)

        line = in_file.readline()
        
   
    in_file.close()
    out_file.close()
def mirror(in_file, out_file):
    
    in_file = open(in_file, "r")
    out_file = open(out_file, "w")
    
    # line = in_file.readline()
    line_counter = 0 
    # while line != "":
    for line in in_file:
        line_counter += 1 
               
        if line_counter < 4:
            out_file.write(line)
        
            '''elif line_counter == 34567:
            line_list = line.split()
            print (line_list)
            print (len(line_list))'''     
        else:
            
            line_num_list = line.strip().split()  
            length = len(line_num_list) 
            small_list = []
            big_list = []
            big_list2 = []
            for x in range(length):
                if x % 3 == 0:
                    small_list = [line_num_list[x], line_num_list[x+1], line_num_list[x+2]]
                    big_list.append(small_list)

            big_list.reverse()

            for x in big_list:
                for a in x:
                    big_list2.append(a) 
            
               
                '''if x % 3 == 0:
                    line_num_list[x], line_num_list[length-3-x] = \
                    line_num_list[length-3-x], line_num_list[x]
                elif x % 3 == 1:
                    line_num_list[x], line_num_list[length-1-x] = \
                    line_num_list[length-1-x], line_num_list[x]
                elif x % 3 == 2:
                    line_num_list[x], line_num_list[length+1-x] = \
                    line_num_list[length+1-x], line_num_list[x]'''
    
            
            new_line = " ".join(big_list2)+"\n"
            out_file.write(new_line)

        # line = in_file.readline()
        
    
    in_file.close()
    out_file.close()
    