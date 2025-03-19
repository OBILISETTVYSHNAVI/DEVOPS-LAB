from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
import time

class RegistrationTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get("http://192.168.24.101:5000")  # Update the path to your local file
        time.sleep(2)  # Wait for the page to load
    
    def fill_form(self, fullName, username, email, phoneNumber, password, confirmPassword, gender):
        driver = self.driver
        driver.find_element(By.ID, "fullName").clear()
        driver.find_element(By.ID, "fullName").send_keys(fullName)
        driver.find_element(By.ID, "username").clear()
        driver.find_element(By.ID, "username").send_keys(username)
        driver.find_element(By.ID, "email").clear()
        driver.find_element(By.ID, "email").send_keys(email)
        driver.find_element(By.ID, "phoneNumber").clear()
        driver.find_element(By.ID, "phoneNumber").send_keys(phoneNumber)
        driver.find_element(By.ID, "password").clear()
        driver.find_element(By.ID, "password").send_keys(password)
        driver.find_element(By.ID, "confirmPassword").clear()
        driver.find_element(By.ID, "confirmPassword").send_keys(confirmPassword)
        
        if gender:
            driver.find_element(By.XPATH, f"//input[@name='gender'][@value='{gender}']").click()
        
        driver.find_element(By.XPATH, "//button[text()='Register']").click()
        time.sleep(2)
    
    def test_empty_fields(self):
        self.fill_form("", "", "", "", "", "", "")
        error_elements = self.driver.find_elements(By.CLASS_NAME, "error")
        self.assertTrue(any(e.text for e in error_elements), "Error messages should be displayed")
    
    def test_invalid_email(self):
        self.fill_form("John Doe", "johndoe123", "invalid-email", "1234567890", "SecurePass123", "SecurePass123", "male")
        error_text = self.driver.find_element(By.ID, "emailError").text
        self.assertIn("valid email", error_text, "Invalid email should trigger an error")
    
    def test_mismatched_passwords(self):
        self.fill_form("John Doe", "johndoe123", "johndoe@example.com", "1234567890", "SecurePass123", "WrongPass", "male")
        error_text = self.driver.find_element(By.ID, "confirmPasswordError").text
        self.assertIn("Passwords do not match", error_text, "Mismatch passwords should trigger an error")
    
    def test_short_password(self):
        self.fill_form("John Doe", "johndoe123", "johndoe@example.com", "1234567890", "123", "123", "male")
        error_text = self.driver.find_element(By.ID, "passwordError").text
        self.assertIn("Password too short", error_text, "Short password should trigger an error")
    
    def test_invalid_phone_number(self):
        self.fill_form("John Doe", "johndoe123", "johndoe@example.com", "abcd1234", "SecurePass123", "SecurePass123", "male")
        error_text = self.driver.find_element(By.ID, "phoneError").text
        self.assertIn("valid phone number", error_text, "Invalid phone number should trigger an error")
    
    def test_successful_registration(self):
        self.fill_form("John Doe", "admin", "admin@example.com", "1234567890", "SecurePass123", "SecurePass123", "male")
        
        # Wait for the success message to appear
        success_message = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "successMessage"))
        ).text
        
        self.assertIn("Registration successful", success_message, "Success message should appear after registration")
        print("Test Passed: Success message displayed correctly!")
    
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()
