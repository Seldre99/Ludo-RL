# Ludo RL
Ludo-RL è un progetto effettuato per l'esame di Intelligenza Artificiale ed ha previsto lo sviluppo e l'implementazione di un sistema di apprendimento per rinforzo finalizzato al gioco da tavolo Ludo. Ludo è un gioco da tavolo di percorso il cui obiettivo consiste nel condurre le proprie pedine al goal centrale del tabellone, seguendo un percorso lungo i margini dello stesso.
La definizione ell’environment è stata resa possibile tramite l’utilizzo della libreria Pygame, ed è composta da quattro zone:
- Base: posizione di partenza delle due pedine dell'agente e della CPU
- Path: posizioni nel quale le pedine possono muoversi
- Safe: caselle che portano al goal finale
- Goal: posizione di arrivo
(Per visualizzare lo schema usato vedere Immagini/Matrice Ludo.png)

Per lo sviluppo di questo progetto sono state implementate le seguenti regole di Ludo:
- Inizio della partita: Per avviare il gioco, i giocatori lanciano il dado a turno. Per mettere una pedina nel percorso di gioco, è necessario ottenere un risultato di 6. Fino a quando un giocatore non ottiene 6, deve passare il turno.
- Avanzare nel path: Una volta ottenuto un 6, il giocatore posiziona una pedina nel path e ha il diritto di lanciare nuovamente il dado. Il valore del dado indica il numero di caselle che la pedina può avanzare nel percorso. Se il giocatore ottiene un 6 di nuovo, può scegliere di inserire un'altra pedina nel percorso o muovere una pedina già presente.
- Vincolo sul dado: Se un giocatore ottiene un 6 per tre volte consecutive, deve passare il turno.

L'agente può effettuare due azioni ovvero muovere la prima pedina, muovere la seconda pedina. L'agente è stato addestrato mediante l'uso del Q-Learning e di Sarsa.

Risultati e maggiori informazioni sono presenti nella documentazione 'IA-Ludo.pdf'
