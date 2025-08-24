from code.Enemy import Enemy
from code.Entity import Entity


class EntityMediator:

    @staticmethod
    def __verify_collision_window(ent: Entity):  # Significa que não consigo invocar esse metodo em outro local
        if isinstance(ent, Enemy):
            if ent.rect.right < 0: # Quando o lado direito da imagem do inimigo passar da tela zera a vida
                ent.health = 0
        pass

    @staticmethod
    def verify_collision(entity_list: list[Entity]):
        for i in range(len(entity_list)):
            test_entity = entity_list[i]
            EntityMediator.__verify_collision_window(test_entity)

    @staticmethod
    def verify_health(entity_list: list[Entity]):
        for ent in entity_list:
            if ent.health <= 0: # Se a vida da entidade for menor ou igual a zero
                entity_list.remove(ent) # Remove a entidade

