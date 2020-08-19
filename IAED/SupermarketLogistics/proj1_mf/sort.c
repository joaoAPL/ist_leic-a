/*
 * Ficheiro:  sort.c
 * Autor:  Joao Lopes
 * Descricao:  Ficheiro fonte com os algoritmos de ordenacao do sistema 
 			   de logistica
*/
#include "sort.h"

/* Ordena os produtos no sistema de logistica por custo em ordem ascendente*/
void quick_sort(int custo_produtos[], int idp_produtos[], int esquerda, 
	int direita) {

	int indice;

	if (direita <= esquerda)
		return;
	indice = particao(custo_produtos, idp_produtos, esquerda, direita);
	quick_sort(custo_produtos, idp_produtos, esquerda, indice - 1);
	quick_sort(custo_produtos, idp_produtos, indice + 1, direita) ;
}

int particao(int custo_produtos[], int idp_produtos[], int esquerda, 
	int direita) {

	int indice_e = esquerda - 1, indice_d = direita;
	int v = custo_produtos[direita];
	int auxiliar_custo, auxiliar_idp;

	while (indice_e < indice_d) {
		while (custo_produtos[++indice_e] < v);
		while (v < custo_produtos[--indice_d])
			if (indice_d == esquerda)
				break;
		if (indice_e < indice_d) {
			auxiliar_custo = custo_produtos[indice_e];
			auxiliar_idp = idp_produtos[indice_e];
			custo_produtos[indice_e] = custo_produtos[indice_d];
			idp_produtos[indice_e] = idp_produtos[indice_d];
			custo_produtos[indice_d] = auxiliar_custo;
			idp_produtos[indice_d] = auxiliar_idp;
		}
	}
	auxiliar_custo = custo_produtos[indice_e];
	auxiliar_idp = idp_produtos[indice_e];
	custo_produtos[indice_e] = custo_produtos[direita];
	idp_produtos[indice_e] = idp_produtos[direita];
	custo_produtos[direita] = auxiliar_custo;
	idp_produtos[direita] = auxiliar_idp;

	return indice_e;
}

/* Ordena os produtos no sistema de logistica por custo em ordem ascendente*/
void selection_sort(int custo_produtos[], int idp_produtos[], int indice_1, int indice_2) {
	int indice_e, indice_d;
	int auxiliar_custo, auxiliar_idp, min;

	for (indice_e = indice_1; indice_e <= indice_2 - 1; indice_e++) {
		min = indice_e;
		for (indice_d = indice_e + 1; indice_d <= indice_2; indice_d++) {
			/* Depois da ordenacao efectuada pelo Quick_sort, resta encontrar
			   chaves com o mesmo custo mas com idp desordenados*/
			if (custo_produtos[indice_d] == custo_produtos[min] && 
				idp_produtos[indice_d] < idp_produtos[min])
				min = indice_d;
			/* Caso encontre uma chave com custo diferente do procurado
			   cessa a procura dentro do vector de custos*/
			if (custo_produtos[indice_d] != custo_produtos[min])
				indice_d = idp;
		}

		auxiliar_custo = custo_produtos[indice_e];
		auxiliar_idp = idp_produtos[indice_e];
		custo_produtos[indice_e] = custo_produtos[min];
		idp_produtos[indice_e] = idp_produtos[min];
		custo_produtos[min] = auxiliar_custo;
		idp_produtos[min] = auxiliar_idp;
	}
}