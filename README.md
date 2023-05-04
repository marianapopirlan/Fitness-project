
Proiectul are 4 sectiuni principale:

1) Sectiunea "Home", care sa prezinte un dashboard cu cateva informatii generale legate de 
managementul salii de fitness. Exemplu: numar membri activi, numar membri noi luna asta, 
numar membri care nu au reinnoit abonamentele, membri carora le expira abonamentele curand, etc. numar instructori, numar clase programate, grupe de varsta membri etc.
2) Sectiunea "Membri", care sa listeze toti membrii inrolati si informatii despre ei, fie intr-un 
tabel (varianta simpla), fie printr-un click pe fiecare membru prin care sa se deschida o 
pagina cu profilul lui (varianta mai complexa). Informatiile necesare pentru un membru ar fi:
nume, prenume, data nasterii, e-mail, data inscrierii in club, data expirarii abonamentului. 
Pentru fiecare client ar trebui sa avem cel putin doua butoane, unul de "Remove" care sterge 
clientul si unul de "Extindere abonament" care permite schimbarea datei de expirare a 
abonamentului. De asemenea, ar trebui sa avem un buton de "Add Member", care sa permita 
adaugarea informatiilor despre un nou membru.
3) Sectiunea "Instructori", care sa listeze toti instructorii clublui si informatii despre ei 
(nume/prenume, data nasterii, e-mail, specializare, scurta descriere a activitatii). Ar trebui 
sa avem un buton de "Add instructor" si cate un buton de "Remove" pentru fiecare instructor in 
parte.
4) Sectiunea "Class", care sa contina informatii despre clasele programate ale clubului 
(ex: Yoga, Pilates, Ciclism etc). Pentru fiecare clasa, ar trebui sa avem ca informatii, 
urmatoarele: data, ora, durata cursului, tipul clasei, numele/prenumele instructorului. 
De asemenea, ar trebui sa avem butoane de "Remove" pentru fiecare in parte, respectiv de 
"Adaugare clasa", care deschide un formular unde se pot introduce informatiile despre o noua 
clasa programata (instructor-ul va fi ales dintr-un drop down generat pe baza listei de 
instructori).

Din punct de vedere vizual, aplicatia poate fi structurata printr-un navbar cu cate un buton 
corespunzand fiecareia din cele 4 sectiuni. Butoanele pentru "Membri", "Instructori" si 
"Clase" pot deschide drop down-uri care sa aiba cate doua optiuni (Listeaza, Adauga).

Din punct de vedere al bazei de date, aplicatia presupun ca ar avea nevoie de 3 tabele:

1) Members, in componenta caruia avem campurile:
•	id
•   name
•	date_of_birth
•	join_date
•	expiry_date
•	e_mail
2) Trainers, in componenta caruia avem campurile:
•	id
•	name
•	date_of_birth
•	speciality
•	description
•	e_mail
3) Classes, cu urmatoarea componenta a campurilor:
•	date
•	hour
•	duration
•	instructor
•	type

