from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time

# Initialize WebDriver
driver_path = './38872194-aa96-44c7-901b-e5316bee674f'  # Replace with the actual path to your driver
driver = webdriver.Chrome(executable_path=driver_path)

# Open the webpage
url = "https://bubt.edu.bd/global_file/validityCheck.php"
driver.get(url)

def get_student_data(student_id):
    try:
        # Select the "Student" option
        student_option = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@value='student']"))
        )
        student_option.click()

        # Enter the student ID
        id_input = driver.find_element(By.ID, "id_no")  # Adjust if the ID is different
        id_input.clear()
        id_input.send_keys(student_id)

        # Submit the form
        submit_button = driver.find_element(By.XPATH, "//input[@type='submit']")
        submit_button.click()

        # Wait for the response to load
        time.sleep(2)  # Adjust with WebDriverWait for better performance

        # Parse the response using BeautifulSoup
        page_source = driver.page_source
        soup = BeautifulSoup(page_source, 'html.parser')

        # Extract relevant data (adjust based on actual HTML structure)
        # Example of finding data (replace 'class_or_id' with actual values)
        name = soup.find("td", {"id": "studentName"})  # Replace with actual ID or class name
        program = soup.find("td", {"id": "programName"})

        # Store data in a dictionary for easy use
        student_data = {
            "name": name.text if name else "N/A",
            "program": program.text if program else "N/A"
        }

        return student_data

    except Exception as e:
        print("Error:", e)
        return None

# Example of usage
student_ids = ["22234103001", "22234103400"]  # Replace with actual student IDs
for student_id in student_ids:
    data = get_student_data(student_id)
    if data:
        print(f"Data for Student ID {student_id}: {data}")
    driver.back()  # Go back to the form page to enter a new ID

# Close the driver
driver.quit()
