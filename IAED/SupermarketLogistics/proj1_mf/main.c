/*
 * Ficheiro:  main.c
 * Autor:  Joao Lopes
 * Descricao:  Ficheiro fonte para executar o sistema de logistica que gere
 			   stocks de produtos e encomendas
*/
#include <stdio.h>
#include <stdlib.h>

#include "features.h"
#include "sort.h"

/* Regula o fluxo de instrucoes ao longo do programa*/
int main() {
	int comando;
	
	inicia_registo_encomendas();

	while ((comando = getchar())) {
		switch (comando) {
			case 'a':
				adiciona_produto();
				break;
			case 'q':
				adiciona_stock();
				break;
			case 'N':
				cria_encomenda();
				break;
			case 'A':
				fornece_encomenda();
				break;
			case 'r':
				remove_stock();
				break;
			case 'R':
				remove_produto_encomenda();
				break;
			case 'C':
				calcula_custo_encomenda();
				break;
			case 'p':
				altera_preco_produto();
				break;
			case 'E':
				lista_quantidade_produto();
				break;
			case 'm':
				lista_produto_mais_referenciado();
				break;
			case 'l':
				lista_produtos_sistema();
				break;
			case 'L':
				lista_produtos_encomenda();
				break;
			case 'x':
				return EXIT_SUCCESS;
		}
	}
	return EXIT_FAILURE;
}