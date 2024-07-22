# Specify the path to the ChromeDriver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Specify the path to the ChromeDriver executable
service = Service('/Users/tejas/Downloads/chromedriver-mac-arm64 2/chromedriver')
# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("start-maximized")
# Initialize the WebDriver with the Service object and Chrome options
driver = webdriver.Chrome(service=service, options=chrome_options)
# Open the desired webpage
driver.get("https://leetcode.com/u/Contagious/")
wait = WebDriverWait(driver, 10)  # 10 seconds timeout


def waitForBasicStuff():
        # Wait until the specified element is present
        submission_number = wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(@class, 'lc-md:text-xl') and contains(@class, 'mr-[5px]') and contains(@class, 'text-base') and contains(@class, 'font-medium')]")))
        # Optionally, print the text of the found element
        print("Element found:", submission_number.text)
        print("Page is ready to parse")
        
        submissions = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(@class, 'h-[56px]') and @href='/submissions/detail/1328949641/']")))
        print("Element found and clickable:", submissions.text)

         # Find the first child element within the parent element
        first_child = submissions.find_element(By.XPATH, "./*")

        # Wait until the first child element is clickable
        wait.until(EC.element_to_be_clickable(first_child))
        
        return first_child

#main method
def main():
    try:
        latest_submission = waitForBasicStuff()
        
        # Click the first child element
        latest_submission.click()
        
        # Get the current window handle
        original_window = driver.current_window_handle

        # Wait for the new window or tab
        wait.until(EC.new_window_is_opened(driver.window_handles))

        # Get the list of all window handles
        windows = driver.window_handles

        # Switch to the new window
        for window in windows:
            if window != original_window:
                driver.switch_to.window(window)
                break

        # Perform actions on the new window
        print("New window title:", driver.title)
        
        
    
    except Exception as e:
        print("An error occurred:", e)

    finally:
        # Close the WebDriver
        time.sleep(20)
        driver.quit()


if __name__ == '__main__':
    main()
