# Laboratorium 12 - Business Intelligence w narzędziu Metabase

---

## Cel ćwiczenia
Praktyczne zapoznanie się z architekturą Business Intelligence (BI). Przeprowadzono proces zasilenia hurtowni danych (PostgreSQL), podłączenia silnika analitycznego (Metabase) oraz konstrukcji interaktywnego dashboardu.

## Zadanie 1 i 2: Środowisko i załadowanie danych
Środowisko zostało uruchomione z wykorzystaniem `docker-compose`, który orkiestrował dwa kontenery:
1. `postgres:16` - pełniący rolę analitycznej bazy danych.
2. `metabase/metabase:latest` - serwer aplikacji BI.

Dane zostały wygenerowane i załadowane z poziomu języka Python z użyciem bibliotek `pandas` oraz `sqlalchemy`. Połączenie z Metabase zrealizowano przez wewnętrzną sieć Dockera, wskazując host `postgres`.

## Zadanie 3: Analiza wizualizacji i pytania
Utworzono cztery pytania odpowiadające różnym potrzebom biznesowym:
1. **Zestawienie tabelaryczne (GUI):** Najlepsze do podglądu danych surowych i analizy pojedynczych rekordów transakcji.
2. **Wykres słupkowy (Agregacja kategorii):** Idealny do porównywania dyskretnych wartości. Szybko obrazuje, która kategoria generuje największy przychód.
3. **Tabela SQL (Zapytanie natywne):** Zaawansowana agregacja napisana w czystym SQL, wyliczająca liczbę zdarzeń i przychód.
4. **Wykres liniowy (Trend w czasie na 5.0):** Najlepszy wybór do pokazywania danych ciągłych (szeregów czasowych). Pozwala szybko wychwycić piki sprzedażowe w poszczególnych tygodniach. 

## Zadanie 4: Interaktywny Dashboard
Skonstruowano panel menedżerski. Kluczowe trendy i agregacje umieszczono na górze, a szczegółowe tabele na dole. Zaimplementowano globalny filtr zakresu dat, który zlinkowano z każdą kartą na pulpicie, co pozwala na dynamiczną analizę wybranego okresu.

**Zrzut ekranu gotowego pulpitu:**
![Dashboard Metabase1](dashboard1.png)
![Dashboard Metabase2](dashboard2.png)

## Zadanie 5: Zagadnienia teoretyczne i wskaźniki KPI

Jako wskaźnik biznesowy (KPI) zdefiniowano "Sumę przychodów" (Total Amount), a przygotowana analiza wykazała, jak zmienia się sprzedaż w kolejnych tygodniach na wykresie liniowym.

**Różnice pojęciowe i architektoniczne:**
* **Przetwarzanie danych a warstwa BI:** Przetwarzanie (np. analizowane wcześniej skrypty w Apache Spark) to przygotowanie danych: czyszczenie, transformacje, konwersje formatów. Warstwa BI (Metabase) to wizualny "front-end" dla biznesu, który tylko odczytuje gotowe dane, nie zmieniając ich struktury w samej bazie.
* **Dashboard a raport statyczny:** Raport statyczny (np. PDF) pokazuje stan danych na konkretny moment w przeszłości i jest płaski. Dashboard pozwala na interakcję, filtrowanie w locie i ukazuje aktualny stan bazy danych.
* **Zapytanie ad-hoc a zdefiniowany wskaźnik (KPI):** Zapytanie ad-hoc to jednorazowa analityka (np. sprawdzenie spadku sprzedaży w konkretny wtorek z powodu awarii). KPI to stale mierzony, powtarzalny wskaźnik kluczowy dla firmy, który na stałe znajduje się na pulpicie menedżerskim.

### Porównanie Metabase z Apache Superset 
* **Metabase** jest narzędziem niezwykle przyjaznym dla użytkowników. Jest idealny do szybkiego wdrażania dashboardów w zespołach bez zaawansowanych inżynierów danych.
* **Apache Superset** to rozbudowane narzędzie optymalizowane pod ogromne zbiory danych i bazy. Oferuje więcej skomplikowanych wizualizacji, ale wymaga lepszej znajomości języka SQL i inżynierii danych, przez co częściej używane jest w środowiskach typu Enterprise.