# Shoprite-Saver-Search-HackHers-2020
Opt-in texting service that allows shoppers to find the brand of a product with the best price per unit at their location

Inspiration

When we were discussing the open-ended challenge offered by Wakefern, we started talking about our own experiences with shopping. All of us had memories of scouring the shelves with our parents, trying to find the cheapest price per unit. ShopRite's website allows for users to select their location and sort by unit price, but it's very cumbersome for the shopper to navigate the website in the store. Opening a website is distracting and time-consuming, but opting into a text service that can tell you the cheapest brand for your item? Simple, delightful, and transformative to the shopping experience!

What it does

Users can opt-in to the texting service by entering their phone number on our webpage. Once they do, they'll receive a text prompting them to text their zipcode back. Then, our server accesses Chrome, goes to the ShopRite Store Locator page, enters in the zipcode, and selects the closest store. The user will then receive a text asking what they're looking for; their reply is entered into the search bar, sorted by lowest unit price, and filtered into the first most-frequent category. The driver grabs the name and unit price of the first item and texts it back; with just two texts, the user finds the product with the most bang for its buck, right on their phones!

How I built it

We utilized python, Selenium webdriver, HTML, CSS, and a Twilio SMS chatbot to create the Shoprite Saver Search. Python and the webdriver were needed for backend, specifically scraping the Shoprite website for the best prices available for the user. HTML, CSS, and Twilio were used for the frontend of our idea. We created a site with a user-friendly interface that allows any customer to input a phone number and sign up for the chatbot. Next, we implemented the Twilio API and asked the user for her ZIP code to locate a nearby store. Once located, the user can input any item they’re shopping for and the webdriver will scrape the Shoprite site for the best price and send it through the chatbot. It tells the price and brand of the item. The user can repeatedly do this for any number of items they want to see.

Challenges I ran into

When we first started sorting by lowest unit price, we would sometimes get results that were irrelevant to the original search. For example, searching for "pear" would result in Tampax Pearl tampons being shown as the optimal result. To fix this, we found that adding a filter for the first most-frequent category after sorting by lowest unit price gave results that were both relevant and the lowest price. We also had a struggle with navigating some of the online elements with Selenium-- in particular, when we were trying to change the sort method from the default criteria to "Unit Price," we struggled to access the drop-down menu due to the structure of the HTML on the source website. After hours and hours of struggles, we ended up modifying the URL instead, creatively solving the problem.

Accomplishments that I'm proud of

For 2/3 of our team, this is our very first Hackathon. Erin M., who worked with front end, hadn't written in HTML before, and hadn't coded since last year. She ended up making a beautiful front-end page, taking in user data, and implementing the Twilio API. It was also Kyle's first Hackathon; he worked on backend, and during a particularly tough challenge with the drop-down menu, drew on what he knew about string modification, saw a pattern in the URLs, and created a formula to alter the search URL. Erin C focused on backend and API integration for the majority of the project, using both Twilio and Selenium for the first time, and is very proud of the new skills she learned. We ended up putting this all together and taking a broad idea, operationalizing it, and making it a reality within 24-hours. We're very proud of the way put our heads together and used unique and new tools to build a solution with real-world applications.

What I learned

In order to bring this project to fruition, we all had to learn a lot. Erin C. and Kyle learned how to use Selenium to test our hack. Meanwhile, Erin M., a first time hacker, learned many key components of HTML and CSS. As a team, we all learned how to use Python to implement our ideas, and how to solve the challenges we met along the way . Additionally, we learned how to use Twilio’s API to send and receive SMS messages.

What's next for ShopRite Saver Search

Right now, due to limitations with Twilio trial account permissions, it can only work on pre-registered phone numbers; ideally, we'd be able to expand and allow for anyone to opt-in to the service. We could also work on improving search relevancy by using string modification to ensure that users are getting the results that best apply to them. In the future, we could even implement machine learning to increase

Built With
css
emmet
flask
html
python
selenium
twilio
