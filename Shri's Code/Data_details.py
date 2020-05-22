import io
import re
import pandas as pd
def Data_details(file_path,type):
    df=pd.read_csv(file_path) if type=='csv' else pd.read_excel(file_path)     #csv and excel check
    initial_data = io.StringIO()
    df.info(verbose=True,buf=initial_data)
    initial_data.seek(0)
    initial_data1 =[]
    for line in initial_data.readlines()[3:-2]:                         #skip the first 3 lines and last 2 lines of the .info fn
        initial_data2 = []
        initial_data2.append(re.sub("\s +","|",line).replace("\n",""))
        for el in initial_data2:
            initial_data1.append(el.split("|")[0]+","+el.split("|")[1].split(" ")[0]+","+el.split("|")[1].split(" ")[2])
    initial_data3 = []
    for i in initial_data1:
         initial_data3.append(i.split(","))

    final_frame = pd.DataFrame(initial_data3,columns=["Column_Name","Not_Nulls","Data_Type"])
    Nulls = pd.DataFrame(df.isnull().sum()).rename_axis(index="Column_Name").rename(columns={0: "Nulls"})
    final_frame["Data_Type"]= final_frame["Data_Type"].replace({"object":"String","float64":"Float","int64":"Int"})
    result=final_frame.set_index("Column_Name").merge(Nulls,on="Column_Name")
    return result

#print(Data_details("/home/sripadapradhan/Documents/SRH_Modules/R Lectures/Datasets/Beer Consumption.csv",'csv'))
