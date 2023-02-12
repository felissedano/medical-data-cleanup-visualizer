#
# Arthur: Felis Sedano Luo
# ID: 260897013

import doctest
import datetime as dt
import numpy as np
import matplotlib.pyplot as plt



 
def date_diff(date1,date2):

    '''(str,str) -> int
    input two strings that represent dates and return the
    difference in date

    >>> date_diff('2019-10-31','2019-11-2')
    2

    '''

    num_string = '1234567890'

    year1 = int(date1[0:4])
    year2 = int(date2[0:4])


    # because some months or days have two digits and some them have only one
    # there needs to be some if state them to check the number of digits and
    # select the correct part of the data

    if date1[6] in num_string:
        month1 = int(date1[5:7])

    else:
        month1 = int(date1[5])

    if date2[6] in num_string:
        month2 = int(date2[5:7])

    else:
        month2 = int(date2[5])


    if date1[6] in num_string:
        day1 = int(date1[8:])

    else:
        day1 = int(date1[7:])

    if date2[6] in num_string:
        day2 = int(date2[8:])

    else:
        day2 = int(date2[7:])

                  
    # assign the dates to new variables
    daydiff1 = dt.date(year1,month1,day1)

    daydiff2 = dt.date(year2,month2,day2)

    # calculate by substucting two numbers

    diff = daydiff2 - daydiff1

    return diff.days




    

    
def get_age(date1,date2):

    '''(str,str) -> int
    calculate how many complete years apart are the two dates
    a year = 365.2425 days

    >>> get_age('2018-10-31','2019-11-2')
    -1

    >>> get_age('2018-10-31','2000-11-2')
    17

    '''

    # apply date_diff in the formula and devide by days in year

    year_diff = date_diff(date2,date1)/365.2425

    return int(year_diff)



########helper########

def which_state(c):

    '''(str) -> str

    input a string and return R D or I depends on what string is inputed

    >>> which_state('INFECTED')
    'I'

    >>> which_state('MORT')
    'D'

    '''
    # return new state depends on the first letter

    if c[0] == 'M' or c[0] == 'D':
        return 'D'

    if c[0] == 'I':
        return 'I'

    if c[0] == 'R':
        return 'R'

    else:
        return 'D'
    



######################


def stage_three(first_file,second_file):
    
     
    '''(str,str) -> dict

    input two files' name, open the first file, modify the date and write        it to the new file and return a dict of number of people that infected,
    recoverd or died.

    >>> stage_three('stage2.tsv','stage3.tsv')
    {0: {'I': 1, 'D': 0, 'R': 0}, 1: {'I': 2, 'D': 1, 'R': 0}, 2: {'I': 6, 'D': 0, 'R': 0}}

     '''
    original = open(first_file,'r',encoding = 'utf-8')

    out_file = open(second_file,'w',encoding = 'utf-8')

        # create a list of lines

    original_list = original.readlines()

    # the first line has the date of the first patient

    index_line = original_list[0].split('\t')

    # find the correct infected date

    index_date = index_line[2]
    

    pendamic_dict = {}
    

    for a in original_list:

        # split each word as a list
        b = a.split('\t')

        # change the date to days after the first patient
        b[2]= str(date_diff(index_date,b[2]))

        # change the date to the actual age
        b[3] = str(get_age(index_date,b[3]))

        # change the state of the patient to I,R or D

        if b[6][0] not in 'IDRM':
            b[6] = b[7]
            b[7] = b[8]
        b[6] = which_state(b[6])

        # if there is a key for the index date,then simply add 1 to the state
        if b[2] in pendamic_dict:

            pendamic_dict[b[2]][b[6]] += 1

        else:

            # create a dict for index date
            pendamic_dict[b[2]] = {'I':0,'D':0,'R':0}

            pendamic_dict[b[2]][b[6]] += 1
            
    
        c = ''

        c = '\t'.join(b)

        out_file.write(c)

    original.close()

    out_file.close()
    


    return pendamic_dict




def plot_time_series(c):

    '''(dict) -> list

    input a dictionary of number of people in each state, make them a list
    and draw a plot with x-axis = days into pendamic, y-axis = number of people
    and draw three lines of people that are in each state

    >>> d = stage_three('stage2.tsv','stage3.tsv')
    >>> plot_time_series(d)
    [[1, 0, 0], [2, 0, 1], [6, 0, 0]]

    '''

    p = {0: {'I': 1, 'D': 0, 'R': 0}, 1: {'I': 2, 'D': 1, 'R': 0}, 2: {'I': 6, 'D': 0, 'R': 0}}

    # get dict from the index dict
    dict_list = c.values()

    data_list = []

    # make them as lists
    for dicts in dict_list:
        data_list.append(list(dicts.values()))

# change the order of D and R (why cant we stick to the original order?)
    for sublist in data_list:
        sublist[1],sublist[2] = sublist[2],sublist[1]

    # arange x axis by the number of lists
    x = np.arange(len(data_list))


    # for y axis
    infected = []

    recovered = []

    dead = []

    # write the value into each y axis state
    for state in data_list:
        infected.append(state[0])

        recovered.append(state[1])

        dead.append(state[2])

        
    # create the plot    

    plt.title('Time series of early pendamic (by Felis Sedano Luo)')

    plt.xlabel('Days into pendamic')

    plt.ylabel('Number of People')

    plt.legend(['Infected','Recovered','Dead'])

    plt.plot(x,infected)

    plt.plot(x,recovered)

    plt.plot(x,dead)

    plt.savefig('time_series.png')


    
    # and return the list    
    
    return data_list




    
    



if __name__ == '__main__':
    doctest.testmod()
