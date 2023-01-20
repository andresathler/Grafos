from AEstrela import AEstrela
from Grafo import Grafo
from GrafoExercicio import GrafoExercicio
from Gulosa import Gulosa
from VetorOrdenado import VetorOrdenado

grafo = GrafoExercicio()

busca = AEstrela(grafo.curitiba)
# busca = Gulosa(grafo.curitiba)

busca.buscar(grafo.portoUniao)

