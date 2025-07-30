import csv 
import random
from itertools import *
import math

with open(r'C:\Users\slava\OneDrive\Documents\exersize\Data\region_sales.csv','r') as csv_file:
    csv_reader =csv.reader(csv_file)
    header = next(csv_reader)
    
    print(header)
    
    # for line in csv_reader:
    #     line.append(random.randrange(1, 50))
    #     print(line)
    
    
    total_score=0
    max_price=0
    for line in csv_reader:
        price=line[1]  
        
        try:
            print(price)
            
            if math.isnan(float(price)):  # skip actual NaN values
                print(f"Skipping NaN value: {price}")
                continue
            total_score += float(price)
            if max_price<float(price):
                max_price=float(price)
                
         
            
        except ValueError:
            print(f"Skipping invalid value: {price}")
    print("total score", total_score,max_price)
        
        
        
 