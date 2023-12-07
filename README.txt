Titolo del Progetto: Applicazione del Deep Q-learning al Gioco da Tavolo Ludo

Obiettivi:
Questo progetto si propone di sviluppare e implementare un sistema avanzato di apprendimento per rinforzo
applicato al gioco da tavolo Ludo. Gli obiettivi specifici includono:
• Apprendimento di una Strategia di Gioco Ottimale: Creare un agente intelligente capace di
apprendere una strategia di gioco ottimale nel Ludo attraverso l'impiego del Deep Q-learning,
migliorando nel tempo le decisioni tattiche durante le partite.
• Definizione degli Stati del Gioco: Identificare in modo accurato gli stati del gioco, considerando la
posizione delle pedine dell'agente e degli avversari, nonché le condizioni del tabellone di gioco.
• Azioni Tattiche Avanzate: Definire azioni avanzate che consentano all'agente di prendere decisioni
tatiche mirate, come il movimento di pedine specifiche, la decisione di occupare o evitare
determinate caselle, e la gestione delle risorse di gioco.
• Implementazione dell’agente basato su Deep Q-learning: Sviluppare un sistema di apprendimento
per rinforzo basato su Deep Q-learning.
Metodologia di Implementazione:
• Simulazione del Gioco Ludo: Implementare un ambiente virtuale per simulare partite di Ludo,
considerando le regole del gioco e fornendo una rappresentazione realistica delle dinamiche di gioco.
• Sviluppo dell'Agente di Gioco: Implementare un agente basato su Deep Q-learning capace di
apprendere strategie complesse.
• Definizione degli Stati e delle Azioni Tattiche: Identificare in modo dettagliato gli stati del gioco e
definire azioni tattiche avanzate, considerando variabili come la posizione delle pedine, le condizioni
del gioco e le dinamiche strategiche.
• Addestramento Iterativo e Fine-Tuning: Condurre sessioni di addestramento iterativo, ottimizzando
i parametri e le strategie di gioco dell'agente attraverso partite simulate.
• Valutazione delle Prestazioni: Valutare le prestazioni dell'agente in termini di capacità di
apprendimento della strategia di gioco ottimale, vincendo partite contro avversari virtuali.

Risultati:
• Dimostrazione dell'abilità dell'agente nel vincere partite contro avversari virtuali.
• Ottimizzazione delle prestazioni dell'agente attraverso l'addestramento iterativo, evidenziando
miglioramenti nella strategia di gioco.
• Analisi delle prestazioni in scenari di gioco variati.
• Discutere le sfide affrontate durante l'implementazione e come sono state risolte.


REGOLE DEL GIOCO
-Per iniziare a muovere le pedine, un giocatore deve ottenere un 6 nel lancio del dado.
Una volta ottenuto un 6, il giocatore può scegliere di inserire una nuova pedina nel tabellone o
muovere una pedina già presente sul tabellone.
-I giocatori lanciano un dado (caso non esce 6 e si ha almeno una pedina in gioco) per determinare il
numero di spazi che possono muovere una delle loro pedine.
-Nel caso in cui un giocatore ottenga un numero che non può essere utilizzato per muovere alcuna pedina,
il suo turno passa al giocatore successivo.
-Se una pedina atterra su uno spazio occupato da una pedina avversaria, la pedina avversaria viene
catturata e rimandata nella zona di partenza. Il giocatore che cattura una pedina avversaria ottiene un altro lancio del dado.
-Due pedine dello stesso colore non possono occupare la stessa casella contemporaneamente.
-Il primo giocatore che riesce a far entrare tutte e quattro le sue pedine nella zona di arrivo vince.