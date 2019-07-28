import requests
from selenium import webdriver
import tldextract

import unittest

class BrokenLinks(unittest.TestCase):

    def setUp(self):
        self.top_page = 'http://localhost:1313'
        self.checked = set()
        self.broken_links = set()
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def get_all_links(self, page):
        self.browser.get(page)
        return self.browser.find_elements_by_css_selector("a")

    def is_web_href(self, href):
        return \
            href is not None and \
            not href == "" and \
            not href.startswith('mailto:') and \
            not href.startswith('resource:')

    def is_local_link(self, link_element):
        href = link_element.get_attribute('href')
        if not self.is_web_href(href):
            return False
        split_page = tldextract.extract(self.top_page)
        split_href = tldextract.extract(href)
        return split_page.domain == split_href.domain and \
               split_page.suffix == split_href.suffix

    def verify_link_element(self, link_element, page):
        href = link_element.get_attribute('href')
        if self.is_web_href(href) and href not in self.checked:
            r = requests.head(href)
            if r.status_code < 200 or 400 <= r.status_code:
                self.broken_links.add((page, href, r.status_code))
            print(f'  {href} -> {r.status_code}')
            self.checked.add(href)

    def test_has_no_broken_hyperlinks(self):
        page_stack = [self.top_page]
        visited = set()
        while page_stack:
            page = page_stack.pop()
            if page in visited:
                continue
            print(f'visiting {page}')
            visited.add(page)
            links = self.get_all_links(page)
            for link in links:
                self.verify_link_element(link, page)
            local_links = [x for x in links if self.is_local_link(x)]
            for link in local_links:
                page_stack.append(link.get_attribute('href'))
        print()
        print('broken links:')
        for link_info in self.broken_links:
            print(f'  {link_info}')
        self.assertEqual(len(self.broken_links), 0)

    #def test_has_no_broken_images(self):
    #    self.fail("unimplemented")

if __name__ == '__main__':
    unittest.main(warnings='ignore')

#options = webdriver.ChromeOptions() 
#options.add_argument("start-maximized")
#options.add_argument('disable-infobars')
#driver=webdriver.Chrome(chrome_options=options, executable_path=r'C:\Utility\BrowserDrivers\chromedriver.exe')
#driver.get('https://google.co.in/')
#links = driver.find_elements_by_css_selector("a")
#for link in links:
#    r = requests.head(link.get_attribute('href'))
#    print(link.get_attribute('href'), r.status_code)
