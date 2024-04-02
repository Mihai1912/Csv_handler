# Parser și Unire de CSV-uri

## Prezentare generală

Acest script Python este conceput pentru a parsa fișiere CSV cu flexibilitate 
în gestionarea delimitatorilor și a ghilimelelor în cadrul datelor. Poate detecta 
diferiți delimitatori (virgule sau punct și virgulă), înlocuiește ghilimelele 
escapate cu un caracter diferit pentru a facilita parsarea și gestionează 
delimitatorii care apar în cadrul șirurilor între ghilimele. După parsare, 
poate uni mai multe seturi de date bazate pe o cheie comună. Acest script 
este deosebit de util pentru sarcini de integrare a datelor unde informațiile 
din diferite surse trebuie combinate într-un singur set de date.

## Funcționalități

- **Detectarea delimitatorilor**: Detectează automat dacă un fișier CSV 
folosește virgule sau punct și virgulă ca delimitatori.
- **Gestionarea ghilimelelor escapate**: Convertește ghilimelele escapate 
din date pentru a evita erorile de parsare.
- **Managementul delimitatorilor interni**: Gestionează delimitatorii care 
apar în cadrul șirurilor între ghilimele, înlocuindu-i temporar pentru a nu 
interfera cu procesul de parsare.
- **Unificarea Seturilor de Date**: Permite unirea mai multor seturi de date 
pe baza unei chei comune, util pentru integrarea datelor din surse multiple.

## Cum funcționează

1. **Detectarea delimitatorului**: Scriptul începe prin a detecta delimitatorul 
folosit în fișierele CSV.
2. **Prelucrarea șirurilor**: Fiecare linie este prelucrată pentru a înlocui 
ghilimelele escapate și pentru a gestiona delimitatorii interni care apar în 
cadrul șirurilor între ghilimele.
3. **Parsarea**: Datele sunt apoi parsate în dicționare Python, folosind antetele 
ca chei.
4. **Unificarea**: În final, seturile de date sunt unite pe baza unei chei comune, 
creând un set de date integrat.
