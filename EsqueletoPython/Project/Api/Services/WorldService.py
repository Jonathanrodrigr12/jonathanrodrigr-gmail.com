from ..Repository.WorldRepository import WorldRepository
class WorldService:
    def GetWorld(self):
        repository = WorldRepository()
        return repository.GetWorld()