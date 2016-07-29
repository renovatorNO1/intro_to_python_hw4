##############################
# UNI:yl3433
# Name: Lucas Liu
# Assignment4
#####################

def apply_effects(in_file, out_file, effects, *filter_files):
    '''primary function that is called by the effects_tester. 
    in_file the name the primary input file 
    out_filerefers is the name of the output file
    effects is a list of booleans where each position indicates whether we want
    that effect activated
	effects[0] object_filter
 	effects[1] shades_of_gray
	effects[2] indicates negate_red
	effects[3] indicates negate_green
	effects[4] indicates negate_blue
	effects[5] indicates mirror

	*filter_files stores the names of additional files for the object_filter
	'''

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
    '''Filters out pixel values that appear in only a minority
    of the images in the parameter in_file_list'''
    file_in1 = open(in_file_list[0], "r")
    file_in2 = open(in_file_list[1], "r")
    file_in3 = open(in_file_list[2], "r")
    out_file = open(out_file, "w")
    
    line1 = file_in1.readline()
    line2 = file_in2.readline()
    line3 = file_in3.readline()


    while line1 != "" and line2 != "" and line3 != "":
        line1_list = line1.strip().split()
        line2_list = line2.strip().split()
        line3_list = line3.strip().split()
        line = []
        
        for i in range(len(line1_list)):
            if line1_list[i] == line2_list[i]:
                line.append(line1_list[i])
                
            elif line1_list[i] == line3_list[i]:
                line.append(line1_list[i])
                
            elif line2_list[i] == line3_list[i]:
                line.append(line2_list[i])
        
        line = " ".join(line)+" "
        out_file.write(line)        
        line1 = file_in1.readline()
        line2 = file_in2.readline()
        line3 = file_in3.readline()
        
    file_in1.close()
    file_in2.close()
    file_in3.close()
    out_file.close()

  


def shades_of_gray(in_file, out_file):
    '''Converts the color image in_file to black and white'''
    in_file = open(in_file, "r")
    out_file = open(out_file, "w")
    
    line = in_file.readline() #Read the first line
    line_counter = 0 #Set up a counter to keep track of the line number
    while line != "":
        line_counter += 1 # Increment the counter by 1
        
        #Copy the first 3 lines, namely the header, into the out_file
        if line_counter < 4:
            out_file.write(line)
 
        #Turn every RGB value into the average of the three    
        else:
            #Turn the line into a list without whitespace at the end
            line_list = line.strip().split()
            #Turn elements of the line_list into integers
            line_num_list = [int(x) for x in line_list] 
            
            
            new_line_num_list = [] #Create this list to store the average RGB values
            for i in range(len(line_num_list)):
                if i % 3 == 0:
                    #Calculate the average value of every three elements 
                    #And add the average value three times into the newly created list
                    average = sum(line_num_list[i:i+3])//3 
                    new_line_num_list.extend([average]*3)
            
            #Turn all the elements of the newly created list into str
            new_line_list = [str(x) for x in new_line_num_list]
            #Join the elements together with '\n' at the end indicate the end of a line
            new_line = ' '.join(new_line_list)+'\n'
            out_file.write(new_line) #Write the line into the out_file
            
        line = in_file.readline() #Go to the next line
   
    #Close the two files
    in_file.close()
    out_file.close()


def negate_red(in_file, out_file):
    '''Negates the red in an image'''
    in_file = open(in_file, "r")
    out_file = open(out_file, "w")
    
    line = in_file.readline() #Read the first line
    line_counter = 0 #Set up a counter to keep track of the line number
    while line != "":
        line_counter += 1 # Increment the counter by 1
        
        #Copy the first 3 lines, namely the header, into the out_file
        if line_counter < 4:
            out_file.write(line)       
            if line_counter == 3:
                max_color_depth = int(line)
            
        #Alter every R value    
        else:
            #Turn the line into a list without whitespace at the end
            line_list = line.strip().split() 
            # Turn elements of the line_list into integers
            line_num_list = [int(char) for char in line_list] 
            
            #Change every R value
            for i in range(len(line_num_list)):
                if i % 3 == 0:
                    line_num_list[i] = max_color_depth - line_num_list[i]
                    
            #Turn all the elements of the newly created list into str        
            new_line_list = [str(num) for num in line_num_list]
            #Join the elements together with '\n' at the end indicate the end of a line
            new_line = " ".join(new_line_list)+"\n"
            out_file.write(new_line) #Write the line into the out_file

        line = in_file.readline()#Go to the next line
        
    #Close the two files
    in_file.close()
    out_file.close()

    
