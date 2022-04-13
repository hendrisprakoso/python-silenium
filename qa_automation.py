from selenium import webdriver
import time

parameter_testing = [
						['HENDRI SURYO PRAKOSO', 'INDONESIA', 'JAKARTA', 5105105105105100, 'April', '2022'],
						['12312313123123123b12i3hb12312n', 'INDONESIA123123', 'JAKARTA34425', 'asdasd123123', '04', 'dua puluh dua'],
						['@@#$', '$%#', '#$???', 'asd123>?', 'ASD?>?', '.""ASD?>']
					]

for param in parameter_testing:
	try:
		driver = webdriver.Chrome()
		driver.get("https://www.demoblaze.com/cart.html")
		time.sleep(5)

		driver.find_element_by_class_name("btn-success").click()
		time.sleep(1)

		driver.find_element_by_id("name").send_keys(param[0])
		time.sleep(1)

		driver.find_element_by_id("country").send_keys(param[1])
		time.sleep(1)

		driver.find_element_by_id("city").send_keys(param[2])
		time.sleep(1)

		driver.find_element_by_id("card").send_keys(param[3])
		time.sleep(1)

		driver.find_element_by_id("month").send_keys(param[4])
		time.sleep(1)

		driver.find_element_by_id("year").send_keys(param[5])
		time.sleep(1)

		driver.find_element_by_css_selector("#orderModal > div > div > div.modal-footer > button.btn.btn-primary").click()
		time.sleep(3)

		driver.find_element_by_css_selector("body > div.sweet-alert.showSweetAlert.visible > div.sa-button-container > div > button").click()
		
		time.sleep(3)
		print('Automation Successfully!')
	except Exception as e:
		print('Automation Error : ', str(e))

	driver.close()