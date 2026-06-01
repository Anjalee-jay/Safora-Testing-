# Safora Selenium Automation Tests

This workspace contains automated UI tests for the Safora website using Selenium WebDriver.

## Setup Instructions

### Prerequisites
- Python 3.8+
- Google Chrome browser

### Installation

1. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

   This installs:
   - `selenium>=4.0.0` - Web automation framework
   - `webdriver-manager>=4.0.0` - Automatic driver management

### Project Structure

```
Safora/
├── requirements.txt              # Python dependencies
├── test_safora.py               # Basic homepage test
├── test_contact_form.py         # Contact form automation test
└── README.md                    # This file
```

## Test Scripts

### 1. test_safora.py - Homepage Test
**Purpose**: Verify that the Safora English homepage loads successfully

**What it tests**:
- Page loads without errors
- Page title contains "Safora"
- URL contains "/en" (English version)
- Page source is loaded (checks length)

**How to run**:
```bash
python test_safora.py
```

**Output**:
```
Title: Safora - Industrial Safety Management System & Platform
Safora EN homepage loaded successfully.
Page length: XXXX
```

---

### 2. test_contact_form.py - Contact Form Automation
**Purpose**: Automate and test the Safora contact form with validation and submission

**What it tests**:
1. **Empty Form Validation** - Attempts to submit empty form to check for validation errors
2. **Form Field Detection** - Identifies all available form fields
3. **Form Filling** - Populates form with test data:
   - Name: Anjalee Jay
   - Email: anjaleejay@gmail.com
   - Phone: +94718888886
   - Message: Test message
4. **Form Submission** - Submits the completed form
5. **Success Verification** - Checks for success messages or redirects

**How to run**:
```bash
python test_contact_form.py
```

**Output Example**:
```
--- Page Information ---
Page Title: Get in Touch With Us - Safora
Current URL: https://safora.se/en/contact.html

Found 4 form fields:
  1. <input> name='name' id='name' placeholder='Full Name' required=True
  2. <input> name='email' id='email' placeholder='Email' required=True
  3. <textarea> name='message' id='message' placeholder='Message' required=True
  4. <input> name='phone' id='phone' placeholder='Phone' required=False

--- Filling Contact Form ---
Name field filled: Jane Smith
Email field filled: jane.smith@test.com
Phone field filled: +46701234567
Message field filled: Testing the Safora contact form automation...

--- Submitting Form ---
✓ Submit button clicked

--- Verifying Submission ---
✓ Success message detected on page

==================================================
Test Result: PASSED
==================================================
```

## Configuration

### Running in Headless Mode
To run tests without displaying the browser window, edit the test script and change:
```python
automation = ContactFormAutomation(headless=True)  # True for headless, False to see browser
```

### Modifying Test Data
To change the form data used in tests, modify the `fill_contact_form()` call:
```python
automation.fill_contact_form(
    name="Your Name",
    email="your.email@example.com",
    phone="+46701234567",
    message="Your test message"
)
```

## Troubleshooting

### WebDriver Issues
The `webdriver-manager` package automatically handles ChromeDriver installation and updates.

### Form Element Not Found
The script uses multiple selector patterns to locate form fields. If fields aren't found:
1. Run with `headless=False` to see the page
2. Check browser console for errors
3. Inspect the page HTML to find the correct field selectors

### Connection Errors
- Ensure you have internet connectivity
- The website may be temporarily unavailable
- Check Safora status at https://safora.se/

## Requirements

See `requirements.txt` for full list of dependencies:
```
selenium>=4.0.0
webdriver-manager>=4.0.0
```

## Notes

- Tests use headless mode by default for CI/CD compatibility
- WebDriver automatically manages Chrome driver version compatibility
- Tests include waits for element visibility to handle dynamic content
- All tests include comprehensive error handling and reporting
