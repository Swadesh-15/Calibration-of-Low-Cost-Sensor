from csv import reader
from csv import writer
import datetime

'''
Input sheet

1st row 
date time pm1 pm2.5 pm10

2nd row to ....
data

Output sheet
1st row
date time_slot avg_pm1 avg_pm2.5 avg_pm10

2nd row to ....
data
'''

# Reading the input csv file 

def fun_time_slot(csv_time):
    # getting the hour
    csv_time_ls = csv_time.split(":")
    if len(csv_time_ls[0])>2:
        csv_time_ls[0] = csv_time_ls[0][:2]
        # print(csv_time_ls[0])
    #print(csv_time_ls)
    if datetime.time(0,0)<= datetime.time((int)(csv_time_ls[0]),0) < datetime.time(6,0):
        return "SLOT-1"
    elif datetime.time(6,0)<= datetime.time((int)(csv_time_ls[0]),0) < datetime.time(12,0):
        return "SLOT-2"
    elif datetime.time(12,0)<= datetime.time((int)(csv_time_ls[0]),0) < datetime.time(18,0):
        return "SLOT-3"
    else:
        return "SLOT-4"
    
csv_data = []
with open("C:/Users/Rubal/Desktop/alphasense OPC.csv","r") as read_obj:
    row_no = 0
    csv_reader = reader(read_obj)
    for rows in csv_reader:
        if row_no>=1:
            csv_data.append(rows)
        row_no+=1
    read_obj.close()

# removing the empty rows
empty_rows_count=0
for rows in csv_data:
    if rows[0]=="":
        rows.clear()
        empty_rows_count+=1
print("removing empty rows -> ",empty_rows_count)
csv_data = list(filter(None,csv_data))
# print(csv_data)
output_data = []
initial_field = ["Date","Slot No.","AVG PM1","AVG PM2.5","AVG PM10"]
output_data.append(initial_field)
current_date = csv_data[0][0]    
time_slot_1_pm1=[]
time_slot_1_pm25=[]
time_slot_1_pm10=[]
time_slot_2_pm1=[]
time_slot_2_pm25=[]
time_slot_2_pm10=[]
time_slot_3_pm1=[]
time_slot_3_pm25=[]
time_slot_3_pm10=[]
time_slot_4_pm1=[]
time_slot_4_pm25=[]
time_slot_4_pm10=[]

