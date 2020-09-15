from time import sleep
from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome('./chromedriver')  # Optional argument, if not specified will search path.
sleep(1)
driver.get("https://ahrefs.com/tr/user/login")
sleep(1)
email = driver.find_element_by_name("email")
passw = driver.find_element_by_name("password")
sign_button = driver.find_element_by_xpath('//*[@id="root"]/div/div/div[1]/div/div/div/form/div/button')
sleep(1)
email.send_keys("tolga@partisepeti.com")
sleep(1)
passw.send_keys("Kezzo123x")
sleep(1)
sign_button.click()
sleep(1)
driver.get("https://ahrefs.com/site-explorer")
sleep(1)
domainInput = driver.find_element_by_id("se_index_target")

domainInput.send_keys("https://www.partisepeti.com/")
sleep(1)
domainButton = driver.find_element_by_id('se_index_start_analysing')
sleep(1)
domainButton.click()
sleep(1)
links = driver.find_element_by_xpath('//*[@id="backlinksCollapse"]/ul/li[1]/a')
sleep(1)
links.click()
sleep(1)

#### BAGLANTILAR SAYFASINDAKİ TABLONUN PARSER BÖLÜMÜ ###
sleep(1)
html = driver.page_source
sleep(1)
soup = BeautifulSoup(html,"html.parser")
sleep(1)
rows = soup.find_all('tr',attrs={'name':'site_explorer_data_rows'})
sleep(1)

#rows = driver.find_elements_by_name('site_explorer_data_rows')

for i in rows:
    tableColumns        = i.find_all('td')
    try:
        referTitle          = tableColumns[1].find('h4').text
    except:
        referTitle          = a[0]
    
    try:
        referUrl            = tableColumns[1].find('a').get('href')
    
    except:
        referUrl            = a[1]
    
    try:
        keywords            = int(tableColumns[8].find('a').text.strip())
        keywordUrl          = tableColumns[8].find('a').get('href')
    except:
        pass
    

    target              = tableColumns[9].find('div',attrs={'class':'truncate truncate-word'})


    targetTitle         = target.text.strip()
    targetUrl           = target.find('a').get('href')

    a = [referTitle,referUrl,targetTitle,targetUrl]

    print(f'{a[0]}, {a[1]} \t YÖNLENDİRİLİYOR \t {a[2]}, {a[3]}')


    """
        tableColumns:{
            0 : box

            referring-page's ;
                1 : title & url 
                2 : domain rating
                3 : url rating

            4 : referring domains
            5 : linked domains
            6 : external backlinks
            7 : traffic
            8 : keywords

            9 : our page's {
                'div.a.get('href')' : linked url
                'div.text'          : linked text
            }
        }
    
    """
    #tablecolumns = i.find_elements_by_tag_name("td")

    # Yonlendiren sitenin title'ı ve linki
    # titleDiv = i.find(attrs={'div','class':'.referring-page-warp breakwords'})
    # titleDivTitle = titleDiv.find_element_by_tag_name("h4").text
    # titleDivHref = titleDiv.find_element_by_tag_name("a").get_attribute("href")

    # keyword = tablecolumns[7]

    # if int(float(keyword.text)) == 0 :
    #     pass
    # else : 



#gelen  css referring-page-warp breakwords
# title h4
#gelen link
#keywords
#


