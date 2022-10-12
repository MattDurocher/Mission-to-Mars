#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager


# In[2]:


# Set up Splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[3]:


# Visit the mars nasa news site
url = 'https://redplanetscience.com'
browser.visit(url)


# In[4]:


# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)


# In[5]:


html = browser.html
news_soup = soup(html, 'html.parser')


# In[6]:


slide_elm = news_soup.select_one('div.list_text')


# In[7]:


slide_elm.find('div', class_='content_title')


# In[8]:


# Use the parent element to find the first a tag and save it as 'news_title'
news_title = slide_elm.find('div', class_='content_title').get_text()
news_title


# In[9]:


# Use the parent element to find the paragraph text
news_p = slide_elm.find('div', class_='article_teaser_body').get_text()
news_p


# # ## JPL Sapce Images Featured Images

# In[10]:


# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)


# In[11]:


# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# In[12]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')


# In[13]:


# Find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# In[14]:


# Use the base URL to create an absolute URL
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# # ## Mars Facts

# In[15]:


df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.head()


# In[16]:


df.columns=['Description', 'Mars', 'Earth']
df.set_index('Description', inplace=True)
df


# In[17]:


df.to_html()


# In[18]:


browser.quit()

