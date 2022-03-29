from bs4 import BeautifulSoup
import time,csv
import requests

START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
r=requests.get(START_URL)
#print("hello")
headers=["Proper name","Distance","Mass","Radius"]
star_data = []
final_star_data=[]
final_star_data_new =[]

def scrape():
    
    
    soup = BeautifulSoup(r.content, "html.parser")
    for row in soup.find_all("tr"):
        temp_list = []
        for index,td_tag in enumerate(row.find_all("td")):
            if index==1 :
                #for index,td_tag in enumerate(row):
                # print(index)
                # print(td_tag.text)
                temp_list.append(td_tag.text)
            else :
                temp_list.append(td_tag.text)
        star_data.append(temp_list)

    
    #print(temp_list)
    
        #     else:
        #         try:
        #             temp_list.append(td_tag.contents[0])
        #         except:
        #             temp_list.append("")
        # star_data.append(temp_list)
        # print(star_data)
# with open("scrapper_2.csv", "w") as f:
#     csvwriter = csv.writer(f)
#     csvwriter.writerow(headers)
#     csvwriter.writerows(star_data)

def remove_extra_columns() :
    for row in star_data :
        #print(row)
        del row[:1]
        #print(row)
        del row[1:2]
        #print(row)
        del row[2:3]
        #print(row)
        del row[4:5]
        #print(row)
        final_star_data.append(row)
    #print(final_star_data)

scrape()
remove_extra_columns()

# for index,data in enumerate(final_star_data) :
#     new_star_data_element=final_star_data[index]
#     new_star_data_element=new_star_data_element[:]
#     new_star_data_element=[element.replace("\n","") for element in new_star_data_element]
#     #final_star_data=[]
#     #print(new_star_data_element)
#     final_star_data_new.append(new_star_data_element)

for row in final_star_data:
    row = [element.replace("\n","")for element in row]
    final_star_data_new.append(row)
#print(final_star_data)

with open("star_data.csv","w",newline="") as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    writer.writerows(final_star_data_new)
