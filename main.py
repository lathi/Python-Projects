from selenium import webdriver

chrome_driver_path = "/Users/harshitlathi/Downloads/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.python.org")

events = driver.find_elements_by_css_selector(".event-widget li")

events_dict = {}
count = 0

# print(events[0].text.split("\n"))

for event in events:
    event_text_string = event.text.split("\n")
    events_dict[count] = {
        'time': event_text_string[0],
        'name': event_text_string[1],
    }
    count += 1

print(events_dict)

driver.quit()
