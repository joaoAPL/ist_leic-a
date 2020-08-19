/*
 * Ficheiro:  features.c
 * Autor:  Joao Lopes
 * Descricao:  Ficheiro fonte com as funcionalidade de sistema de logistica
*/
#include <stdio.h>
#include <string.h>

#include "features.h"
#include "sort.h"

/* Inicia o registo de encomendas limpo*/
void inicia_registo_encomendas() {
	int indice_encomenda, indice_produto;

	for (indice_encomenda = 0; indice_encomenda < MAXENCOM; ++indice_encomenda)
		for (indice_produto = 0; indice_produto < MAXPROD; ++indice_produto)
			encomendas[indice_encomenda].idp_produtos[indice_produto] = PRODUTO_OUT;
} 

/* Adiciona um produto ao sistema com uma identificacao*/
void adiciona_produto() {

	scanf(" %[^:]:%d:%d:%d", produtos[idp].desc, &produtos[idp].custo,
	&produtos[idp].peso, &produtos[idp].quantidade);
	printf("Novo produto %d.\n", idp);
	++idp;
}

/* Adiciona stock a um produto existente no sistema*/
void adiciona_stock() {
	int idp_instrucao, quantidade;

	scanf(" %d:%d", &idp_instrucao, &quantidade);
	if (idp_instrucao < idp)
		produtos[idp_instrucao].quantidade += quantidade;
	else
		printf("Impossivel adicionar produto %d ao stock. "
			"Produto inexistente.\n", idp_instrucao);
}

/* Cria uma nova encomenda com uma identificacao*/
void cria_encomenda() {
	
	printf("Nova encomenda %d.\n", ide);
	++ide;
}

/* Fornece uma encomenda com produtos*/
void fornece_encomenda() {
	int ide_instrucao, idp_instrucao;
	int quantidade;
	int estado_produto;
	int indice_produto;

	scanf(" %d:%d:%d", &ide_instrucao, &idp_instrucao, &quantidade);

	if (ide_instrucao < ide && idp_instrucao < idp &&
		quantidade <= produtos[idp_instrucao].quantidade && 
		encomendas[ide_instrucao].peso + quantidade * produtos[idp_instrucao].peso 
		<= MAXPROD) {
		estado_produto = PRODUTO_OUT;
		for (indice_produto = 0; indice_produto < MAXPROD; ++indice_produto)
			if (encomendas[ide_instrucao].idp_produtos[indice_produto] == idp_instrucao) {
				estado_produto = PRODUTO_IN;
				encomendas[ide_instrucao].peso += quantidade * 
				produtos[idp_instrucao].peso;
				encomendas[ide_instrucao].quantidade_produtos[indice_produto] +=
				quantidade;
				produtos[idp_instrucao].quantidade -= quantidade;
				indice_produto = MAXPROD;
			}
		if (estado_produto == PRODUTO_OUT) {
			for (indice_produto = 0; indice_produto < MAXPROD && 
				encomendas[ide_instrucao].idp_produtos[indice_produto] != PRODUTO_OUT;
				++indice_produto);
			encomendas[ide_instrucao].idp_produtos[indice_produto] = idp_instrucao;
			encomendas[ide_instrucao].peso += quantidade * produtos[idp_instrucao].peso;
			encomendas[ide_instrucao].quantidade_produtos[indice_produto] = quantidade;
			produtos[idp_instrucao].quantidade -= quantidade;
		}
	}
	else
		if (ide_instrucao >= ide)
			printf("Impossivel adicionar produto %d a encomenda %d. "
				"Encomenda inexistente.\n", idp_instrucao, ide_instrucao);
		else if (idp_instrucao >= idp)
				printf("Impossivel adicionar produto %d a encomenda %d. "
					"Produto inexistente.\n", idp_instrucao, ide_instrucao);
		else if (quantidade > produtos[idp_instrucao].quantidade)
			printf("Impossivel adicionar produto %d a encomenda %d. "
				"Quantidade em stock insuficiente.\n", idp_instrucao, 
				ide_instrucao);
		else
			printf("Impossivel adicionar produto %d a encomenda %d. "
						"Peso da encomenda excede o maximo de 200.\n", idp_instrucao, 
						ide_instrucao);
}

/* Remove stock a um produto numa certa quantidade*/
void remove_stock() {
	int idp_instrucao, quantidade;

	scanf(" %d:%d", &idp_instrucao, &quantidade);
	if (idp_instrucao < idp)
		if (quantidade <= produtos[idp_instrucao].quantidade)
			produtos[idp_instrucao].quantidade -= quantidade;
		else
			printf("Impossivel remover %d unidades do produto %d "
				"do stock. Quantidade insuficiente.\n", quantidade, idp_instrucao);
	else
		printf("Impossivel remover stock do produto %d. "
			"Produto inexistente.\n", idp_instrucao);
}

