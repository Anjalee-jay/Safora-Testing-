# QUICKSTART GUIDE - Safora Selenium Tests

## 1️⃣ First Time Setup

```bash
# Navigate to project folder
cd c:\Users\SKYLINE\Desktop\Safora

# Install dependencies
pip install -r requirements.txt
```

## 2️⃣ Run Individual Tests

### Test Homepage
```bash
python test_safora.py
```
✓ Validates the English homepage loads correctly

### Test Contact Form
```bash
python test_contact_form.py
```
✓ Tests form validation, filling, and submission

## 3️⃣ Run All Tests at Once

```bash
python run_all_tests.py
```
Runs all tests in sequence and generates a summary report

## 🎯 What Gets Tested

| Test | URL | Purpose |
|------|-----|---------|
| Homepage | https://safora.se/en/ | Verify page loads, title, and content |
| Contact Form | https://safora.se/en/contact.html | Validate form fields, submission, success |

## 📋 Test Features

- **Automatic Driver Management**: No need to manually download ChromeDriver
- **Headless Mode**: Tests run without opening browser window (customizable)
- **Error Handling**: Comprehensive error messages and validation
- **Field Detection**: Auto-detects form fields using multiple selector patterns
- **Submission Verification**: Checks for success messages and redirects

## ⚙️ Configuration

### Change Browser Visibility
Edit `test_contact_form.py`, line ~120:
```python
automation = ContactFormAutomation(headless=True)   # False to see browser
```

### Modify Test Data
Edit the `fill_contact_form()` call in `main()` function:
```python
automation.fill_contact_form(
    name="Your Name",
    email="your@email.com",
    phone="+46XXXXXXXXX",
    message="Your test message"
)
```

## 🆘 Troubleshooting

| Issue | Solution |
|-------|----------|
| ModuleNotFoundError | Run `pip install -r requirements.txt` |
| Chrome not found | webdriver-manager will auto-download |
| Form fields not detected | Run with `headless=False` to see the page |
| Network errors | Check internet connection and Safora status |
| Timeout errors | Website may be slow; increase timeout in code |

## 📁 File Structure

```
Safora/
├── test_safora.py              # Homepage test
├── test_contact_form.py        # Contact form test  
├── run_all_tests.py            # Test suite runner
├── requirements.txt            # Python dependencies
├── README.md                   # Full documentation
├── QUICKSTART.md              # This file
└── .gitignore                 # Git ignore rules
```

## 🚀 Next Steps

1. Run individual tests to verify setup: `python test_safora.py`
2. Test the contact form: `python test_contact_form.py`
3. Run entire suite: `python run_all_tests.py`
4. Customize tests for your needs
5. Integrate into CI/CD pipeline

## 📚 Learn More

- [Selenium Documentation](https://www.selenium.dev/documentation/)
- [WebDriver Manager](https://github.com/SergeyPirogov/webdriver_manager)
- [Safora Website](https://safora.se/en/)

---

**Ready?** Start with: `python test_safora.py`
