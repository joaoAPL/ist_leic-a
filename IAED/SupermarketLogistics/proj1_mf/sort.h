/*
 * Ficheiro:  sort.h
 * Autor:  Joao Lopes
 * Descricao:  Ficheiro header com os algoritmos de ordenacao do sistema 
 			   de logistica
*/
#ifndef SORT_H_
#define SORT_H_

/* Variaveis que delimitam o numero de produtos e encomendas actual
respectivamente*/
int idp, ide;

void quick_sort(int custo_produtos[], int idp_produtos[], int esquerda, 
	int direita);
/* Define a funcao particao que divide o vector a ordenar (faz parte do Quick
sort)*/
int particao(int custo_produtos[], int idp_produtos[], int esquerda, 
	int direita);
/* Define a funcao auxiliar de ordenamento Selection sort*/
void selection_sort(int custo_produtos[], int idp_produtos[], int indice_1, int indice_2);

#endif