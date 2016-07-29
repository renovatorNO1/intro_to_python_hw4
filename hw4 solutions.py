"""
effects module for assignment 4
Date: 

@author: 

"""
import os
import statistics as stats

def apply_effects(in_filename, out_filename, effects, *filter_filenames):
    '''primary function that is called by the effects_tester. 
    in_filename the name the primary input file 
    out_filename refers is the name of the output file
    effects is a list of booleans where each position indicates whether we want
    that effect activated
	effects[0] object_filter
 	effects[1] shades_of_gray
	effects[2] indicates negate_red
	effects[3] indicates negate_green
	effects[4] indicates negate_blue
	effects[5] indicates mirror

	*filter_filenames stores the names of additional files for the object_filter
	'''
    in_file = open(in_filename, 'r')
    out_file = open(out_filename, 'w')
    temp_file = open('temp1.ppm', 'w')
    temp_list = ['temp1.ppm']

    for line in in_file:
        temp_file.write(line)
    temp_file.close()
    
    #Put all the additional files into a big list
    filter_files = []
    for filter_filename in filter_filenames:
        filter_files.append(open(filter_filename, 'r'))

    read_temp, write_temp = open_temp_files('temp1.ppm', 'temp2.ppm')
    temp_list.append('temp2.ppm')
    if effects[0]:
        filter_files.insert(0, read_temp)
        object_filter(filter_files, write_temp)
    else:
        write_file(read_temp, write_temp)
    close_read_write(read_temp, write_temp)

    read_temp, write_temp = open_temp_files('temp2.ppm', 'temp3.ppm')
    temp_list.append('temp3.ppm')
    if effects[1]:
        shades_of_gray(read_temp, write_temp)
    else:
        write_file(read_temp, write_temp)
    close_read_write(read_temp, write_temp)

    read_temp, write_temp = open_temp_files('temp3.ppm', 'temp4.ppm')
    temp_list.append('temp4.ppm')
    if effects[2]:
        negate_red(read_temp, write_temp)
    else:
        write_file(read_temp, write_temp)
    close_read_write(read_temp, write_temp)

    read_temp, write_temp = open_temp_files('temp4.ppm', 'temp5.ppm')
    temp_list.append('temp5.ppm')
    if effects[3]:
        negate_green(read_temp, write_temp)
    else:
        write_file(read_temp, write_temp)
    close_read_write(read_temp, write_temp)

    read_temp, write_temp = open_temp_files('temp5.ppm', 'temp6.ppm')
    temp_list.append('temp6.ppm')
    if effects[4]:
        negate_blue(read_temp, write_temp)
    else:
        write_file(read_temp, write_temp)
    close_read_write(read_temp, write_temp)

    read_temp, write_temp = open_temp_files('temp6.ppm','temp7.ppm')
    temp_list.append('temp7.ppm')
    if effects[5]:
        mirror(read_temp, write_temp)
    else:
        write_file(read_temp, write_temp)
    close_read_write(read_temp, write_temp)

    read_temp = open('temp7.ppm', 'r')
    write_file(read_temp, out_file)
    temp_file.close()
    read_temp.close()
    in_file.close()
    out_file.close()

    remove_temps(temp_list)


def open_temp_files(read_temp, write_temp):
    return open(read_temp, 'r'), open(write_temp, 'w')


def remove_temps(temp_list):
    for temp in temp_list:
        os.remove(temp)


def close_read_write(read_file, write_file):
    read_file.close()
    write_file.close()


def write_file(read_file, write_file):
    for line in read_file:
        write_file.write(line)


def object_filter(in_file_list, out_file):
    '''Filters out pixel values that appear in only a minority
    of the images in the parameter in_file_list'''
    
    header = read_write_header(in_file_list[0], out_file)
    for i in range(1, len(in_file_list)):
        read_write_header(in_file_list[i])

    for i in range(header['rows']):
        rows = []
        final_row = []
        for in_file in in_file_list:
            rows.append([pixel for pixel in in_file.readline().strip().split()])
        for i in range(header['cols'] * 3):
            pixels = []
            for row in rows:
                pixels.append(row[i])
            final_row.append(stats.mode(pixels))
        out_file.write(' '.join(final_row) + '\n')


def shades_of_gray(in_file, out_file):
    '''Converts the color image in_file to black and white'''
    header = read_write_header(in_file, out_file)
    for i in range(header['rows']):
        pixels = [pixel for pixel in in_file.readline().strip().split()]
        for j in range(0, len(pixels), 3):
            pixels[j] = pixels[j + 1] = pixels[j + 2]\
                = str((int(pixels[j]) + int(pixels[j+1]) + int(pixels[j+2]))//3)
        out_file.write(' '.join(pixels) + '\n')



def negate_red(in_file, out_file):
    '''Negates the red in an image'''
    negate(in_file, out_file, 0)
    

def negate_green(in_file, out_file):
    '''Negates the green in an image'''
    negate(in_file, out_file, 1)


def negate_blue(in_file, out_file):
    '''Negates the blue in an image''' 
    negate(in_file, out_file, 2)   
    

def mirror(in_file, out_file):
    '''Creates a mirror image by flipping an image horizontally''' 
    header = read_write_header(in_file, out_file)
    for i in range(header['rows']):
        pixels = [pixel for pixel in in_file.readline().strip().split()]
        pixels.reverse()
        for j in range(0, len(pixels), 3):
            temp = pixels[j]
            pixels[j] = pixels[j + 2]
            pixels[j + 2] = temp
        out_file.write(' '.join(pixels) + '\n')


def negate(in_file, out_file, start_pos):
    ''' applies the negate effect to either the r, g or b pixel pased on 
    the value of start_pos '''

    header = read_write_header(in_file, out_file)
    for i in range(header['rows']):
        pixels = [pixel for pixel in in_file.readline().strip().split()]
        for j in range(start_pos, len(pixels), 3):
            pixels[j] = str(header['color_depth'] - int(pixels[j]))
        out_file.write(' '.join(pixels) + '\n')

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

#apply_effects('black.ppm', 'red.ppm', [False, False, True, False, False, False])
#apply_effects('black.ppm', 'green.ppm', [False, False, False, True, False, False])
#apply_effects('black.ppm', 'blue.ppm', [False, False, False, False, True, False])
apply_effects('tetons2.ppm', 'mirror.ppm', [False, False, False, False, False, True])
#apply_effects('tetons1.ppm', 'test1.ppm', [False, True, False, False, False, False])
#apply_effects('tetons1.ppm', 'test1.ppm', [True, False, False, False, False, False], 'tetons2.ppm', 'tetons3.ppm')
def main():
    in_file = input("What file do you want to apply effects on?")
    out_file = input("What do you want to call your out_file?")
    choices = input("Enter the number of effects you want to apply")
    choices = list(choices)
    choices = [int(x) for x in choices]
    values = [False]*6
    for choice in choices :
        values[choice-1] = True
       
        
    apply_effects(in_file+'.ppm', out_file +'.ppm', values, 'tetons2.ppm', 'tetons3.ppm')
#main()
    
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
            
    
