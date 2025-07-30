import csv 
import random
from itertools import *

with open(r'C:\Users\slava\OneDrive\Documents\exersize\Data\customers.csv','r') as csv_file:
    csv_reader =csv.reader(csv_file)
    header = next(csv_reader)
    header.append('Score')
    print(header)
    
    # for line in csv_reader:
    #     line.append(random.randrange(1, 50))
    #     print(line)
    
    
    total_score=0
    for line in islice(csv_reader, 10):
        line.append(random.randrange(1, 50))
        score=line[12]
        total_score += score
    print(total_score)
        
        
        
 