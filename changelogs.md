# Changelog

Todas as alterações relevantes deste projeto serão documentadas neste arquivo.

O formato segue o padrão **Keep a Changelog**.

---

# [1.0.0] - 2026-07-24

## 🎉 Primeira versão oficial

Primeira versão pública do SenSei.

---

## ✨ Adicionado

### Sistema de Ranking

- Ranking Geral
- Ranking Semanal
- Ranking Mensal
- Ranking Individual
- Contagem automática de tempo em canais de voz
- Exclusão do canal AFK
- Exclusão de bots
- Atualização automática do ranking
- Cargo automático para o vencedor
- Persistência em SQLite

---

### Sistema de Voice Tracker

- Registro automático de entrada em call
- Registro automático de saída
- Atualização periódica do tempo em voz
- Contagem apenas em canais permitidos

---

### Sistema de Reset

- Weekly Reset
- Monthly Reset
- Backup antes da limpeza
- Reset administrativo protegido por senha

---

### Sistema de Logs

#### Mensagens

- Registro de mensagens apagadas
- Registro de mensagens editadas

#### Voz

- Entrada em call
- Saída da call
- Movimentação entre canais

#### Auditoria

- Criação de canais
- Alteração de canais
- Exclusão de canais
- Criação de cargos
- Alteração de cargos
- Exclusão de cargos
- Alteração de apelidos
- Banimentos
- Desbanimentos
- Entrada de bots

---

### Eventos

- Sistema de boas-vindas
- Sistema de despedida
- Cargo automático para novos membros
- Mensagens aleatórias
- Painel público do servidor

---

### Embeds

- Padronização visual
- EmbedFactory
- Cores organizadas
- Campos auxiliares
- Thumbnail
- Footer personalizado

---

### Estrutura

Arquitetura completamente modular.

- Commands
- Events
- Managers
- Background
- Utils
- Embeds
- Database

---

## 🔧 Alterado

- Reformulação completa da arquitetura do projeto.
- Separação entre eventos públicos e logs administrativos.
- Migração dos logs para ANSI.
- Melhor organização dos comandos.
- Melhor gerenciamento de configurações.
- Tratamento centralizado de erros.
- Padronização dos horários para America/Sao_Paulo.
- Melhor organização do banco SQLite.

---

## 🛠 Corrigido

- Correção da contagem de tempo em call.
- Correção do reset semanal.
- Correção do reset mensal.
- Correção da atualização do ranking.
- Correção dos logs de mensagens apagadas.
- Correção dos logs de mensagens editadas.
- Correção dos logs de movimentação em voz.
- Correção da atribuição automática de cargos.
- Correção da hierarquia de cargos.
- Correção do fuso horário dos logs.
- Correção da inicialização dos Cogs.
- Correção de diversos problemas relacionados à sincronização dos Slash Commands.

---

## 📈 Estatísticas da versão

### Recursos implementados

- Sistema de Ranking
- Sistema de Logs
- Voice Tracker
- Welcome & Goodbye
- Reset Semanal
- Reset Mensal
- Painel Público
- Cargo Automático
- EmbedFactory
- SQLite
- Configuração centralizada

---

## 🚀 Próximas versões

Planejado para futuras versões:

- Dashboard Web
- API REST
- Sistema de Tickets
- AutoMod
- Sistema de Advertências
- PostgreSQL
- Multi Servidores
- Integração com IA