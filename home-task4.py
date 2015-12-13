#import sys
#import struct
#open_file = sys.argv[1]



###### file processing ######

#for i in range(len(file) - 1):
#    string = file[i].split(',')
#    if string[0] == '':
#        continue
#    if string[5] == 'RUR':
#        string[3] = int(string[3]) * 267
#        string[3] = int(string[4]) * 267


###### all fuel cost   ######

def all_fuel_cost(file):
    sum_of_fuel = 0
    for i in range(len(file)):
        string = file[i].split(',')
        if string[5] == 'RUR':
            string[3] = int(string[3]) * 267
        sum_of_fuel += int(string[3])
    return sum_of_fuel


###### avg money per month  ######

def avg_money_per_month(file):
    date_temp = []
    sum_per_month = 0
    for i in range(len(file) - 1):
        string = file[i].split(',')
        if string[0] == '':
            continue
        if string[5] == 'RUR':
            string[3] = int(string[3]) * 267
        sum_per_month += int(string[3])
        date_temp.append(int(string[0].split('/')[0]))

    if len(date_temp) != 0:
        quantity_of_month = 1
        for i in range(len(date_temp) - 1):
            if date_temp[i] != date_temp[i+1]:
                quantity_of_month += 1
        sum_per_month /= quantity_of_month
    else:
        sum_per_month = "no or incorrect date's in the file"
    return sum_per_month


###### avg fuel for 100 km  ######

def avg_fuel_for_100km(file):
    liter = 0
    road = 0
    for i in range(len(file)-1):
        string = file[i].split(',')
        if string[1] == '':
            continue
        if string[0] == '':
            continue
        if string[5] == 'RUR':
            string[3] = int(string[3]) * 267
        road += float(string[1])
        liter += float(string[2])
    avg_liter_per_100km = liter * 100 / road
    return avg_liter_per_100km



if __name__ == "__main__":
#    file = (open(open_file, 'rb')).readlines()
    file = (open('car_stats.txt')).readlines()
    print("All fuel cost = {}".format(all_fuel_cost(file)))
    print("Money per month for a fuel = {}".format(avg_money_per_month(file)))
    print("Avg liter's of fuel for 100 km = {}".format(avg_fuel_for_100km(file)))




