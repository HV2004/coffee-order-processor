import csv 
class Writer:
    def write(self,file_path,rows):
        with open(file_path,"w",newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["order_id","drink","size","price","timestamp","extras_count"])
            writer.writerows(rows)