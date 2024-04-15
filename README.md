Stworzyłem password manager, który spełnia standardy bezpieczeństwa. Bardzo trudno jest zdobyć wprowadzone tam dane użytkownika. Program działa w ten sposób:
1. By się zalogować musimy mieć swoje konto w systemie, wykorzystałem do tego zapisywanie hashów 2 hashę użytkownika i hasła mające po 256 bitów w sumie dają 512 bitów.
2. Hash jest zapisywany i by zalogować się musimy wpisać zgadzające się dane, jeśli hash nazwy użytkownika i hash hasła utworzą ten sam hash co jest na liście zalogujemy się do systemu.
3. Do subprocesu głównego programu, czyli naszego menagera haseł wysyłamy z ekranu logowania hash użytkownika. Dzięki temu będziemy mogli stworzyć indywidualny klucz użytkownika. Teraz program jest w stanie odróżnić, które hasła już wcześniej zapisane należą do tego użytkownika.
4. Klucz użytkonika to 32 znakowa część hashu, przerabiamy to na bity i szyfrujemy każde nowe dane użytkownika tym kluczem. Szyfrowanie jest symetryczne czyli tym kluczem szyfrujemy jak i deszyfrujemy.
5. Dodając hasło program sprawdza czy istnieje plik txt użytkownika. Plik txt poszczególnego użytkownika nazywa się jak 7 pierwszych wyrazów hasha użytkownika.
6. Majac ten plik dopisujemy nową stronę, użytkownika i hasło. Plik w tym momencie jest deszyfrowany zmieniony by dopisać nowe dane i znów zaszyfrowany, tak dzieje się identycznie przy metodzie wyświetlania haseł.
7. Zamykając wylogowujemy się.

Program posiada generator haseł by się nie męczyć przy tworzeniu trudnych do złamania haseł. Każde hasło powinno być inne, a hasło do zalogowania się na menager haseł mocne. 


![obraz](https://github.com/WojtekMatr/Bezpieczny-menadzer-hasel/assets/127395210/43298dd3-a2a6-4714-9218-778b2ceab95a)
[![Obejrzyj program]](https://www.youtube.com/watch?v=Rw_fVDx8JLA)

