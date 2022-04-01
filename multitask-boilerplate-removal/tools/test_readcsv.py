# import necessary libraries
import os
import glob
  
domain = []

# loop over the list of csv files
for file in os.listdir(os.getcwd()):
    if "ce" in file:
        domain_out = 0 # cleaneval
    else:
        domain_out = 1 # newdata
    domain.append(domain_out)

print(domain)