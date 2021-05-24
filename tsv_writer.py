import csv
import string
import csv
import cam
import os


def write_tsv(emp_id,time,year,month,day):
    path="attendence-record/"+year+"/"+month+"/attendance-record-"+year+"-"+month+"-"+day+".tsv"
    if os.path.exists(path):
        file = open(path, 'a',encoding="utf-8")
        tsv_writer = csv.writer(file,delimiter='\t', lineterminator='\n' )
        
        tsv_writer.writerow([ emp_id,time])
        file.close()
    else:
        print('tsv file does not exist yet, create it first')


if __name__ == "__main__":
    last_rec_name='test111'
    current_time='2021/05/23/23:11'
    year='2021'
    month='05'
    day='23'
    for i in range(0,20):
        write_tsv( last_rec_name,current_time,year,month,day)