from code.Constante import WIN_WIDTH
from code.EmenyShot import EnemyShot
from code.Enemy import Enemy
from code.Entity import Entity
from code.Player import Player
from code.Playershot import PlayerShot


class EntityMediator:

    @staticmethod
    def __verify_collision_window(ent: Entity):  # Significa que não consigo invocar esse metodo em outro local
        if isinstance(ent, Enemy):
            if ent.rect.right < 0: # Quando o lado direito da imagem do inimigo passar da tela zera a vida
                ent.health = 0
        if isinstance(ent, PlayerShot):
            if ent.rect.left >= WIN_WIDTH:
                ent.health = 0
        if isinstance(ent, EnemyShot):
            if ent.rect.right <= 0:
                ent.health = 0
        pass

    @staticmethod
    def __verify_collision_entity(ent1, ent2): # Verifica as colisoes do tiro do player com o inimigo e o tiro do inimigo como player
        valid_interaction = False
        if isinstance(ent1, Enemy) and isinstance(ent2, PlayerShot):
            valid_interaction = True
        elif isinstance(ent1, PlayerShot) and isinstance(ent2, Enemy):
            valid_interaction = True
        elif isinstance(ent1, Player) and isinstance(ent2, EnemyShot):
            valid_interaction = True
        elif isinstance(ent1, EnemyShot) and isinstance(ent2, Player):
            valid_interaction = True

        if valid_interaction:  # if valid_interaction == True
            if (ent1.rect.right >= ent2.rect.left and  # Verifica se uma entidade encostou na outra
                    ent1.rect.left <= ent2.rect.right and
                    ent1.rect.bottom >= ent2.rect.top and
                    ent1.rect.top <= ent2.rect.bottom):
                ent1.health -= ent2.damage  # Reduz o valor do dano na vida (CAUSA DANO)
                ent2.health -= ent1.damage
                ent1.last_dmg = ent2.name  # Verifica se a entidade foi destruida por outra entidade e não por ter saido do cenario
                ent2.last_dmg = ent1.name

    @staticmethod
    def __give_score(enemy: Enemy, entity_list: list[Entity]):
        if enemy.last_dmg == 'Player1Shot': # Verifica se o tiro que matou o inimigo é do jogador 1
            for ent in entity_list: # Procura pelo jogador 1
                if ent.name == 'Player1':
                    ent.score += enemy.score
        elif enemy.last_dmg == 'Player2Shot': # Verifica se o tiro que matou o inimigo é do jogador 2
            for ent in entity_list: # Procura pelo jogador 2
                if ent.name == 'Player2':
                    ent.score += enemy.score


    @staticmethod
    def verify_collision(entity_list: list[Entity]):
        for i in range(len(entity_list)):
            entity1 = entity_list[i]
            EntityMediator.__verify_collision_window(entity1) # Para cada entidade verifica se ela esta ou nao na janela
            for j in range(i +1, len(entity_list)):
                entity2 = entity_list[j]
                EntityMediator.__verify_collision_entity(entity1, entity2)

    @staticmethod
    def verify_health(entity_list: list[Entity]):
        for ent in entity_list:
            if ent.health <= 0: # Se a vida da entidade for menor ou igual a zero
                if isinstance(ent, Enemy): # Verifica se a entidade com a vida zerada é um inimigo
                    EntityMediator.__give_score(ent, entity_list) # Se for adiciona ao escore
                entity_list.remove(ent) # Remove a entidade (MATAR INIMIGOS E JOGADORES)

