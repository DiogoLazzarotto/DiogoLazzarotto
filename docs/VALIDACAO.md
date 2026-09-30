# Validação da entrega

Verificado em 30/09/2026 com Python 3.12 e Node.js 24.

- 18 testes unitários de regras aprovados (`python verify.py`).
- Consultas SQL executadas e comparadas com resultados documentados.
- Relatório HTML e JSON gerados a partir do CSV de exemplo.
- Sintaxe dos dois arquivos JavaScript verificada com `node --check`.
- Integração HTTP do planejador: cadastro, viagem, atribuição, excesso de carga (400), entrega, desplanejamento e leitura do estado.
- Arquivos HTML/CSS/JS servidos corretamente; banco fora da raiz pública (404).
- Persistência confirmada ao fechar conexões e reabrir o banco.

## Verificação ainda pendente

Inspeção visual do planejador, interação por teclado e teste em tela móvel. A página de portfólio foi publicada no GitHub Pages, inspecionada visualmente em desktop e seus três filtros foram verificados em 30/09/2026. Layout responsivo e recursos semânticos foram implementados, mas a inspeção visual não foi executada neste ambiente. Não houve validação com usuários ou medição de produtividade.

## Roteiro de revisão pessoal

1. Execute todos os projetos pelo guia START_HERE.
2. Confirme o resultado de 145 t no relatório.
3. Crie uma viagem e planeje pedidos até o limite.
4. Tente enviar pedido que ultrapasse capacidade via API e observe rejeição.
5. Reabra o planejador e confira persistência.
6. Confira filtros do portfólio, largura móvel e navegação com Tab.
7. Estude as decisões e explique as limitações sem atribuir resultados fictícios à operação real.
