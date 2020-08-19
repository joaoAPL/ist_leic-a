/*
 * Ficheiro:  features.h
 * Autor:  Joao Lopes
 * Descricao:  Ficheiro header com as funcionalidade de sistema de logistica
*/
#ifndef FEATURES_H_
#define FEATURES_H_

/* A capacidade maxima de produtos no sistema*/
#define MAXSISTEMA 10000
/* O numero maximo de encomendas que o sistema suporta*/
#define MAXENCOM 500

/* O comprimento maximo da descricao de um produto*/
#define MAXDESC 63

/* O numero maximo de produtos que uma encomenda pode ter*/
#define MAXPROD	200

/* O estado de uma encomenda com um produto procurado*/
#define PRODUTO_IN 1
/* O estado de uma encomenda sem um produto procurado*/
#define PRODUTO_OUT -1

/* O conjunto de dados de um produto*/
typedef struct produto {
	char desc[MAXDESC];
	int custo;
	int peso;
	int quantidade;
} Produto;

/* O conjunto de dados de uma encomenda*/
typedef struct encomenda {
	int idp_produtos[MAXPROD];
	int quantidade_produtos[MAXPROD];
	int peso;
} Encomenda;

/* Vector de Produtos que guardam cada produto adicionado no sistema*/
Produto produtos[MAXSISTEMA];
/* Vector de Encomendas que guardam cada encomenda adicionada no sistema*/
Encomenda encomendas[MAXENCOM];

/* Define a funcao auxiliar que inicia o registo de encomendas*/
void inicia_registo_encomendas();
/* Define o comando '__a__'*/
void adiciona_produto();
/* Define o comando '__q__'*/
void adiciona_stock();
/* Define o comando '__N__'*/
void cria_encomenda();
/* Define o comando '__A__'*/
void fornece_encomenda();
/* Define o comando '__r__'*/
void remove_stock();
/* Define o comando '__R__'*/
void remove_produto_encomenda();
/* Define o comando '__C__'*/
void calcula_custo_encomenda();
/* Define o comando '__p__'*/
void altera_preco_produto();
/* Define o comando '__E__'*/
void lista_quantidade_produto();
/* Define o comando '__m__'*/
void lista_produto_mais_referenciado();
/* Define o comando '__l__'*/
void lista_produtos_sistema();
/* Define o comando '__L__'*/
void lista_produtos_encomenda();

#endif