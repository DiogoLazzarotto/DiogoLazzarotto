# Organização e decisões

Os quatro projetos possuem repositórios independentes. Este repositório de perfil contém a apresentação e documentação geral. As cópias em `projects/` preservam a primeira entrega; novas alterações devem ocorrer nos repositórios próprios, ligados no README.

## Decisões

- Python: biblioteca padrão nos projetos locais e openpyxl opcional para importar XLSX.
- CSV/XLSX: importação com validação compartilhada e pesos Decimal no projeto de relatórios.
- Decimal: evitar erros de ponto flutuante nos totais de produção.
- SQLite: banco relacional local, restrições e transações, sem servidor externo.
- API + HTML/CSS/JS: separar regras do servidor e apresentação; validação no servidor.
- Interface grafite com azul/ciano, responsiva e controles com rótulos.

## Escopo e honestidade

Dados, produtores e veículos são fictícios. Não há alegação de uso empresarial, produtividade medida ou domínio profissional de todas as tecnologias demonstradas. O autor deve executar, estudar e adaptar o código antes de apresentá-lo em uma entrevista.

## Evolução

1. Importação XLSX implementada e testada; exportação PDF direta permanece no backlog.
2. Autenticação e implantação segura do planejador.
3. Repositórios independentes criados e fixados no perfil em 30/09/2026.
4. Adição de métricas após medir uma rotina real autorizada.

Não incluir dados comerciais reais, credenciais ou informações pessoais nos exemplos.
