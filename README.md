# BMI Calculator

A simple **Body Mass Index (BMI) Calculator** built using **Flask** with a database connection for storing user information like Name and Surname. This project allows users to calculate their BMI and categorize it based on their height, weight, and other parameters.

## Features
- User input for Name, Surname, Age, Gender, Height, and Weight.
- Calculates and displays BMI.
- Categorizes BMI result (Underweight, Normal weight, Overweight, Obesity).
- Stores user data in a connected SQLAlchemy database.

## Tech Stack
- **Backend**: Python, Flask
- **Frontend**: HTML, CSS, Font Awesome for icons
- **Database**: SQLite (or can be configured with PostgreSQL for deployment)
- **Deployment**: Render / Heroku / PythonAnywhere (choose based on preference)

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/z4code/bmi-calculator.git
   cd bmi-calculator
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment:**

   On macOS/Linux:
   ```bash
   source venv/bin/activate
   ```

   On Windows:
   ```bash
   venv\Scripts\activate
   ```

4. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

5. **Run the application:**
   ```bash
   flask run
   ```

   The app will run at `http://127.0.0.1:5000/`.

## Project Structure

```
bmi-calculator/
│
├── app.py                  # Main Flask application
├── static/
│   └── style.css           # CSS for the app
├── templates/
│   └── index.html          # HTML template for BMI form
├── requirements.txt        # Python dependencies
├── Procfile                # For deployment on Heroku or Render
└── README.md               # Project documentation
```

## Usage

1. Fill in your **Name**, **Surname**, **Age**, **Gender**, **Height**, and **Weight**.
2. Click on the **Calculate BMI** button.
3. The app will display your BMI and categorize it accordingly.

## Deployment

### Render

1. Create a **`requirements.txt`** file:
   ```bash
   pip freeze > requirements.txt
   ```

2. Create a **`Procfile`**:
   ```
   web: gunicorn app:app
   ```

3. Push your code to GitHub and follow Render deployment steps.

### Heroku

1. Login to Heroku:
   ```bash
   heroku login
   ```

2. Create and push to Heroku:
   ```bash
   heroku create
   git push heroku master
   ```

3. Open the app:
   ```bash
   heroku open
   ```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
