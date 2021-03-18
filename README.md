#kenc323 Personal Projects

senator_trade_backtest
-
    - Using Selenium Chrome webdriver, scrape down all the submitted trades of US senator from the US Senate financial
    disclousre webpage. Then carry out event study to understand subsequent performance of stocks over a certain horizon
    after each Senator trade was carried out (using yfinance - Yahoo Finance API as pricing data source). So effectively 
    treating each Senator's trade as a long/short signal.

web_scraper / fsa_rating (WIP)
-
    - Scrape (using Selenium with Chrome driver) FSA (Food Standards Agency) hygiene ratings on takeaways restaurants
    within proximity of a postcode based on JustEat listings.
    
web_scraper / levis_web_check (WIP)
-
    - Continuous price scraping (using Selenium with Chrome driver) on selected item listings on the Levis UK e-commerce 
    store. Once a price drop (or change) is detected, an email alert is sent to the user.