/* Remove totalmente um produto duma encomenda no sistema*/
void remove_produto_encomenda() {
	int ide_instrucao, idp_instrucao;
	int indice_produto;

	scanf(" %d:%d", &ide_instrucao, &idp_instrucao);

	if (ide_instrucao < ide) {
		if (idp_instrucao < idp) {
			for (indice_produto = 0; indice_produto < MAXPROD; ++indice_produto)
				if (encomendas[ide_instrucao].idp_produtos[indice_produto] == idp_instrucao) {
					produtos[idp_instrucao].quantidade += 
					encomendas[ide_instrucao].quantidade_produtos[indice_produto];
					encomendas[ide_instrucao].peso -= 
					encomendas[ide_instrucao].quantidade_produtos[indice_produto] * 
					produtos[idp_instrucao].peso;
					encomendas[ide_instrucao].quantidade_produtos[indice_produto] = 0;
					encomendas[ide_instrucao].idp_produtos[indice_produto] = PRODUTO_OUT;
					indice_produto = MAXPROD;
				}
		}
		else
			printf("Impossivel remover produto %d a encomenda %d. "
			"Produto inexistente.\n", idp_instrucao, ide_instrucao);
	}
	else
		printf("Impossivel remover produto %d a encomenda %d. "
			"Encomenda inexistente.\n", idp_instrucao, ide_instrucao);
}
	
/* Calcula o custo de uma encomenda*/
void calcula_custo_encomenda() {
	int ide_instrucao;
	int custo = 0;
	int indice_produto;

	scanf(" %d", &ide_instrucao);

	if (ide_instrucao < ide) {
		for (indice_produto = 0; indice_produto < MAXPROD; ++indice_produto)
			custo += produtos[encomendas[ide_instrucao].idp_produtos[indice_produto]].custo * 
		encomendas[ide_instrucao].quantidade_produtos[indice_produto];
		printf("Custo da encomenda %d %d.\n", ide_instrucao, custo);
	}
	else
		printf("Impossivel calcular custo da encomenda %d. "
			"Encomenda inexistente.\n", ide_instrucao);
}

/* Altera o preco de um produto existente no sistema*/
void altera_preco_produto() {
	int idp_instrucao, custo_instrucao;

	scanf(" %d:%d", &idp_instrucao, &custo_instrucao);
	if (idp_instrucao < idp)
		produtos[idp_instrucao].custo = custo_instrucao;
	else
		printf("Impossivel alterar preco do produto %d. "
			"Produto inexistente.\n", idp_instrucao);
}

/* Lista a descricao e a quantidade de um dado produto numa encomenda*/
void lista_quantidade_produto() {
	int ide_instrucao, idp_instrucao;
	int indice_produto;

	scanf(" %d:%d", &ide_instrucao, &idp_instrucao);

	if (ide_instrucao < ide)
		if (idp_instrucao < idp) {
			for (indice_produto = 0; 
				encomendas[ide_instrucao].idp_produtos[indice_produto] 
				!= idp_instrucao && indice_produto < MAXPROD;
				++indice_produto);
			if (indice_produto != MAXPROD)
				printf("%s %d.\n", produtos[idp_instrucao].desc, 
					encomendas[ide_instrucao].quantidade_produtos[indice_produto]);
			else
				printf("%s 0.\n", produtos[idp_instrucao].desc);
		}
		else
			printf("Impossivel listar produto %d. "
				"Produto inexistente.\n", idp_instrucao);
	else
		printf("Impossivel listar encomenda %d. "
				"Encomenda inexistente.\n", ide_instrucao);
}

/* Lista a encomenda com o produto procurado em maior quantidade*/
void lista_produto_mais_referenciado() {
	int idp_instrucao;
	int indice_encomenda, indice_produto;
	int estado_produto;
	int max_referencia = 0;
	int ide_referencia = 0, idp_referencia = 0;

	scanf(" %d", &idp_instrucao);

	if (idp_instrucao < idp) {
		estado_produto = PRODUTO_OUT;
		for (indice_encomenda = 0; indice_encomenda < MAXENCOM; ++indice_encomenda) {
			for (indice_produto = 0; indice_produto < MAXPROD; ++indice_produto)
				if (encomendas[indice_encomenda].idp_produtos[indice_produto] == idp_instrucao)
					if (encomendas[indice_encomenda].quantidade_produtos[indice_produto] > max_referencia || 
						(encomendas[indice_encomenda].quantidade_produtos[indice_produto] == max_referencia && 
							indice_encomenda < ide_referencia)) {
					max_referencia = 
					encomendas[indice_encomenda].quantidade_produtos[indice_produto];
					ide_referencia = indice_encomenda;
					idp_referencia = indice_produto;
					indice_produto = MAXPROD;
					estado_produto = PRODUTO_IN;
					}
		}
		if (estado_produto == PRODUTO_IN)
			printf("Maximo produto %d %d %d.\n", idp_instrucao, ide_referencia, 
				encomendas[ide_referencia].quantidade_produtos[idp_referencia]);
	}
	else
		printf("Impossivel listar maximo do produto %d. "
			"Produto inexistente.\n", idp_instrucao);
}

