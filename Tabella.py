import pygame
import sys

# Inizializza Pygame
pygame.init()

# Definisci le dimensioni della finestra e altri parametri
larghezza_finestra = 600
altezza_finestra = 600
colore_sfondo = (255, 255, 255)
dimensione_cella = larghezza_finestra // 15  # 15 caselle in una riga
spessore_bordo = 1

# Inizializza la finestra
finestra = pygame.display.set_mode((larghezza_finestra, altezza_finestra))
pygame.display.set_caption("Tabella Ludo")


# Funzione per disegnare la tabella
def disegna_tabella():
    for riga in range(15):
        for colonna in range(15):
            #Caselle Rosse
            if (riga == 0 and colonna in range(6)):
                colore_casella = (255, 0, 0)
            elif (riga in range(6) and colonna == 0):
                colore_casella = (255, 0, 0)
            elif (riga == 5 and colonna in range(6)):
                colore_casella = (255, 0, 0)
            elif (riga in range(6) and colonna == 5):
                colore_casella = (255, 0, 0)
            elif ((riga == 6 or riga == 7) and colonna == 1):
                colore_casella = (255, 0, 0)
            elif (riga == 7 and colonna in range(2,7)):
                colore_casella = (255, 0, 0)

            #Caselle per i pallini rossi
            elif ((riga == 2 or riga == 3) and (colonna == 2 or colonna == 3)):
                colore_casella = (255, 0, 0)

            #Caselle verdi
            elif (riga == 0 and colonna in range(9,15)):
                colore_casella = (0, 255, 0)
            elif (riga in range(6) and colonna == 9):
                colore_casella = (0, 255, 0)
            elif (riga == 5 and colonna in range(9,15)):
                colore_casella = (0, 255, 0)
            elif (riga in range(6) and colonna == 14):
                colore_casella = (0, 255, 0)
            elif (riga == 1 and (colonna == 7 or colonna == 8)):
                colore_casella = (0, 255, 0)
            elif (riga in range(1,7) and colonna == 7):
                colore_casella = (0, 255, 0)

            # Caselle per i pallini verdi
            elif ((riga == 2 or riga == 3) and (colonna == 11 or colonna == 12)):
                colore_casella = (0, 255, 0)

            #Caselle blu
            elif (riga == 9 and colonna in range(6)):
                colore_casella = (0, 0, 255)
            elif (riga in range(9,15) and colonna == 0):
                colore_casella = (0, 0, 255)
            elif (riga == 14 and colonna in range(6)):
                colore_casella = (0, 0, 255)
            elif (riga in range(9,15) and colonna == 5):
                colore_casella = (0, 0, 255)
            elif (riga == 13 and (colonna == 6 or colonna == 7)):
                colore_casella = (0, 0, 255)
            elif (riga in range(8,14) and colonna == 7):
                colore_casella = (0, 0, 255)

            #Caselle per i pallini blu
            elif ((riga == 11 or riga == 12) and (colonna == 2 or colonna == 3)):
                colore_casella = (0, 0, 255)

            #Caselle gialle
            elif (riga == 9 and colonna in range(9,15)):
                colore_casella = (255, 255, 0)
            elif (riga in range(9,15) and colonna == 9):
                colore_casella = (255, 255, 0)
            elif (riga == 14 and colonna in range(9,15)):
                colore_casella = (255, 255, 0)
            elif (riga in range(9,15) and colonna == 14):
                colore_casella = (255, 255, 0)
            elif ((riga == 7 or riga == 8) and colonna == 13):
                colore_casella = (255, 255, 0)
            elif (riga == 7 and colonna in range(8,14)):
                colore_casella = (255, 255, 0)

            #Caselle per i pallini blu
            elif ((riga == 11 or riga == 12) and (colonna == 11 or colonna == 12)):
                colore_casella = (255, 255, 0)

            #Caselle nere da cui non passare
            elif ((riga == 6 or riga == 8) and (colonna == 6 or colonna == 8)):
                colore_casella = (0, 0, 0)

            else:
                colore_casella = (255, 255, 255)

            pygame.draw.rect(finestra, colore_casella,(colonna * dimensione_cella, riga * dimensione_cella, dimensione_cella, dimensione_cella),0)
            pygame.draw.rect(finestra, (0, 0, 0),(colonna * dimensione_cella, riga * dimensione_cella, dimensione_cella, dimensione_cella),spessore_bordo)


# Ciclo principale
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Pulisci la finestra
    finestra.fill(colore_sfondo)

    # Disegna la tabella
    disegna_tabella()

    # Aggiorna la finestra
    pygame.display.flip()