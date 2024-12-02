import json
import os
import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Ścieżka do plików
RENTALS_FILE = 'data/rentals.json'

# Funkcja do wynajmu roweru
def rent_bike():
    customer_name = input("Enter your name: ")
    rental_duration = float(input("Enter rental duration in hours: "))
    
    # Sprawdzanie poprawności danych
    if rental_duration <= 0:
        print("Rental duration must be greater than 0")
        return

    cost = calculate_cost(rental_duration)
    rental = {
        'customer_name': customer_name,
        'rental_duration': rental_duration,
        'cost': cost,
        'rental_date': str(datetime.datetime.now())
    }
    save_rental(rental)
    print(f"Rental successful! Total cost: {cost} PLN")
    
    send_invoice = input("Do you want to receive an invoice by email? (yes/no): ").strip().lower()
    if send_invoice == 'yes':
        customer_email = input("Enter your email address: ")
        send_rental_invoice_email(customer_email, rental)
    
    return rental

# Funkcja do obliczania kosztu wynajmu
def calculate_cost(rental_duration):
    if rental_duration <= 1:
        return 10
    else:
        return 10 + (rental_duration - 1) * 5

# Funkcja do zapisu wynajmu w pliku JSON
def save_rental(rental):
    if not os.path.exists('data'):
        os.makedirs('data')

    if os.path.exists(RENTALS_FILE):
        with open(RENTALS_FILE, 'r') as file:
            rentals = json.load(file)
    else:
        rentals = []

    rentals.append(rental)
    with open(RENTALS_FILE, 'w') as file:
        json.dump(rentals, file, indent=4)

# Funkcja do ładowania wynajmów z pliku JSON
def load_rentals():
    if os.path.exists(RENTALS_FILE):
        with open(RENTALS_FILE, 'r') as file:
            return json.load(file)
    return []

# Funkcja do anulowania wynajmu
def cancel_rental():
    customer_name = input("Enter the name of the customer to cancel rental: ")
    rentals = load_rentals()
    rentals = [rental for rental in rentals if rental['customer_name'] != customer_name]
    with open(RENTALS_FILE, 'w') as file:
        json.dump(rentals, file, indent=4)
    print(f"Rental for {customer_name} has been canceled.")

# Funkcja generująca raport dzienny
def generate_daily_report():
    rentals = load_rentals()
    date_str = datetime.datetime.now().strftime('%Y-%m-%d')
    report_filename = f"data/daily_report_{date_str}.json"
    with open(report_filename, 'w') as file:
        json.dump(rentals, file, indent=4)
    print(f"Daily report generated: {report_filename}")

# Funkcja wysyłająca fakturę przez e-mail
def send_rental_invoice_email(customer_email, rental_details):
    subject = 'Invoice for Bike Rental'
    body = f"Hello {rental_details['customer_name']},\n\nHere are your rental details:\n" \
           f"Duration: {rental_details['rental_duration']} hours\n" \
           f"Total Cost: {rental_details['cost']} PLN\n\nThank you for renting with us!"

    msg = MIMEMultipart()
    msg['From'] = 'smtp.gmail.com'  # Użyj swojego adresu e-mail
    msg['To'] = customer_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)  # Użyj właściwego serwera SMTP
        server.starttls()
        server.login('bartosz21082004@gmail.com', '')  # Użyj prawdziwych danych logowania
        text = msg.as_string()
        server.sendmail('bartosz21082004@gmail.com', customer_email, text)
        server.quit()
        print(f"Invoice sent to {customer_email}")
    except Exception as e:
        print(f"Error sending email: {e}")

# Przykład uruchomienia programu
if __name__ == '__main__':
    while True:
        print("\nBike Rental System")
        print("1. Rent a bike")
        print("2. Cancel a rental")
        print("3. Generate daily report")
        print("4. Exit")
        choice = input("Select an option (1-4): ")

        if choice == '1':
            rent_bike()
        elif choice == '2':
            cancel_rental()
        elif choice == '3':
            generate_daily_report()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")