/* Lista todos os produtos contidos no sistema por ordem crescente de preco*/
void lista_produtos_sistema() {
	int custo_produtos[MAXSISTEMA], idp_produtos[MAXSISTEMA];
	int indice_produto;
	int indice_1, indice_2;

	for (indice_produto = 0; indice_produto < idp; ++indice_produto) {
		idp_produtos[indice_produto] = indice_produto;
		custo_produtos[indice_produto] = produtos[indice_produto].custo;
	}

	quick_sort(custo_produtos, idp_produtos, 0, idp - 1);
	/* Devido a instabilidade do Quick_sort e necessario nova ordenacao.
	   Neste caso apenas interessam chaves adjacentes com custo igual*/
	for (indice_1 = 0; indice_1 < idp - 1; ++indice_1)
		for (indice_2 = indice_1 + 1; indice_2 < idp; ++indice_2)
			if (custo_produtos[indice_1] == custo_produtos[indice_2]) {
				for (; custo_produtos[indice_1] == custo_produtos[indice_2 + 1] && 
					indice_2 < idp; ++indice_2);
				/* Aplica o Selection_sort ao conjunto restrito de chaves adjacentes
				   com custo igual*/
				selection_sort(custo_produtos, idp_produtos, indice_1, indice_2);
				indice_1 = indice_2;
				break;
			}

	printf("Produtos\n");
	for (indice_produto = 0; indice_produto < idp; ++indice_produto)
		printf("* %s %d %d\n", produtos[idp_produtos[indice_produto]].desc, 
			produtos[idp_produtos[indice_produto]].custo,
			produtos[idp_produtos[indice_produto]].quantidade);
}

/* Lista todos os produtos contidos numa encomenda por ordem alfabetica*/
void lista_produtos_encomenda() {
	int ide_instrucao;
	int indice_e, indice_d;
	int indice_produto;
	int min, auxiliar_idp, auxiliar_quantidade;

	scanf(" %d", &ide_instrucao);

	/* Aplica uma versao alterada do Quick_sort em que chaves com valor -1 (PRODUTO_OUT)
	   sao ignoradas. A comparacao e efectuada entre strings de descricao*/
	if (ide_instrucao < ide) {
		for (indice_e = 0; indice_e < MAXPROD - 1; indice_e++) {
			min = indice_e;
			for (indice_d = indice_e + 1; indice_d < MAXPROD; indice_d++) {
				if (encomendas[ide_instrucao].idp_produtos[indice_e] != PRODUTO_OUT && 
					encomendas[ide_instrucao].idp_produtos[indice_d] != PRODUTO_OUT)
						if (strcmp(
							produtos[encomendas[ide_instrucao].idp_produtos[indice_d]].desc, 
							produtos[encomendas[ide_instrucao].idp_produtos[min]].desc) < 0)
							min = indice_d;
			}
			auxiliar_idp = encomendas[ide_instrucao].idp_produtos[indice_e];
			auxiliar_quantidade = encomendas[ide_instrucao].quantidade_produtos[indice_e];
			encomendas[ide_instrucao].idp_produtos[indice_e] =
			encomendas[ide_instrucao].idp_produtos[min];
			encomendas[ide_instrucao].quantidade_produtos[indice_e] = 
			encomendas[ide_instrucao].quantidade_produtos[min];
			encomendas[ide_instrucao].idp_produtos[min] = auxiliar_idp;
			encomendas[ide_instrucao].quantidade_produtos[min] = auxiliar_quantidade;
		}

		printf("Encomenda %d\n", ide_instrucao);
		for (indice_produto = 0; indice_produto < MAXPROD; ++indice_produto)
			if (encomendas[ide_instrucao].idp_produtos[indice_produto] != -1)
				printf("* %s %d %d\n", 
					produtos[encomendas[ide_instrucao].idp_produtos[indice_produto]].desc, 
					produtos[encomendas[ide_instrucao].idp_produtos[indice_produto]].custo,
					encomendas[ide_instrucao].quantidade_produtos[indice_produto]);
	}
	else
		printf("Impossivel listar encomenda %d. Encomenda inexistente.\n", ide_instrucao);
}