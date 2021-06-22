import csv
import string
import os
import cam

#year='2021'
#month='01'
#day='07'
#date='2021/1/7'
def create_tsv(guard_id,year,month,day):#create a file structure according to the parameters
    path="attendence-record"
    if not os.path.exists(path):
        os.mkdir(path)
        print("Directory " , path ,  " Created ")
    else:    
        print("Directory " , path ,  " already exists")
    
    year_path = '/'+year
    if not os.path.exists(path+year_path):
        os.mkdir(path+year_path)
        print("Directory " , path +year_path,  " Created ")
    else:    
        print("Directory " , path +year_path,  " already exists")
    month_path="/"+month
    if not os.path.exists(path+year_path+month_path):
        os.mkdir(path+year_path+month_path)
        print("Directory " , path+year_path+month_path ,  " Created ")
    else:    
        print("Directory " , path+year_path+month_path ,  " already exists")
    if not os.path.exists("attendence-record/"+year+"/"+month+
        "/attendance-record-"+year+"-"+month+"-"+day+".tsv"):
        try:

            out_file=open("attendence-record/"+year+"/"+month+
            "/attendance-record-"+year+"-"+month+"-"+day+".tsv", 'wt',encoding="utf-8")
            tsv_writer = csv.writer(out_file,delimiter='\t', lineterminator='\n' )
            tsv_writer.writerow(['值班警衛ID:'+guard_id,'date:'+year+'-'+month+'-'+day])
            #tsv_writer.writerow(['employee_id',year+'-'+month+'-'+day])
            out_file.close()
        except OSError:
            print ("Creation of the directory %s failed" % path)
    else:    
        print("Directory " +"attendence-record/"+year+"/"+month+
        "/attendance-record-"+year+"-"+month+"-"+day+".tsv" +  " already exists")
 
    
if __name__ == "__main__":
    create_tsv('guard123','2021','05','23')