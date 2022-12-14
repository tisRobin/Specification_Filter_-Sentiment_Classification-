{
 "metadata": {
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.1"
  },
  "orig_nbformat": 2,
  "kernelspec": {
   "name": "python391jvsc74a57bd0696f1b3f4ec608302c0ac7d485b61cbe5cb6c2ed50640f9120220e665ff62020",
   "display_name": "Python 3.9.1 64-bit"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2,
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import csv\n",
    "from selenium import webdriver\n",
    "from selenium.webdriver.support.ui import WebDriverWait\n",
    "from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException\n",
    "from bs4 import BeautifulSoup\n",
    "import requests"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [],
   "source": [
    "chrome_driver_path = \"C:\\\\Users\\\\nicol\\\\OneDrive\\\\Desktop\\\\Datum Proj\\\\chromedriver.exe\"\n",
    "driver = webdriver.Chrome(executable_path=chrome_driver_path)\n",
    "product_data_df = pd.DataFrame(columns=['Category', 'URL', 'Brand', 'Product_name', 'Price', 'Hearts', 'Total_Stars', 'Reviews', 'Review_Stars'])\n",
    "# hearts = people who like the product\n",
    "# stars = given with reviews to rate the product"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {
    "tags": [
     "outputPrepend"
    ]
   },
   "outputs": [
    {
     "output_type": "stream",
     "name": "stdout",
     "text": [
      "overpowering and the consistency ...      5 stars  \n",
      "1  I started using \"That blockbuster wonder cream...      4 stars  \n",
      "2  * I received this item complimentary in exchan...      3 stars  \n",
      "3  I got this cream as a sample. I usually use dr...      2 stars  \n",
      "4  The cream itself is great, very thick and does...       1 star  \n",
      "clicked\n",
      "                        Category  \\\n",
      "0  moisturizing-cream-oils-mists   \n",
      "1  moisturizing-cream-oils-mists   \n",
      "2  moisturizing-cream-oils-mists   \n",
      "3  moisturizing-cream-oils-mists   \n",
      "4  moisturizing-cream-oils-mists   \n",
      "\n",
      "                                                 URL       Brand  \\\n",
      "0  https://www.sephora.com/product/jlo-beauty-tha...  JLo Beauty   \n",
      "1  https://www.sephora.com/product/jlo-beauty-tha...  JLo Beauty   \n",
      "2  https://www.sephora.com/product/jlo-beauty-tha...  JLo Beauty   \n",
      "3  https://www.sephora.com/product/jlo-beauty-tha...  JLo Beauty   \n",
      "4  https://www.sephora.com/product/jlo-beauty-tha...  JLo Beauty   \n",
      "\n",
      "                                  Product_Name   Price Hearts Total_Stars  \\\n",
      "0  That Blockbuster Cream with Hyaluronic Acid  $58.00   5.1K     4 stars   \n",
      "1  That Blockbuster Cream with Hyaluronic Acid  $58.00   5.1K     4 stars   \n",
      "2  That Blockbuster Cream with Hyaluronic Acid  $58.00   5.1K     4 stars   \n",
      "3  That Blockbuster Cream with Hyaluronic Acid  $58.00   5.1K     4 stars   \n",
      "4  That Blockbuster Cream with Hyaluronic Acid  $58.00   5.1K     4 stars   \n",
      "\n",
      "                                             Reviews Review_Stars  \n",
      "0  Packaging: Beautiful pretty packaging; looks b...      5 stars  \n",
      "1  I received this product from Influenster and J...      4 stars  \n",
      "2  I received a complimentary product from Influe...      3 stars  \n",
      "3  I got this sample from Influenster and I can h...      2 stars  \n",
      "4  I???d give it 0 stars if I could. First, the pac...       1 star  \n",
      "clicked\n",
      "                        Category  \\\n",
      "0  moisturizing-cream-oils-mists   \n",
      "1  moisturizing-cream-oils-mists   \n",
      "2  moisturizing-cream-oils-mists   \n",
      "3  moisturizing-cream-oils-mists   \n",
      "4  moisturizing-cream-oils-mists   \n",
      "\n",
      "                                                 URL       Brand  \\\n",
      "0  https://www.sephora.com/product/jlo-beauty-tha...  JLo Beauty   \n",
      "1  https://www.sephora.com/product/jlo-beauty-tha...  JLo Beauty   \n",
      "2  https://www.sephora.com/product/jlo-beauty-tha...  JLo Beauty   \n",
      "3  https://www.sephora.com/product/jlo-beauty-tha...  JLo Beauty   \n",
      "4  https://www.sephora.com/product/jlo-beauty-tha...  JLo Beauty   \n",
      "\n",
      "                                  Product_Name   Price Hearts Total_Stars  \\\n",
      "0  That Blockbuster Cream with Hyaluronic Acid  $58.00   5.1K     4 stars   \n",
      "1  That Blockbuster Cream with Hyaluronic Acid  $58.00   5.1K     4 stars   \n",
      "2  That Blockbuster Cream with Hyaluronic Acid  $58.00   5.1K     4 stars   \n",
      "3  That Blockbuster Cream with Hyaluronic Acid  $58.00   5.1K     4 stars   \n",
      "4  That Blockbuster Cream with Hyaluronic Acid  $58.00   5.1K     4 stars   \n",
      "\n",
      "                                             Reviews Review_Stars  \n",
      "0  Wonderful i really love it. I received this sa...      5 stars  \n",
      "1  Lovely package. Great moisturizer. Recommend. ...      4 stars  \n",
      "2  I received this product FREE from Influenster ...      3 stars  \n",
      "3  I received a good size sample of this with a r...      2 stars  \n",
      "4  Actually not bad, a little goes a long way. Th...       1 star  \n",
      "clicked\n",
      "                        Category  \\\n",
      "0  moisturizing-cream-oils-mists   \n",
      "1  moisturizing-cream-oils-mists   \n",
      "2  moisturizing-cream-oils-mists   \n",
      "3  moisturizing-cream-oils-mists   \n",
      "4  moisturizing-cream-oils-mists   \n",
      "\n",
      "                                                 URL       Brand  \\\n",
      "0  https://www.sephora.com/product/jlo-beauty-tha...  JLo Beauty   \n",
      "1  https://www.sephora.com/product/jlo-beauty-tha...  JLo Beauty   \n",
      "2  https://www.sephora.com/product/jlo-beauty-tha...  JLo Beauty   \n",
      "3  https://www.sephora.com/product/jlo-beauty-tha...  JLo Beauty   \n",
      "4  https://www.sephora.com/product/jlo-beauty-tha...  JLo Beauty   \n",
      "\n",
      "                                  Product_Name   Price Hearts Total_Stars  \\\n",
      "0  That Blockbuster Cream with Hyaluronic Acid  $58.00   5.1K     4 stars   \n",
      "1  That Blockbuster Cream with Hyaluronic Acid  $58.00   5.1K     4 stars   \n",
      "2  That Blockbuster Cream with Hyaluronic Acid  $58.00   5.1K     4 stars   \n",
      "3  That Blockbuster Cream with Hyaluronic Acid  $58.00   5.1K     4 stars   \n",
      "4  That Blockbuster Cream with Hyaluronic Acid  $58.00   5.1K     4 stars   \n",
      "\n",
      "                                             Reviews Review_Stars  \n",
      "0  I like the smell on this and how moisturizing ...      5 stars  \n",
      "1  Thrilled to receive this product complimentary...      4 stars  \n",
      "2  This product smells amazing.  It feels like bu...      3 stars  \n",
      "3  I recieved this cream via Influenster. I tried...      2 stars  \n",
      "4  Not the best. Not the worst. Absorbs nicely. S...       1 star  \n",
      "clicked\n",
      "                        Category  \\\n",
      "0  moisturizing-cream-oils-mists   \n",
      "1  moisturizing-cream-oils-mists   \n",
      "2  moisturizing-cream-oils-mists   \n",
      "3  moisturizing-cream-oils-mists   \n",
      "4  moisturizing-cream-oils-mists   \n",
      "\n",
      "                                                 URL       Brand  \\\n",
      "0  https://www.sephora.com/product/jlo-beauty-tha...  JLo Beauty   \n",
      "1  https://www.sephora.com/product/jlo-beauty-tha...  JLo Beauty   \n",
      "2  https://www.sephora.com/product/jlo-beauty-tha...  JLo Beauty   \n",
      "3  https://www.sephora.com/product/jlo-beauty-tha...  JLo Beauty   \n",
      "4  https://www.sephora.com/product/jlo-beauty-tha...  JLo Beauty   \n",
      "\n",
      "                                  Product_Name   Price Hearts Total_Stars  \\\n",
      "0  That Blockbuster Cream with Hyaluronic Acid  $58.00   5.1K     4 stars   \n",
      "1  That Blockbuster Cream with Hyaluronic Acid  $58.00   5.1K     4 stars   \n",
      "2  That Blockbuster Cream with Hyaluronic Acid  $58.00   5.1K     4 stars   \n",
      "3  That Blockbuster Cream with Hyaluronic Acid  $58.00   5.1K     4 stars   \n",
      "4  That Blockbuster Cream with Hyaluronic Acid  $58.00   5.1K     4 stars   \n",
      "\n",
      "                                             Reviews Review_Stars  \n",
      "0  I???m a 52 year old woman who has very dry skin ...      5 stars  \n",
      "1  I received this complimentary from influenster...      4 stars  \n",
      "2  I got this product complimentary from Influens...      3 stars  \n",
      "3  I really like this moisturizer. It leaves my s...      2 stars  \n",
      "4  Love this cream, it is just what I was looking...       1 star  \n",
      "clicked\n",
      "                        Category  \\\n",
      "0  moisturizing-cream-oils-mists   \n",
      "1  moisturizing-cream-oils-mists   \n",
      "2  moisturizing-cream-oils-mists   \n",
      "3  moisturizing-cream-oils-mists   \n",
      "4  moisturizing-cream-oils-mists   \n",
      "\n",
      "                                                 URL       Brand  \\\n",
      "0  https://www.sephora.com/product/jlo-beauty-tha...  JLo Beauty   \n",
      "1  https://www.sephora.com/product/jlo-beauty-tha...  JLo Beauty   \n",
      "2  https://www.sephora.com/product/jlo-beauty-tha...  JLo Beauty   \n",
      "3  https://www.sephora.com/product/jlo-beauty-tha...  JLo Beauty   \n",
      "4  https://www.sephora.com/product/jlo-beauty-tha...  JLo Beauty   \n",
      "\n",
      "                                  Product_Name   Price Hearts Total_Stars  \\\n",
      "0  That Blockbuster Cream with Hyaluronic Acid  $58.00   5.1K     4 stars   \n",
      "1  That Blockbuster Cream with Hyaluronic Acid  $58.00   5.1K     4 stars   \n",
      "2  That Blockbuster Cream with Hyaluronic Acid  $58.00   5.1K     4 stars   \n",
      "3  That Blockbuster Cream with Hyaluronic Acid  $58.00   5.1K     4 stars   \n",
      "4  That Blockbuster Cream with Hyaluronic Acid  $58.00   5.1K     4 stars   \n",
      "\n",
      "                                             Reviews Review_Stars  \n",
      "0  Nothing special, of all the products in this l...      5 stars  \n",
      "1  This is so amazing it???s really a hit and left ...      4 stars  \n",
      "2  I recieved this product free from influenster ...      3 stars  \n",
      "3  I recieved this as a complimentary gift from I...      2 stars  \n",
      "4  Omg so I haven???t found my holy grail night cre...       1 star  \n",
      "clicked\n",
      "                        Category  \\\n",
      "0  moisturizing-cream-oils-mists   \n",
      "1  moisturizing-cream-oils-mists   \n",
      "2  moisturizing-cream-oils-mists   \n",
      "3  moisturizing-cream-oils-mists   \n",
      "4  moisturizing-cream-oils-mists   \n",
      "\n",
      "                                                 URL       Brand  \\\n",
      "0  https://www.sephora.com/product/jlo-beauty-tha...  JLo Beauty   \n",
      "1  https://www.sephora.com/product/jlo-beauty-tha...  JLo Beauty   \n",
      "2  https://www.sephora.com/product/jlo-beauty-tha...  JLo Beauty   \n",
      "3  https://www.sephora.com/product/jlo-beauty-tha...  JLo Beauty   \n",
      "4  https://www.sephora.com/product/jlo-beauty-tha...  JLo Beauty   \n",
      "\n",
      "                                  Product_Name   Price Hearts Total_Stars  \\\n",
      "0  That Blockbuster Cream with Hyaluronic Acid  $58.00   5.1K     4 stars   \n",
      "1  That Blockbuster Cream with Hyaluronic Acid  $58.00   5.1K     4 stars   \n",
      "2  That Blockbuster Cream with Hyaluronic Acid  $58.00   5.1K     4 stars   \n",
      "3  That Blockbuster Cream with Hyaluronic Acid  $58.00   5.1K     4 stars   \n",
      "4  That Blockbuster Cream with Hyaluronic Acid  $58.00   5.1K     4 stars   \n",
      "\n",
      "                                             Reviews Review_Stars  \n",
      "0  absorbs quickly into the skin, is non-greasy a...      5 stars  \n",
      "1  I really like this cream. A little bit goes a ...      4 stars  \n",
      "2  Love!! Like dewy skin and this product deliver...      3 stars  \n",
      "3  Received this as a sample, nice moisturizer fo...      2 stars  \n",
      "4  Pros: fragrance, hydrating \\nCons: packaging i...       1 star  \n",
      "clicked\n",
      "                        Category  \\\n",
      "0  moisturizing-cream-oils-mists   \n",
      "1  moisturizing-cream-oils-mists   \n",
      "2  moisturizing-cream-oils-mists   \n",
      "3  moisturizing-cream-oils-mists   \n",
      "4  moisturizing-cream-oils-mists   \n",
      "\n",
      "                                                 URL       Brand  \\\n",
      "0  https://www.sephora.com/product/jlo-beauty-tha...  JLo Beauty   \n",
      "1  https://www.sephora.com/product/jlo-beauty-tha...  JLo Beauty   \n",
      "2  https://www.sephora.com/product/jlo-beauty-tha...  JLo Beauty   \n",
      "3  https://www.sephora.com/product/jlo-beauty-tha...  JLo Beauty   \n",
      "4  https://www.sephora.com/product/jlo-beauty-tha...  JLo Beauty   \n",
      "\n",
      "                                  Product_Name   Price Hearts Total_Stars  \\\n",
      "0  That Blockbuster Cream with Hyaluronic Acid  $58.00   5.1K     4 stars   \n",
      "1  That Blockbuster Cream with Hyaluronic Acid  $58.00   5.1K     4 stars   \n",
      "2  That Blockbuster Cream with Hyaluronic Acid  $58.00   5.1K     4 stars   \n",
      "3  That Blockbuster Cream with Hyaluronic Acid  $58.00   5.1K     4 stars   \n",
      "4  That Blockbuster Cream with Hyaluronic Acid  $58.00   5.1K     4 stars   \n",
      "\n",
      "                                             Reviews Review_Stars  \n",
      "0  Makes your skin feel really soft however the f...      5 stars  \n",
      "1  I received this product free for testing purpo...      4 stars  \n",
      "2  This cream definitely applies heavy and greasy...      3 stars  \n",
      "3  I received this product free in exchange for a...      2 stars  \n",
      "4  I received the product complimentary for my ho...       1 star  \n",
      "clicked\n",
      "                        Category  \\\n",
      "0  moisturizing-cream-oils-mists   \n",
      "1  moisturizing-cream-oils-mists   \n",
      "2  moisturizing-cream-oils-mists   \n",
      "3  moisturizing-cream-oils-mists   \n",
      "4  moisturizing-cream-oils-mists   \n",
      "\n",
      "                                                 URL       Brand  \\\n",
      "0  https://www.sephora.com/product/jlo-beauty-tha...  JLo Beauty   \n",
      "1  https://www.sephora.com/product/jlo-beauty-tha...  JLo Beauty   \n",
      "2  https://www.sephora.com/product/jlo-beauty-tha...  JLo Beauty   \n",
      "3  https://www.sephora.com/product/jlo-beauty-tha...  JLo Beauty   \n",
      "4  https://www.sephora.com/product/jlo-beauty-tha...  JLo Beauty   \n",
      "\n",
      "                                  Product_Name   Price Hearts Total_Stars  \\\n",
      "0  That Blockbuster Cream with Hyaluronic Acid  $58.00   5.1K     4 stars   \n",
      "1  That Blockbuster Cream with Hyaluronic Acid  $58.00   5.1K     4 stars   \n",
      "2  That Blockbuster Cream with Hyaluronic Acid  $58.00   5.1K     4 stars   \n",
      "3  That Blockbuster Cream with Hyaluronic Acid  $58.00   5.1K     4 stars   \n",
      "4  That Blockbuster Cream with Hyaluronic Acid  $58.00   5.1K     4 stars   \n",
      "\n",
      "                                             Reviews Review_Stars  \n",
      "0  I received this from influenster for free for ...      5 stars  \n",
      "1  LOVE this cream! When I received this product ...      4 stars  \n",
      "2  I did not love the smell of it, kind of like w...      3 stars  \n",
      "3  I received this product to review. Over all it...      2 stars  \n",
      "4  I received this complementary product to revie...       1 star  \n",
      "clicked\n",
      "                        Category  \\\n",
      "0  moisturizing-cream-oils-mists   \n",
      "1  moisturizing-cream-oils-mists   \n",
      "2  moisturizing-cream-oils-mists   \n",
      "3  moisturizing-cream-oils-mists   \n",
      "4  moisturizing-cream-oils-mists   \n",
      "\n",
      "                                                 URL       Brand  \\\n",
      "0  https://www.sephora.com/product/jlo-beauty-tha...  JLo Beauty   \n",
      "1  https://www.sephora.com/product/jlo-beauty-tha...  JLo Beauty   \n",
      "2  https://www.sephora.com/product/jlo-beauty-tha...  JLo Beauty   \n",
      "3  https://www.sephora.com/product/jlo-beauty-tha...  JLo Beauty   \n",
      "4  https://www.sephora.com/product/jlo-beauty-tha...  JLo Beauty   \n",
      "\n",
      "                                  Product_Name   Price Hearts Total_Stars  \\\n",
      "0  That Blockbuster Cream with Hyaluronic Acid  $58.00   5.1K     4 stars   \n",
      "1  That Blockbuster Cream with Hyaluronic Acid  $58.00   5.1K     4 stars   \n",
      "2  That Blockbuster Cream with Hyaluronic Acid  $58.00   5.1K     4 stars   \n",
      "3  That Blockbuster Cream with Hyaluronic Acid  $58.00   5.1K     4 stars   \n",
      "4  That Blockbuster Cream with Hyaluronic Acid  $58.00   5.1K     4 stars   \n",
      "\n",
      "                                             Reviews Review_Stars  \n",
      "0  Jlo baby!!! Thanks for giving us a piece of yo...      5 stars  \n",
      "1  So wI wanted to take some time to really try t...      4 stars  \n",
      "2  I received the product free for testing purpos...      3 stars  \n",
      "3  If you have oily skin this cream is not good f...      2 stars  \n",
      "4  It is not bad. It leave the face Glowy and hyd...       1 star  \n",
      "clicked\n",
      "                        Category  \\\n",
      "0  moisturizing-cream-oils-mists   \n",
      "1  moisturizing-cream-oils-mists   \n",
      "2  moisturizing-cream-oils-mists   \n",
      "3  moisturizing-cream-oils-mists   \n",
      "4  moisturizing-cream-oils-mists   \n",
      "\n",
      "                                                 URL       Brand  \\\n",
      "0  https://www.sephora.com/product/jlo-beauty-tha...  JLo Beauty   \n",
      "1  https://www.sephora.com/product/jlo-beauty-tha...  JLo Beauty   \n",
      "2  https://www.sephora.com/product/jlo-beauty-tha...  JLo Beauty   \n",
      "3  https://www.sephora.com/product/jlo-beauty-tha...  JLo Beauty   \n",
      "4  https://www.sephora.com/product/jlo-beauty-tha...  JLo Beauty   \n",
      "\n",
      "                                  Product_Name   Price Hearts Total_Stars  \\\n",
      "0  That Blockbuster Cream with Hyaluronic Acid  $58.00   5.1K     4 stars   \n",
      "1  That Blockbuster Cream with Hyaluronic Acid  $58.00   5.1K     4 stars   \n",
      "2  That Blockbuster Cream with Hyaluronic Acid  $58.00   5.1K     4 stars   \n",
      "3  That Blockbuster Cream with Hyaluronic Acid  $58.00   5.1K     4 stars   \n",
      "4  That Blockbuster Cream with Hyaluronic Acid  $58.00   5.1K     4 stars   \n",
      "\n",
      "                                             Reviews Review_Stars  \n",
      "0  I received this product to test for free.This ...      5 stars  \n",
      "1  I received this product for free from Influens...      4 stars  \n",
      "2  I received this product complimentary from inf...      3 stars  \n",
      "3  I received this item complimentary from Influe...      2 stars  \n",
      "4  I got this item free from influencer and Jlo i...       1 star  \n",
      "clicked\n",
      "                        Category  \\\n",
      "0  moisturizing-cream-oils-mists   \n",
      "1  moisturizing-cream-oils-mists   \n",
      "2  moisturizing-cream-oils-mists   \n",
      "3  moisturizing-cream-oils-mists   \n",
      "4  moisturizing-cream-oils-mists   \n",
      "\n",
      "                                                 URL       Brand  \\\n",
      "0  https://www.sephora.com/product/jlo-beauty-tha...  JLo Beauty   \n",
      "1  https://www.sephora.com/product/jlo-beauty-tha...  JLo Beauty   \n",
      "2  https://www.sephora.com/product/jlo-beauty-tha...  JLo Beauty   \n",
      "3  https://www.sephora.com/product/jlo-beauty-tha...  JLo Beauty   \n",
      "4  https://www.sephora.com/product/jlo-beauty-tha...  JLo Beauty   \n",
      "\n",
      "                                  Product_Name   Price Hearts Total_Stars  \\\n",
      "0  That Blockbuster Cream with Hyaluronic Acid  $58.00   5.1K     4 stars   \n",
      "1  That Blockbuster Cream with Hyaluronic Acid  $58.00   5.1K     4 stars   \n",
      "2  That Blockbuster Cream with Hyaluronic Acid  $58.00   5.1K     4 stars   \n",
      "3  That Blockbuster Cream with Hyaluronic Acid  $58.00   5.1K     4 stars   \n",
      "4  That Blockbuster Cream with Hyaluronic Acid  $58.00   5.1K     4 stars   \n",
      "\n",
      "                                             Reviews Review_Stars  \n",
      "0  I recieved this complementary from influenster...      5 stars  \n",
      "1  The moisturizer is creamy, but doesn't feel oi...      4 stars  \n",
      "2  Lets get loud!! This product is amazing, as th...      3 stars  \n",
      "3  Adoring this moisturizer already! I have only ...      2 stars  \n",
      "4  I received this product for free to review. \\n...       1 star  \n",
      "clicked\n",
      "                        Category  \\\n",
      "0  moisturizing-cream-oils-mists   \n",
      "1  moisturizing-cream-oils-mists   \n",
      "2  moisturizing-cream-oils-mists   \n",
      "3  moisturizing-cream-oils-mists   \n",
      "4  moisturizing-cream-oils-mists   \n",
      "\n",
      "                                                 URL       Brand  \\\n",
      "0  https://www.sephora.com/product/jlo-beauty-tha...  JLo Beauty   \n",
      "1  https://www.sephora.com/product/jlo-beauty-tha...  JLo Beauty   \n",
      "2  https://www.sephora.com/product/jlo-beauty-tha...  JLo Beauty   \n",
      "3  https://www.sephora.com/product/jlo-beauty-tha...  JLo Beauty   \n",
      "4  https://www.sephora.com/product/jlo-beauty-tha...  JLo Beauty   \n",
      "\n",
      "                                  Product_Name   Price Hearts Total_Stars  \\\n",
      "0  That Blockbuster Cream with Hyaluronic Acid  $58.00   5.1K     4 stars   \n",
      "1  That Blockbuster Cream with Hyaluronic Acid  $58.00   5.1K     4 stars   \n",
      "2  That Blockbuster Cream with Hyaluronic Acid  $58.00   5.1K     4 stars   \n",
      "3  That Blockbuster Cream with Hyaluronic Acid  $58.00   5.1K     4 stars   \n",
      "4  That Blockbuster Cream with Hyaluronic Acid  $58.00   5.1K     4 stars   \n",
      "\n",
      "                                             Reviews Review_Stars  \n",
      "0  I received this from Influenster. Really nice ...      5 stars  \n",
      "1  Wow! What a moisturizer! The first time I touc...      4 stars  \n",
      "2  the product is thick and the formula works ver...      3 stars  \n",
      "3  Received this as a complimentary gift from Inf...      2 stars  \n",
      "4  JLo comes through with this Wonder Cream. The ...       1 star  \n",
      "clicked\n",
      "                        Category  \\\n",
      "0  moisturizing-cream-oils-mists   \n",
      "1  moisturizing-cream-oils-mists   \n",
      "2  moisturizing-cream-oils-mists   \n",
      "3  moisturizing-cream-oils-mists   \n",
      "4  moisturizing-cream-oils-mists   \n",
      "\n",
      "                                                 URL       Brand  \\\n",
      "0  https://www.sephora.com/product/jlo-beauty-tha...  JLo Beauty   \n",
      "1  https://www.sephora.com/product/jlo-beauty-tha...  JLo Beauty   \n",
      "2  https://www.sephora.com/product/jlo-beauty-tha...  JLo Beauty   \n",
      "3  https://www.sephora.com/product/jlo-beauty-tha...  JLo Beauty   \n",
      "4  https://www.sephora.com/product/jlo-beauty-tha...  JLo Beauty   \n",
      "\n",
      "                                  Product_Name   Price Hearts Total_Stars  \\\n",
      "0  That Blockbuster Cream with Hyaluronic Acid  $58.00   5.1K     4 stars   \n",
      "1  That Blockbuster Cream with Hyaluronic Acid  $58.00   5.1K     4 stars   \n",
      "2  That Blockbuster Cream with Hyaluronic Acid  $58.00   5.1K     4 stars   \n",
      "3  That Blockbuster Cream with Hyaluronic Acid  $58.00   5.1K     4 stars   \n",
      "4  That Blockbuster Cream with Hyaluronic Acid  $58.00   5.1K     4 stars   \n",
      "\n",
      "                                             Reviews Review_Stars  \n",
      "0  I received a free sample from Influenster and ...      5 stars  \n",
      "1  I received this product for free from Influens...      4 stars  \n",
      "2  phenomenal cream. I love how it makes my skin ...      3 stars  \n",
      "3  I received this product for free for reviewing...      2 stars  \n",
      "4  Love this cream. Was concerned with level of g...       1 star  \n",
      "https://www.sephora.com/product/the-essence-plumping-skin-softener-P415771?skuId=1890904&icid2=skugrid:p415771\n"
     ]
    },
    {
     "output_type": "error",
     "ename": "AttributeError",
     "evalue": "'NoneType' object has no attribute 'getText'",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mAttributeError\u001b[0m                            Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-26-a1ff4b746924>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m     27\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     28\u001b[0m         \u001b[1;31m# get other info that doesnt req pagination\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 29\u001b[1;33m         \u001b[0mbrand\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0msoup\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mfind\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"a\"\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mclass_\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;34m\"css-nc375s e65zztl0\"\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mgetText\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     30\u001b[0m         \u001b[0mproduct_name\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0msoup\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mfind\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"span\"\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mclass_\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;34m\"css-1pgnl76\"\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mgetText\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     31\u001b[0m         \u001b[0mprice\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0msoup\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mfind\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"b\"\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mclass_\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;34m\"css-0\"\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mgetText\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mAttributeError\u001b[0m: 'NoneType' object has no attribute 'getText'"
     ]
    }
   ],
   "source": [
    "with open(r'C:\\\\Users\\\\nicol\\\\OneDrive\\\\Desktop\\\\Datum Proj\\\\product_urls.csv', 'r') as csv_file:\n",
    "    csv_reader = csv.reader(csv_file)\n",
    "    next(csv_reader)\n",
    "    for row in csv_reader:  # iterable reader object gives rows as list\n",
    "        try:\n",
    "            print(row[1])\n",
    "            driver.get(row[1])\n",
    "            WebDriverWait(driver, 30)\n",
    "            r = requests.get(row[1])\n",
    "            soup = BeautifulSoup(r.content)\n",
    "        except NoSuchElementException:\n",
    "            break\n",
    "\n",
    "        # check for country code pop up & dismiss\n",
    "        try:\n",
    "            driver.find_element_by_xpath('/html/body/div[3]/div/div/div[2]/div/div/button').click()\n",
    "            WebDriverWait(driver, 20)\n",
    "        except:\n",
    "            pass\n",
    "\n",
    "        # check for sign in pop up\n",
    "        try:\n",
    "            driver.find_element_by_xpath('//*[@id=\"modal1Dialog\"]/button').click()\n",
    "            WebDriverWait(driver, 20)\n",
    "        except NoSuchElementException:\n",
    "            pass\n",
    "\n",
    "        # get other info that doesnt req pagination\n",
    "        brand = soup.find(\"a\", class_=\"css-nc375s e65zztl0\").getText()\n",
    "        product_name = soup.find(\"span\", class_=\"css-1pgnl76\").getText()\n",
    "        price = soup.find(\"b\", class_=\"css-0\").getText()\n",
    "        hearts = soup.find(\"span\", class_=\"css-jk94q9\").getText()\n",
    "        tot_stars = soup.find(\"div\", class_=\"css-jp4jy6\")[\"aria-label\"]\n",
    "        print(f\"Data: {product_name}, {brand}, {price}, {hearts}, {tot_stars}\")\n",
    "\n",
    "        # review pagination\n",
    "        rev_count = 0\n",
    "        while True:\n",
    "            #close any pop ups\n",
    "            # check for country code pop up & dismiss\n",
    "            try:\n",
    "                driver.find_element_by_xpath('/html/body/div[3]/div/div/div[2]/div/div/button').click()\n",
    "                WebDriverWait(driver, 20)\n",
    "            except:\n",
    "                pass\n",
    "\n",
    "            # check for sign in pop up\n",
    "            try:\n",
    "                driver.find_element_by_xpath('//*[@id=\"modal1Dialog\"]/button').click()\n",
    "                WebDriverWait(driver, 20)\n",
    "            except NoSuchElementException:\n",
    "                pass\n",
    "\n",
    "            #find and scroll down to bottom of page\n",
    "            total_height = int(driver.execute_script(\"return document.body.scrollHeight\"))\n",
    "            for i in range(1, total_height, 20):\n",
    "                driver.execute_script(\"window.scrollTo(0, {});\".format(i)) \n",
    "                WebDriverWait(driver,20)\n",
    "\n",
    "            find_reviews = driver.find_elements_by_class_name(\"css-1x44x6f\")\n",
    "            review_stars = driver.find_elements_by_class_name(\"css-4qxrld\")\n",
    "            #print(f\"Reviews: {find_reviews}\")\n",
    "            #print(f\"Stars: {review_stars}\")\n",
    "\n",
    "            # organize collected reviews in temporary df and push to main df\n",
    "            organized = []\n",
    "            for ind, review in enumerate(find_reviews):\n",
    "                organize_data = {}\n",
    "                organize_data['Category'] = row[0]\n",
    "                organize_data['URL'] = row[1]\n",
    "                organize_data['Brand'] = brand\n",
    "                organize_data['Product_Name'] = product_name\n",
    "                organize_data['Price'] = price\n",
    "                organize_data['Hearts'] = hearts\n",
    "                organize_data['Total_Stars'] = tot_stars\n",
    "                organize_data['Reviews'] = review.text\n",
    "                organize_data['Review_Stars'] = review_stars[ind].get_attribute('aria-label') #Incorrect\n",
    "                organized.append(organize_data)\n",
    "\n",
    "            df = pd.DataFrame(organized)\n",
    "            print(df.head())  # testing\n",
    "            product_data_df = pd.concat([product_data_df, df], axis=0, ignore_index=True)\n",
    "\n",
    "            if rev_count == 50:#number of pages per product you wish to scrape\n",
    "                break\n",
    "            # paginate\n",
    "            try:  # click next page\n",
    "                next_page = driver.find_element_by_class_name('css-2anst8')\n",
    "                next_page.click()\n",
    "                print(\"clicked\")\n",
    "                rev_count +=1\n",
    "                WebDriverWait(driver, 30)\n",
    "\n",
    "            except ElementNotInteractableException:\n",
    "                try:  # check for sign in pop up\n",
    "                    driver.find_element_by_xpath('//*[@id=\"modal1Dialog\"]/button').click()\n",
    "                    WebDriverWait(driver, 10)\n",
    "                except NoSuchElementException:\n",
    "                    pass\n",
    "            except NoSuchElementException:  # no next page\n",
    "                break\n",
    "driver.close()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "product_data_df\n",
    "product_data_df.to_csv(r'C:\\Users\\nicol\\OneDrive\\Desktop\\Datum Proj\\product_data_sephora.csv', index = False)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ]
}