from VetorOrdenadoGulosa import VetorOrdenadoGulosa


class Gulosa:
    def __init__(self, objetivo):
        self.objetivo = objetivo
        self.encontrado = False

    def buscar(self, atual):
        print("--------")
        print("Atual: {}".format(atual.rotulo))
        atual.visitado = True

        if atual == self.objetivo:
            self.encontrado = True
        else:
            vetor_ordenado = VetorOrdenadoGulosa(len(atual.adjacentes))
            for adjacente in atual.adjacentes:
                if not adjacente.vertice.visitado:
                    adjacente.vertice.visitado = True
                    vetor_ordenado.insere(adjacente.vertice)

            vetor_ordenado.imprime()

            if vetor_ordenado.valores[0] is not None:
                self.buscar(vetor_ordenado.valores[0])
