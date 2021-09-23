from ocho_puzzle import ocho_puzzle

if __name__ == "__main__":
    puzzle = ocho_puzzle("123H56478")
    puzzle.algoritmo_anchura(puzzle.estado_inicial)