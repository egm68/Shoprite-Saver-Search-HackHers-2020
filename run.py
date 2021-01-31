from flask import Flask, request, session
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from twilio.twiml.messaging_response import MessagingResponse

driver = webdriver.Chrome('/Users/ErinCorbo/Documents/math/chromedriver-2')
driver.get('https://www.shoprite.com/store-locator')
SECRET_KEY = 'shh'
app = Flask(__name__)
app.config.from_object(__name__)
callers = {
    "+19085007076": "Erin",
}
count=0;

@app.route("/sms", methods=['GET', 'POST'])
def sms_ahoy_reply():
    counter = session.get('counter', 0)
    counter += 1
    from_number = request.values.get('From')
    if from_number in callers:
        name = callers[from_number]
    else:
        name = "Friend"
    """Respond to incoming messages with a friendly SMS."""
    # Start our response
    body = request.values.get('Body', None)
    global count
    if count==0:
        if len(body)==5:
            id_box = driver.find_element_by_name('SearchTerm')
            id_box.send_keys(body)
            login_button = driver.find_element_by_class_name('searchBox__submit')
            login_button.click()
            driver.implicitly_wait(30)
            hyperlink = driver.find_element_by_class_name('store__name')
            hyperlink.click()
            message = 'Thank you! What are you shopping for today?'
            count=count+1;
        else:
            message='Please enter a 5 digit zip code!'
        resp = MessagingResponse()
            #session['state'] = state
        resp.message(message)
        return str(resp)
    else:
        print(body)
        print(count)
        driver.implicitly_wait(30)
        please = driver.find_element_by_class_name('searchBox__input')
        please.send_keys(body)
        hyperlink3 = driver.find_element_by_class_name('searchBox__submit')
        hyperlink3.click()
        driver.implicitly_wait(30)
        strin= driver.current_url
        driver.get(strin[:strin.index("search")]+'search?query='+body+'&displayType=Grid&page=1&sort=UnitPrice&title='+body+'(60)&sponsored=5')
        #driver.get('https://shop.shoprite.com/store/504c3951/search?query='+foodItem+'&displayType=Grid&page=1&sort=UnitPrice&title='+foodItem+'(60)&sponsored=5')
        driver.implicitly_wait(30)
        #hyperlink4 = driver.find_element_by_class_name('facetList__title')
        #hyperlink4.click()
        hyperlink5 = driver.find_element_by_class_name('facet__name')
        hyperlink5.click()
        name1=driver.find_element_by_class_name('product__detailsLink').text
        price = driver.find_element_by_class_name('sizeInfo__unitPrice ').text
        message = 'The best option is {} for just {}.' \
            .format(name1, price)
        resp = MessagingResponse()
            #session['state'] = state
        resp.message(message)
        return str(resp)


if __name__ == "__main__":
    app.run(debug=True)
