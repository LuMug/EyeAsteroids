from pygame.math import Vector2

# La classe Game è la classe  che rappresenta gli oggetti in gioco in modo generico
# che verrà ereditato dagli altri oggetti in gioco.
class Game:

    # Costruttore che ha 3 parametri:
    #  position: posizione dell'oggetto come centro dell'immagine
    #  sprite: percorso dell'immagine
    #  velocity: velocità in movimento dell'oggetto
    def __init__(self, position, sprite, velocity):
        self.position = Vector2(position)
        self.sprite = sprite
        self.radius = sprite.get_width() / 2
        self.velocity = Vector2(velocity)

    # stampa l'oggetto calcolando la posizione (centro dell'oggetto) sottrando il raggio
    def draw(self, surface):
        blit_position = self.position - Vector2(self.radius)
        surface.blit(self.sprite, blit_position)

    # aggiorna la posizione dell'oggetto sommando la velocità
    def move(self):
        self.position = self.position + self.velocity

    # calcola la collisione tra gli oggetti
    def collides_with(self, other_obj):
        distance = self.position.distance_to(other_obj.position)
        return distance < self.radius + other_obj.radius
