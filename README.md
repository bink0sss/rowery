### Tutorial: System wynajmu rowerów - bike_rental.py

#### Struktura plików i branchy
- **Struktura plików**:
  - `bike_rental.py`: Główny plik aplikacji.
  - `data/`: Katalog zawierający pliki JSON do przechowywania wynajmów i raportów dziennych.
    - `rentals.json`: Plik przechowujący wszystkie aktywne wynajmy.
    - `daily_report_<date>.json`: Pliki zawierające raporty dzienne.
  - `README.md`: Dokumentacja projektu.

- **Branchy w Git**:
  - `main`: Główna gałąź projektu zawierająca stabilną wersję aplikacji.
  - `feature/basic_rental`: Gałąź do implementacji podstawowych funkcji wynajmu.
  - `feature/advanced_features`: Gałąź do implementacji zaawansowanych funkcji, takich jak raporty i e-maile.
  - `feature/google_calendar_integration`: Gałąź do integracji z Google Calendar.

- **Nazwy funkcji**:
  - `rent_bike(customer_name, rental_duration)`: Dodaje wynajem roweru.
  - `calculate_cost(rental_duration)`: Oblicza koszt wynajmu.
  - `save_rental(rental)`: Zapisuje dane wynajmu do pliku JSON.
  - `load_rentals()`: Wczytuje wynajmy z pliku JSON.
  - `cancel_rental(customer_name)`: Usuwa wynajem.
  - `send_rental_invoice_email(customer_email, rental_details)`: Wysyła e-mail z fakturą.
  - `generate_daily_report()`: Generuje raport dzienny.

#### Sprint 1: Podstawowe Funkcjonalności Wynajmu Rowerów

##### Milestone 1: Przygotowanie projektu
1. **Stwórz plik projektu**: Utwórz nowy plik o nazwie `bike_rental.py`.
2. **Utwórz strukturę katalogów**: Utwórz katalogi dla plików JSON, aby przechowywać wynajmy oraz raporty dzienne, np. `data/`.
3. **Importuj biblioteki**: Dodaj niezbędne importy, takie jak `json`, `datetime`, `smtplib`, i ewentualnie `os` do pracy z plikami.

##### Milestone 2: Implementacja podstawowych funkcji
1. **Funkcja rent_bike(customer_name, rental_duration)**
   - Implementuj funkcję, która przyjmuje imię klienta i czas wynajmu.
   - W funkcji wywołaj `calculate_cost()` do obliczenia kosztu wynajmu.
   - Zapisz szczegóły wynajmu do pliku JSON, korzystając z `save_rental()`.

2. **Funkcja calculate_cost(rental_duration)**
   - Implementuj obliczenia kosztu wynajmu roweru.
   - Zasady: pierwsza godzina kosztuje 10 zł, każda następna to 5 zł.

3. **Funkcja save_rental(rental)**
   - Implementuj funkcję zapisującą wynajem do pliku `rentals.json`.
   - Sprawdź, czy plik `rentals.json` istnieje, jeśli nie - utwórz go.
   - Użyj funkcji `json.dump()` do zapisu danych w pliku.

##### Milestone 3: Praca z plikiem rentals.json
1. **Funkcja load_rentals()**
   - Implementuj funkcję do odczytu istniejących wynajmów z pliku `rentals.json`.
   - Wyświetl wszystkie zapisane wynajmy.

2. **Funkcja cancel_rental(customer_name)**
   - Implementuj funkcję do anulowania wynajmu na podstawie imienia klienta.
   - Wczytaj dane z pliku `rentals.json`, usuń odpowiedni rekord i zapisz zmodyfikowane dane z powrotem do pliku.


#### Sprint 2: Zaawansowane Funkcjonalności

##### Milestone 1: Generowanie raportów dziennych
1. **Raport dzienny**: Utwórz funkcję `generate_daily_report()`, która zapisuje dane wynajmów do pliku `daily_report_<date>.json`.
   - Użyj `datetime.now()` do uzyskania dzisiejszej daty i generowania nazw plików dynamicznie.

##### Milestone 2: Wysyłanie e-maila z fakturą
1. **Funkcja send_rental_invoice_email(customer_email, rental_details)**
   - Użyj `smtplib` do wysłania e-maila z fakturą wynajmu.
   - Przygotuj treść e-maila zawierającą szczegóły wynajmu.
   - Dodaj obsługę potencjalnych błędów podczas wysyłania wiadomości.

##### Milestone 3: Integracja z Google Calendar
1. **Automatyczne przypomnienie o zwrocie**
   - Skorzystaj z API Google Calendar, aby zintegrować aplikację z kalendarzem użytkownika.
   - Użyj bibliotek takich jak `google-api-python-client` do dodawania przypomnienia o godzinie zwrotu roweru.


#### Sprint 3: Testowanie i Walidacja

##### Milestone 1: Testowanie funkcjonalności
1. **Testowanie funkcji wynajmu**
   - Przetestuj każdą funkcję w aplikacji, aby upewnić się, że działa prawidłowo.
   - Sprawdź scenariusze, takie jak brak pliku `rentals.json`, anulowanie nieistniejącego wynajmu itd.

##### Milestone 2: Walidacja danych
1. **Dodaj walidację danych wejściowych**
   - Sprawdź, czy `rental_duration` to poprawna liczba.
   - Dodaj sprawdzanie, czy imię klienta i adres e-mail są poprawne.

##### Milestone 3: Dokumentacja
1. **Przygotuj dokumentację**
   - Utwórz plik `README.md`, opisując kroki instalacji oraz używania programu.
   - Dodaj instrukcje, jak skonfigurować integrację z Google Calendar oraz wysyłanie e-maili.