for rows in csv_data:
    if current_date == rows[0]:
        # print("current date matches -> ",current_date)
        csv_time = rows[1]
        time_slot = fun_time_slot(csv_time)
        slot_no = time_slot
        # print(time_slot," -> ",csv_time," -> ", current_date)
        # add to the respective slot list
        if time_slot=="SLOT-1":
            time_slot_1_pm1.append((float)(rows[2]))
            time_slot_1_pm25.append((float)(rows[3]))
            time_slot_1_pm10.append((float)(rows[4]))
        elif time_slot=="SLOT-2":
            time_slot_2_pm1.append((float)(rows[2]))
            time_slot_2_pm25.append((float)(rows[3]))
            time_slot_2_pm10.append((float)(rows[4]))
        elif time_slot=="SLOT-3":
            time_slot_3_pm1.append((float)(rows[2]))
            time_slot_3_pm25.append((float)(rows[3]))
            time_slot_3_pm10.append((float)(rows[4]))
        elif time_slot=="SLOT-4":
            time_slot_4_pm1.append((float)(rows[2]))
            time_slot_4_pm25.append((float)(rows[3]))
            time_slot_4_pm10.append((float)(rows[4]))
        
    else:
        # calculate the avg for 4 slots and add it to the list
        mean_slot1_pm1=0
        mean_slot1_pm25=0
        mean_slot1_pm10=0
        mean_slot2_pm1=0
        mean_slot2_pm25=0
        mean_slot2_pm10=0
        mean_slot3_pm1=0
        mean_slot3_pm25=0
        mean_slot3_pm10=0
        mean_slot4_pm1=0
        mean_slot4_pm25=0
        mean_slot4_pm10=0
        if len(time_slot_1_pm1)==0:
            mean_slot1_pm1=0
        else:
            mean_slot1_pm1 = sum(time_slot_1_pm1)/len(time_slot_1_pm1)
        if len(time_slot_1_pm25)==0:
            mean_slot1_pm25=0
        else:
            mean_slot1_pm25 = sum(time_slot_1_pm25)/len(time_slot_1_pm25)
        if len(time_slot_1_pm10)==0:
            mean_slot1_pm10=0
        else:
            mean_slot1_pm10 = sum(time_slot_1_pm10)/len(time_slot_1_pm10)
        
        
        if len(time_slot_2_pm1)==0:
            mean_slot2_pm1=0
        else:
            mean_slot2_pm1 = sum(time_slot_2_pm1)/len(time_slot_2_pm1)
        if len(time_slot_2_pm25)==0:
            mean_slot2_pm25=0
        else:
            mean_slot2_pm25 = sum(time_slot_2_pm25)/len(time_slot_2_pm25)
        if len(time_slot_2_pm10)==0:
            mean_slot2_pm10=0
        else:
            mean_slot2_pm10 = sum(time_slot_2_pm10)/len(time_slot_2_pm10)
        
        
        if len(time_slot_3_pm1)==0:
            mean_slot3_pm1=0
        else:
            mean_slot3_pm1 = sum(time_slot_3_pm1)/len(time_slot_3_pm1)
        if len(time_slot_3_pm25)==0:
            mean_slot3_pm25=0
        else:
            mean_slot3_pm25 = sum(time_slot_3_pm25)/len(time_slot_3_pm25)
        if len(time_slot_3_pm10)==0:
            mean_slot3_pm10=0
        else:
            mean_slot3_pm10 = sum(time_slot_3_pm10)/len(time_slot_3_pm10)
        
        if len(time_slot_4_pm1)==0:
            mean_slot4_pm1=0
        else:
            mean_slot4_pm1 = sum(time_slot_4_pm1)/len(time_slot_4_pm1)
        if len(time_slot_4_pm25)==0:
            mean_slot4_pm25=0
        else:
            mean_slot4_pm25 = sum(time_slot_4_pm25)/len(time_slot_4_pm25)
        if len(time_slot_4_pm10)==0:
            mean_slot4_pm10=0
        else:
            mean_slot4_pm10 = sum(time_slot_4_pm10)/len(time_slot_4_pm10)
        
        slot_1_row_list = []
        slot_2_row_list = []
        slot_3_row_list = []
        slot_4_row_list = []
        
        slot_1_row_list.append(current_date)
        slot_1_row_list.append("SLOT-1")
        slot_1_row_list.append(mean_slot1_pm1)
        slot_1_row_list.append(mean_slot1_pm25)
        slot_1_row_list.append(mean_slot1_pm10)
        
        slot_2_row_list.append(current_date)
        slot_2_row_list.append("SLOT-2")
        slot_2_row_list.append(mean_slot2_pm1)
        slot_2_row_list.append(mean_slot2_pm25)
        slot_2_row_list.append(mean_slot2_pm10)
        
        slot_3_row_list.append(current_date)
        slot_3_row_list.append("SLOT-3")
        slot_3_row_list.append(mean_slot3_pm1)
        slot_3_row_list.append(mean_slot3_pm25)
        slot_3_row_list.append(mean_slot3_pm10)
        
        slot_4_row_list.append(current_date)
        slot_4_row_list.append("SLOT-4")
        slot_4_row_list.append(mean_slot4_pm1)
        slot_4_row_list.append(mean_slot4_pm25)
        slot_4_row_list.append(mean_slot4_pm10)
        
        
        
        output_data.append(slot_1_row_list)
        output_data.append(slot_2_row_list)
        output_data.append(slot_3_row_list)
        output_data.append(slot_4_row_list)
        
        slot_1_row_list = []
        slot_2_row_list = []
        slot_3_row_list = []
        slot_4_row_list = []
        
        
        # empty the mean list for the 4 slots
        time_slot_1_pm1=[]
        time_slot_1_pm25=[]
        time_slot_1_pm10=[]
        time_slot_2_pm1=[]
        time_slot_2_pm25=[]
        time_slot_2_pm10=[]
        time_slot_3_pm1=[]
        time_slot_3_pm25=[]
        time_slot_3_pm10=[]
        time_slot_4_pm1=[]
        time_slot_4_pm25=[]
        time_slot_4_pm10=[]
        
        current_date = rows[0]
        time_slot = fun_time_slot(csv_time)
        if time_slot=="SLOT-1":
            time_slot_1_pm1.append((float)(rows[2]))
            time_slot_1_pm25.append((float)(rows[3]))
            time_slot_1_pm10.append((float)(rows[4]))
        # add to list
        
with open("C:/Users/Rubal/Desktop/alphasense OPC.csv","w",newline="") as write_obj:  
            csv_writer = writer(write_obj)
            csv_writer.writerows(output_data)
            print(" Successuflly Completed")
            write_obj.close()
