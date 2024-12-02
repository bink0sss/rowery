# System Wynajmu Rowerów

System umożliwia zarządzanie wynajmem rowerów, w tym rejestrację wynajmów, ich anulowanie, generowanie raportów oraz wysyłanie faktur za pomocą poczty elektronicznej.

---

## Wymagania

- Python 3.x
- Zainstalowane biblioteki: `json`, `os`, `datetime`, `smtplib`, `email`
- Folder `data` w katalogu głównym (jeśli nie istnieje, zostanie utworzony automatycznie)

---

## Funkcje

### 1. `rent_bike()`
Rejestruje nowy wynajem roweru.

- **Wprowadzane dane:**
  - Imię klienta
  - Czas wynajmu w godzinach
  - Opcjonalnie: Adres e-mail do wysłania faktury
- **Działanie:**
  - Oblicza koszt wynajmu za pomocą funkcji `calculate_cost`.
  - Zapisuje dane wynajmu do pliku `rentals.json` za pomocą `save_rental`.
  - Opcjonalnie wysyła fakturę e-mail poprzez funkcję `send_rental_invoice_email`.

---

### 2. `calculate_cost(rental_duration)`
Oblicza koszt wynajmu w oparciu o czas trwania.

- **Logika obliczeń:**
  - Pierwsza godzina: 10 PLN
  - Każda dodatkowa godzina: 5 PLN

---

### 3. `save_rental(rental)`
Zapisuje informacje o wynajmie do pliku `rentals.json`.

- **Działanie:**
  - Tworzy plik `rentals.json` w folderze `data`, jeśli jeszcze nie istnieje.
  - Dodaje nowe dane do istniejącego pliku.

---

### 4. `load_rentals()`
Ładuje dane wynajmów z pliku `rentals.json`.

- **Zwracane dane:** Lista zarejestrowanych wynajmów.

---

### 5. `cancel_rental()`
Anuluje wynajem na podstawie imienia klienta.

- **Wprowadzane dane:**
  - Imię klienta
- **Działanie:**
  - Usuwa wszystkie wynajmy powiązane z podanym imieniem z pliku `rentals.json`.

---

### 6. `generate_daily_report()`
Generuje raport dzienny z wynajmów.

- **Działanie:**
  - Tworzy plik raportu w folderze `data` z nazwą w formacie: `daily_report_YYYY-MM-DD.json`.

---

### 7. `send_rental_invoice_email(customer_email, rental_details)`
Wysyła fakturę za wynajem na podany adres e-mail.

- **Wymagane dane:**
  - Adres e-mail klienta
  - Szczegóły wynajmu (np. czas trwania, koszt)
- **Działanie:**
  - Używa SMTP do wysłania wiadomości e-mail.

**Uwaga:** Funkcja wymaga poprawnego skonfigurowania danych logowania do serwera SMTP.

---

## Jak używać?

1. Uruchom skrypt: `python bike_rental.py`.
2. Wybierz jedną z dostępnych opcji:
   - **1:** Wynajem roweru
   - **2:** Anulowanie wynajmu
   - **3:** Generowanie raportu dziennego
   - **4:** Wyjście z systemu

---

## Struktura plików
bike_rental/ <br>
├── data/ <br>
│   ├── rentals.json              # Plik z zapisanymi wynajmami<br>
│   ├── daily_report_YYYY-MM-DD.json  # Generowane raporty dzienne<br>
├── bike_rental.py                # Główny skrypt programu<br>
└── README.md                     # Dokumentacja projektu<br>

---

## Przyszłe ulepszenia

- Dodanie interfejsu graficznego (GUI)
- Możliwość konfiguracji kosztów wynajmu
- Obsługa większej liczby języków

---

## Autorzy

**Imię i nazwisko:** Bartosz  
**Kontakt:** bartosz21082004@gmail.com