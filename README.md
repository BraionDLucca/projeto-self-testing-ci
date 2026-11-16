# Atividade Prática Avaliativa (Projeto Capstone)

**Tema do Projeto:** Construção de uma API de Microsserviço Financeiro com Automação CI, Suíte de Self-Testing Multinível e Estratégia de Branching.

## Escopo e Cenário do Sistema
Deverá ser desenvolvida uma API REST simplificada de conciliação bancária e
carteira digital (Wallet API) com as seguintes operações essenciais:

- Criação e consulta de contas digitais com saldo inicial.

- Transferência de saldo entre contas com tratamento de concorrência, saldo insuficiente e idempotência.

- Consulta de extrato com filtros por data e tipo de transação (débito/crédito).

- Integração com um serviço de gateway externo fictício (ex: envio de notificação anti-fraude via webhook).

## 2. Entregáveis Obrigatórios
```
projeto-self-testing-ci/
├── .github/
│   └── workflows/
│       └── ci.yml                  # Pipeline automatizado no GitHub Actions
├── src/
│   ├── domain/
│   ├── controllers/
│   ├── services/
│   └── repositories/
├── tests/
│   ├── unit/                       # Testes de lógica pura (TDD)
│   ├── integration/                # Testes com Mocks, Stubs e BD em memória
│   └── e2e/                        # Testes de ponta a ponta (Supertest / PyTest TestClient)
├── .env.example
├── Makefile ou package.json / requirements.txt
└── RELATORIO_TECNICO.md            # Documentação formal de requisitos e arquitetura
```