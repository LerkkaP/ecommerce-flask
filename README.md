# Luxury watch e-commerce website

This project is an exercise for the course Databases and Web Programming at the University of Helsinki. It simulates a luxury watch e-commerce platform.

## Features

- **User accounts**: Users can create accounts to log in and access additional functionalities.

- **Shopping cart**: Logged-in users can add watches to their shopping cart for convenient checkout.

- **Mocked payment system**: While not using real payment processing, the system is designed to simulate the purchase process. Real payment integration, e.g., with Stripe, could be implemented in the future.

- **Custom CSS styling**: The project features custom CSS styling for a unique and visually appealing user interface.

- **Admin panel**: An admin panel is provided, allowing users with admin privileges to manage various aspects of the website, such as adding new watches and handling reviews.

- **User reviews**: Authenticated users can provide reviews and ratings for watches, contributing to the overall user experience.

- **JavaScript for dynamicality**: JavaScript is utilized to add dynamicality to the website, enhancing user interaction and providing a more seamless experience.

- **Responsive Design (Laptops and Larger Screens)**: This app is designed to be somewhat responsive for laptops and larger screens.
  While efforts have been made to ensure a reasonable viewing experience on these devices,
  it is not fully optimized for mobile devices.

## Technologies used

- **Frontend**: HTML, CSS, JavaScript

- **Backend**: Python, Flask

- **Database**: PostgreSQL

## Database schema

![Alt text](image.png)

## Installation guide

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/LerkkaP/ecommerceFlask.git
   ```

2. Navigate to the project root

3. Create a .env file in the root directory of the project and add your environment variables:

   ```bash
   DATABASE_URL = your_local_database_url
   SECRET_KEY = your_secret_key
   ```

4. Activate virtual environment:

   ```bash
   python3 -m venv venv
   ```

   ```bash
   source venv/bin/activate
   ```

5. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

6. Set up the database:

   ```bash
   psql < schema.sql
   ```

   ```bash
   psql < seed.sql
   ```

7. Run the application:

   ```bash
   python3 main.py
   ```

## Seed Data

The seed data includes the following:

- 12 watches have been added to the store in the database.

- Two user accounts have been created for testing purposes:

  1. Admin user:

     - Username: `admin`
     - Password: `Adminpassword23!`

     This account has administrative privileges.

  2. Customer user:

     - Username: `alice`
     - Password: `Customerpassword1!`

     This account has customer privileges.

- To access the admin panel, log in with the admin account and visit the URL `/admin`.

- You can use these accounts to test the application. If you wish to create additional accounts, you can do so through `psql`. Please make sure to specify the privileges (either `admin` or `customer`) and save the password in hashed form using `sha256`.

- Additionally, you can add new watches through `psql` or the admin panel (if logged in with an admin account). While adding an image is optional, it is recommended to maintain the integrity of the user interface. If you choose to include an image, please remember to manually add it to the `images/watches` folder in the static directory.

  For specific naming conventions for watch images, please refer to the `images/watches` folder in the project directory.
