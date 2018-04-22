5# -*- coding: cp936 -*-
import urllib
import urllib2
import re

url_1 = "http://169.254.168.150/datagen.php?type=Meas&callback=callback&_="
url_2 = 1510404285886

num_of_sample = input('Enter the how many webs you wanna catch:')

# get the smallest length of valid data1-4's length 
def mini_len( x1, x2, x3, x4):
    if(x1<=x2):
        m1 = x1
    else:
        m1 = x2
    if(x3<=x4):
        m2 = x3
    else:
        m2 = x4
    if(m1<=m2):
        m = m1
    else:
        m = m2
    return m

#open the file
print "open the data.txt to write ..."
f = open("E://data.txt","w")
f1 = open("E://data1.txt","w")
f2 = open("E://data2.txt","w")               
f3 = open("E://data3.txt","w")               
f4 = open("E://data4.txt","w")               

print "ask the http address for data..."

s = 0  #the_number_of_sample_data 

for i in range(0,(int)(num_of_sample)):
    url = url_1+ str(url_2+i)
    request = urllib2.Request(url)
    response = urllib2.urlopen(request)
    data_base = response.read()
    #print "source data :"
    #print data_base
    '''
    for i in range(0,len(data_base)/110):  #data_base /110 = 188
        print data_base[22+i*96:30+i*96],data_base[31+i*96:39+i*96],data_base[40+i*96:48+i*96],data_base[49+i*96:57+i*96]
        print
     '''
    reg1 = r'18\d\d\d0{3}'
    data_re1 = re.compile(reg1)
    data_1= re.findall(data_re1,data_base)

    reg2 = r'23\d\d\d0{3}'
    data_re2 = re.compile(reg2)
    data_2= re.findall(data_re2,data_base)

    reg3 = r'25\d\d\d0{3}'
    data_re3 = re.compile(reg3)
    data_3= re.findall(data_re3,data_base)

    reg4 = r'29\d\d\d0{3}'

    data_re4 = re.compile(reg4)
    data_4= re.findall(data_re4,data_base)
    

    min_len = mini_len(len(data_1),len(data_2),len(data_3),len(data_4))
    for i in range(0,min_len):
         #show in conlose
         print data_1[i],data_2[i],data_3[i],data_4[i]

         s = s+1
         # write to text #
         
         f1.write(data_1[i])
         f1.write('\n')
         f2.write(data_2[i])
         f2.write('\n')
         f3.write(data_3[i])
         f3.write('\n')
         f4.write(data_4[i])
         f4.write('\n')

         f.write(data_1[i])
         f.write(' ')
         f.write(data_2[i])
         f.write(' ')
         f.write(data_3[i])
         f.write(' ')
         f.write(data_4[i])
         f.write('\n')
       
# close the file
f.close()
f1.close()

f2.close()

f3.close()

f4.close()

print "Get Data finished....\n"
print "the number of sample data:",s
