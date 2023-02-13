import requests
satellite= input("enter satName:")

# Make a request to https://codedamn-classrooms.github.io/webscraper-python-codedamn-classroom-website/
# Store the result in 'res' variable
res = requests.get(
    
'https://celestrak.com/NORAD/elements/gp.php?GROUP=stations&FORMAT=tle')

txt = res.text
status = res.status_code


with open('/home/brian/Pictures/sales4.txt','w') as f:
   f.write(txt)

#raw_TLE_data = 'pythonMusvo.txt'             #Input file

filtered_TLE = '/home/brian/Pictures/sales6.txt'                      #Output file
        
        
#A function definition
def revisedTLE(line):
    with open(filtered_TLE, 'a') as fout:
        fout.write(line)
            
# Opening the raw TLE text file
TLE_data = open('/home/brian/Pictures/sales4.txt', 'r')

#Variable initialization
filteredTLElineNumber= 0
requiredSatAcquired = False
firstSatDone = 'No'

#Read TLE data, from text file, line by line
for line in TLE_data:
    #Clear variables before each iteration
    spaces = 0
    satName = ''
    
    if not line.strip():
        continue
    
    if requiredSatAcquired == True:
        revisedTLE(line)
        filteredTLElineNumber += 1
        
        if filteredTLElineNumber == 3:
            filteredTLElineNumber = 0
            requiredSatAcquired = False
            firstSatDone = 'Yes'
    
    #Clear variables before each iteration
  
    
    for value in line:
        
        
        if value != ' ': #Skip spaces
            satName = satName + value
        else:
            spaces += 1
            
        if ((spaces >= 2 and satName == 'FUTABA') or (spaces >= 2 and satName == satellite)):
            
            if (filteredTLElineNumber == 0 and firstSatDone == 'No'):
                with open(filtered_TLE, 'w') as fout:
                    fout.write(line)
            else:
                revisedTLE(line)
            
            requiredSatAcquired = True
            filteredTLElineNumber += 1
            break



        