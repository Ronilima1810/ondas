# Wave Control · Warehouse Operations

**Frontend Next.js/TypeScript de planejamento e controle de ondas de separação.**

O projeto passou de uma estrutura vazia para um frontend demonstrativo editável, com interface de software corporativo orientado a armazéns. Os exemplos de ondas, operadores, prioridades, horários e volumetria são inventados.

## Funcionalidades

- Painel executivo com totais de ondas, pedidos, unidades e andamento.
- Gestão visual de ondas com status *Planejada → Liberada → Aguardando impressão → Em separação → Conferência → Concluída*.
- Mudança simulada de etapa, preservada somente na sessão do navegador.
- Comparativos de pedidos por canal e filas por situação.
- Pesquisa, filtro de status e exportação CSV.
- Guia de processos, arquitetura e limites da demonstração.

## Tecnologias

| Camada | Ferramentas |
| --- | --- |
| Interface | Next.js 15.5.28, React 19, TypeScript |
| Ícones e layout | Lucide React, CSS customizado responsivo |
| API conceitual | FastAPI + Pydantic |
| Dados | Fixtures totalmente fictícias, sem WMS |
| Verificação | Build TypeScript e testes sintéticos via GitHub Actions |

## Executar interface

```bash
cd frontend
npm install
npm run dev
```

O sistema funciona com os dados sintéticos incorporados. Para gerar o build de produção do frontend: `npm run build`.

## API de demonstração

```bash
python3 -m pip install -r backend/requirements.txt
uvicorn backend.main:app --host 127.0.0.1 --port 8000
```

Endpoints: `GET /api/health` e `GET /api/waves`. O frontend atual é uma demonstração local independente; ainda não consome essa API automaticamente.

## Atenção

**Este não é um WMS de produção.** Não realiza importação real, separação física, emissão fiscal, agendamento ou movimentação de estoque, nem consulta dados empresariais. O backend de produção requer autenticação, perfis, persistência, filas de tarefas, auditoria e contratos reais de integração.

O código-fonte pode ser compilado e estudado sem banco de dados ou credenciais. A versão pública foi concebida para demonstrar UX, arquitetura e evolução de um produto full-stack.
