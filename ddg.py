# https://mechanicalsoup.readthedocs.io/en/stable/tutorial.html


import mechanicalsoup as ms
br = ms.StatefulBrowser()
url = "https://www.duckduckgo.com"
br.open(url)
br.get_url()
br.get_current_page()

br.select_form("form[action=/html]") #action of form -- from html
br.get_current_form().print_summary()

browser["q"] = "testing 123" #name of form
br.launch_browser()

resp = br.submit_selected()
print(resp.text)
