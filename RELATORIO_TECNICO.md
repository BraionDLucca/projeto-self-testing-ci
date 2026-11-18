# RELATÓRIO TÉCNICO

## 1. Visão geral

Este documento apresenta os requisitos funcionais e não funcionais da
API de microsserviço financeiro, destinada ao gerenciamento de contas
digitais, transferências de saldo e consulta de extratos.

## 2. Requisitos funcionais

| Identificador | Descrição                                                                                                                          |
|---------------|------------------------------------------------------------------------------------------------------------------------------------|
| RF01          | O sistema deve permitir a criação de contas com valor de saldo inicial.                                                            |
| RF02          | O sistema deve permitir a consulta de contas.                                                                                      |
| RF03          | O sistema deve permitir a transferência de saldo entre contas, creditando na conta de destino o valor debitado da conta de origem. |
| RF04          | O sistema deve impedir transferências quando o saldo for insuficiente.                                                             |
| RF05          | O sistema deve impedir que o saldo de débito seja negativo, sendo o valor mínimo igual a zero.                                     |
| RF06          | O sistema deve permitir a consulta de extratos de uma conta, com filtros por data e tipo de transação (débito ou crédito).         |

## 3. Requisitos não funcionais

| Identificador | Descrição                                                                                                         |
|---------------|-------------------------------------------------------------------------------------------------------------------|
| RNF01         | Em transações concorrentes, o sistema deve garantir que apenas uma transação realize leitura ou escrita de dados. |
| RNF02         | O sistema deve responder em até 1 segundo para até 50 requisições simultâneas.                                    |

## 4. Estratégia de branching e integração contínua

O projeto utilizará **Git Flow** como estratégia de branching, mantendo
a branch `main` como branch principal.

Serão utilizadas **feature branches** para desenvolver novas
funcionalidades de forma isolada. Após a conclusão do desenvolvimento,
as alterações deverão ser integradas à branch de integração (**develop**) por meio de **Pull
Requests** para então, após aprovadas, serem integradas à branch principal também por meio de Pull Requests.

A pipeline de Integração Contínua (CI), configurada no **GitHub Actions**,
será executada automaticamente nos seguintes eventos da branch `main` e `develop`:

-   **Pull Request:** execução da pipeline para validar as alterações
    propostas antes da integração.
-   **Push:** execução da pipeline quando houver alterações enviadas
    diretamente à branch `main` ou `develop`, incluindo integrações realizadas após a
    aprovação dos Pull Requests.
