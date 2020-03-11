from selenium import webdriver

id=input()
chrome_path=r"<ENTER PATH OF CHROMEDRIVER>"
driver=webdriver.Chrome(chrome_path)
driver.get("https://www.codechef.com/users/{}".format(id))

name=driver.find_element_by_xpath("""/html/body/main/div/div/div/div/div/header/h2""")
details=driver.find_element_by_class_name("user-country-name")
state=driver.find_element_by_xpath("""/html/body/main/div/div/div/div/div/section[1]/ul/li[3]/span""")
city=driver.find_element_by_xpath("""/html/body/main/div/div/div/div/div/section[1]/ul/li[4]/span""")
stu=driver.find_element_by_xpath("""/html/body/main/div/div/div/div/div/section[1]/ul/li[5]/span""")
ins=driver.find_element_by_xpath("""/html/body/main/div/div/div/div/div/section[1]/ul/li[6]/span""")
rate=driver.find_element_by_class_name("rating-number")
gar=driver.find_element_by_xpath("""/html/body/main/div/div/div/aside/div[1]/div/div[2]/ul/li[1]/a/strong""")
car=driver.find_element_by_xpath("""/html/body/main/div/div/div/aside/div[1]/div/div[2]/ul/li[2]/a/strong""")
long=driver.find_element_by_xpath("""//*[@id="hp-sidebar-blurbRating"]/div/table/tbody/tr[1]/td[2]""")
cook=driver.find_element_by_xpath("""//*[@id="hp-sidebar-blurbRating"]/div/table/tbody/tr[2]/td[2]""")
lunch=driver.find_element_by_xpath("""//*[@id="hp-sidebar-blurbRating"]/div/table/tbody/tr[3]/td[2]""")
longr=driver.find_element_by_xpath("""//*[@id="hp-sidebar-blurbRating"]/div/table/tbody/tr[1]/td[3]/a/hx""")
cookr=driver.find_element_by_xpath("""//*[@id="hp-sidebar-blurbRating"]/div/table/tbody/tr[2]/td[3]/a/hx""")
lunchr=driver.find_element_by_xpath("""//*[@id="hp-sidebar-blurbRating"]/div/table/tbody/tr[3]/td[3]/a/hx""")
longcr=driver.find_element_by_xpath("""//*[@id="hp-sidebar-blurbRating"]/div/table/tbody/tr[1]/td[4]/a/hx""")
cookcr=driver.find_element_by_xpath("""//*[@id="hp-sidebar-blurbRating"]/div/table/tbody/tr[2]/td[4]/a/hx""")
lunchcr=driver.find_element_by_xpath("""//*[@id="hp-sidebar-blurbRating"]/div/table/tbody/tr[3]/td[4]/a/hx""")
ful=driver.find_element_by_xpath("""/html/body/main/div/div/div/div/div/section[6]/div/h5[1]""")
par=driver.find_element_by_xpath("""/html/body/main/div/div/div/div/div/section[6]/div/h5[2]""")

page="""<html>
   <body>
      <img src="https://avatars0.githubusercontent.com/u/11960354?s=400&v=4" height=100 width=1noo00>	
	<h2>"""+name.text+"""</h2>
	<h3>Personal details</h3>
	<table style="width:100%">
  		
		<tr>
    			<td>Country</th>
    			<td>"""+details.text+"""</th>
  		</tr>
  		<tr>
    			<td>State</td>
    			<td>"""+state.text+"""</td>
    			
  		</tr>
  		<tr>
    			<td>City</td>
    			<td>"""+city.text+"""</td>
  		</tr>
                <tr>
    			<td>Student/Professional</td>
    			<td>"""+stu.text+"""</td>
  		</tr>
		<tr>
    			<td>Institute</td>
    			<td>"""+ins.text+"""</td>
  		</tr>
	
	</table>
	<h3>Overall Rating="""+rate.text+"""</h3>
	<table style="width:100%">
		<tr>
			<td>Global rank="""+gar.text+"""</td>
			<td>country rank="""+car.text+"""</td>
		</tr>
	</table>
	<h4>Competition details</h4>
	<table style="width:100%">
		<tr>
			<th> Contests</th>
			<th> Rating</th>
			<th> Global rank</th>
			<th> Country rank</th>
		</tr>
		<tr>
			<td>Long Challenge</td>
			<td>"""+long.text+"""</td>
			<td>"""+longr.text+"""</td>
            <td>"""+longcr.text+"""</td>
		</tr>
		<tr>
			<td>Cookoff</td>
			<td>"""+cook.text+"""</td>
			<td>"""+cookr.text+"""</td>
            <td>"""+cookcr.text+"""</td>
		</tr>
		<tr>
			<td>Lunchtime</td>
			<td>"""+lunch.text+"""</td>
			<td>"""+lunchr.text+"""</td>
            <td>"""+lunchcr.text+"""</td>
		</tr>	
	</table>
    <h4>"""+ful.text+"""</h4>
    <h4>"""+par.text+"""</h4>
   </body>
</html>
"""
with open("output.html", "w") as f:
    print(page, file=f)
driver.get("<PATH OF OUTPUT.HTML>")