def negate_green(in_file, out_file):
    '''Negates the green in an image'''
    in_file = open(in_file, "r")
    out_file = open(out_file, "w")
    
    line = in_file.readline() #Read the first line
    line_counter = 0 #Set up a counter to keep track of the line number
    while line != "":
        line_counter += 1 # Increment the counter by 1
        
        #Copy the first 3 lines, namely the header, into the out_file
        if line_counter < 4:
            out_file.write(line)       
            if line_counter == 3:
                #Save the maximum color depth
                max_color_depth = int(line)
            
        #Alter every G value    
        else:
            #Turn the line into a list without whitespace at the end
            line_list = line.strip().split() 
            # Turn elements of the line_list into integers
            line_num_list = [int(char) for char in line_list] 
            
            #Change every G value
            for i in range(len(line_num_list)):
                if i % 3 == 1:
                    new_G_value = max_color_depth - line_num_list[i]
                    line_num_list[i] = new_G_value
            #Turn all the elements of the newly created list into str        
            new_line_list = [str(num) for num in line_num_list]
            #Join the elements together with '\n' at the end indicate the end of a line
            new_line = " ".join(new_line_list)+"\n"
            out_file.write(new_line) #Write the line into the out_file

        line = in_file.readline()#Go to the next line
        
    #Close the two files
    in_file.close()
    out_file.close()

def negate_blue(in_file, out_file):
    '''Negates the blue in an image'''  
    in_file = open(in_file, "r")
    out_file = open(out_file, "w")
    
    line = in_file.readline() #Read the first line
    line_counter = 0 #Set up a counter to keep track of the line number
    while line != "":
        line_counter += 1 # Increment the counter by 1
        
        #Copy the first 3 lines, namely the header, into the out_file
        if line_counter < 4:
            out_file.write(line)       
            if line_counter == 3:
                #Save the maximum color depth
                max_color_depth = int(line)
            
        #Alter every G value    
        else:
            #Turn the line into a list without whitespace at the end
            line_list = line.strip().split() 
            # Turn elements of the line_list into integers
            line_num_list = [int(char) for char in line_list] 
            for i in range(len(line_num_list)):
                if i % 3 == 2:
                    new_B_value = max_color_depth - line_num_list[i]
                    line_num_list[i] = new_B_value
            #Turn all the elements of the newly created list into str        
            new_line_list = [str(num) for num in line_num_list]
            #Join the elements together with '\n' at the end indicate the end of a line
            new_line = " ".join(new_line_list)+"\n"
            out_file.write(new_line) #Write the line into the out_file

        line = in_file.readline()#Go to the next line
        
    #Close the two files
    in_file.close()
    out_file.close()
    
def mirror(in_file, out_file):
    '''Creates a mirror image by flipping an image horizontally'''
    in_file = open(in_file, "r")
    out_file = open(out_file, "w")
    
    line = in_file.readline() #Read the first line
    line_counter = 0 #Set up a counter to keep track of the line number
    while line != "":
        line_counter += 1 # Increment the counter by 1
        
        #Copy the first 3 lines, namely the header, into the out_file
        if line_counter < 4:
            out_file.write(line)
            
            
        else:
            #Turn the line into a list without whitespace at the end
            line_list = line.strip().split() 
            # Turn elements of the line_list into integers
            line_num_list = [int(char) for char in line_list]
            #store the length of line_num_list into length for later use
            length = len(line_num_list)
            
            #set the range as half length to make sure swapping only happens onece on each index
            for x in range(length // 2):
                #Swap the values of two R indices
                if x % 3 == 0:
                    line_num_list[x], line_num_list[length-3-x] = \
                    line_num_list[length-3-x], line_num_list[x]
                    
                #Swap the values of two G indices
                elif x % 3 == 1:
                    line_num_list[x], line_num_list[length-1-x] = \
                    line_num_list[length-1-x], line_num_list[x]
                    
                #Swap the values of two G indices
                elif x % 3 == 2:
                    line_num_list[x], line_num_list[length+1-x] = \
                    line_num_list[length+1-x], line_num_list[x]
                    
            #Turn all the elements of the newly created list into str        
            new_line_list = [str(num) for num in line_num_list]
            #Join the elements together with '\n' at the end indicate the end of a line
            new_line = " ".join(new_line_list)+" "
            out_file.write(new_line) #Write the line into the out_file

        line = in_file.readline()#Go to the next line
        
    #Close the two files
    in_file.close()
    out_file.close()
def read_write_header(in_file, out_file=None):
    ''' reads and parses the ppm header and writes it to the output file '''
    magic_number = in_file.readline()
    dimens = in_file.readline()
    color_depth = in_file.readline()

    cols_rows = dimens.split()
    cols = int(cols_rows[0])
    rows = int(cols_rows[1])

    if out_file:
        out_file.write(magic_number + dimens + color_depth)

    return { 'cols' : cols, 'rows' : rows, 'color_depth' : int(color_depth) }

def read_write_file(infile, outfile):
    with open(infile, 'r') as in_file:
        out_file = open(outfile, 'w')
        
        #for line in in_file:
         #   print(line, file=out_file)
        #lines = []
        header = read_write_header(in_file, out_file)
        all_lines = in_file.read()
        lines = all_lines.strip().split()
        print(len(lines))
        width = header['cols']
        k = 0
        for i in range(header['rows']):
            line = lines[k:k+width*3]
            line_to_write = ' '.join(line)
            print(line_to_write, file=out_file)
            k = k+width*3
        #print(header['rows'])
        #for i in range(header['rows']):
          #line = in_file.readline().strip().split()
          #lines.extend(line) 
          #line_to_write = ' '.join(line) 
          #print(line_to_write, file=out_file)
        out_file.close()

read_write_file('tetons2.ppm', 'test2.ppm')
mirror('test2.ppm', 'test3.ppm')