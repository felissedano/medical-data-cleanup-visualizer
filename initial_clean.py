#
# Arthur: Felis Sedano Luo
# ID: 260897013

import doctest

def which_delimiter(c):
    '''(str) -> str

    input a string and return the most common delimiter
    
    >>> which_delimiter('0,1 2 3')
    ' '
    >>> which_delimiter('1\\t234')
    '\\t'
    >>> which_delimiter('hello')
    Traceback(most recent call last):
    AssertionError:No Delimiter


    '''
    # count numbers for each delimiter
    
    x = (c.count(' '))
    y = (c.count(','))
    z = (c.count('\t'))


    #if not zero then continue
    if x != 0 or y != 0 or z != 0:
        if x > y and x > z:
            return ' '

        if y > x and y > z:
            return ','

        else:
            return '\t'

     # for cases that dont have delimiter
    else:
        raise AssertionError('No Delimiter')



 
def stage_one(first_file,second_file):

    '''(str,str) -> int

    input two file name, open the first one, edit it (change symbol,upper case
    change delimiters) and create a new file and return the number of lines

    >>> stage_one('260897013.txt','stage1.tsv')
    10

    '''


            # open the two files

    original = open(first_file,'r',encoding = 'utf-8')

    # create a list of lines

    original_list = original.readlines() 

    out_file = open(second_file,'w',encoding = 'utf-8')

    


    # count number of lines
    num = len(original_list)

    # edit each line and write it to the new file
    for a in original_list:

        


        deli = which_delimiter(a)
        new = a.replace(deli,'\t')


        new = new.replace('/','-')
        new = new.replace(',','-')
        new = new.replace('.','-')
        new = new.replace(' ','')
        

        new = new.upper()

        
        out_file.write(new)



    original.close()

    out_file.close()

    return num



    
def stage_two(first_file,second_file):

    '''(str,str) -> int
    input two file names, open the first file, correct it to exactly 9
    colums and write them into the second file, then return the number of
    lines it has.

    >>> stage_two('stage1.tsv', 'stage2.tsv')
    10

    '''

    original = open(first_file,'r',encoding = 'utf-8')

    out_file = open(second_file,'w',encoding = 'utf-8')

        # create a list of lines

    original_list = original.readlines() 


    # count number of lines
    num = len(original_list)

    

    for a in original_list:


        # split each word as a list
        b = a.split('\t')

        

        # more than 9 columns
        if len(b) > 9:
            
            # combine two temp
            b[7] = b[7] + ',' + b[8]


            b[8] = b[9]

            
            b = b[:-1]

            c = ''

            c = '\t'.join(b)


            out_file.write(c)

        else:

            z = ''

            for section in b:
                z += section + ('\t')


            out_file.write(a)
                
            

    original.close

    out_file.close
    

    
    return num

    
    



if __name__ == '__main__':
    doctest.testmod()
