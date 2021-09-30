import sys, os
sys.setrecursionlimit(100000)

from ocho_puzzle import ocho_puzzle

if __name__ == "__main__":
    puzzle = ocho_puzzle("123H56478")
    #puzzle = ocho_puzzle("87653H241")
    #puzzle.algoritmo_anchura()
    #puzzle.algoritmo_profundidad()
    #puzzle.algoritmo_primero_mejor()
    #puzzle.algoritmo_hill_climbing()
    puzzle.algoritmo_beam()