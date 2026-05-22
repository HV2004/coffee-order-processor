import csv 
import logging

logger = logging.getLogger(__name__)
class Writer:
    """
    Writes processed order data into a CSV file
    """

    def write(self,file_path,rows):
        '''
        Writes rows into CSV format.
        '''
        logger.info(f"Writing CSV report: {file_path}")

        with open(file_path,"w",newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["order_id","drink","size","price","converted_total","currency","timestamp","extras_count"]) #CSV headers
            writer.writerows(rows) #Write processed rows
        
        logger.info(f"CSV rows written: {len(rows)}")