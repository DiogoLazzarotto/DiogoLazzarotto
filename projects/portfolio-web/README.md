# Portfólio web

Página estática responsiva em HTML/CSS/JavaScript, com apresentação, três projetos, filtro por área e links para código. Sem frameworks, rastreadores ou recursos externos. Projeto demonstrativo.

## Executar

```bash
python -m http.server 8080 --bind 127.0.0.1
```

Abra http://127.0.0.1:8080. Alternativamente, abra `index.html` diretamente. O filtro é executado no navegador.

## Decisões

Paleta grafite, azul e ciano; tipografia do sistema; layout responsivo. Estrutura semântica, idioma declarado, foco visível, botões com `aria-pressed` e resultado de filtro com anúncio acessível. Os números nos cards são exemplos fictícios, não métricas profissionais.

## Limites

Links apontam para os projetos no repositório de perfil. A página não hospeda os servidores Python. Não há formulário de contato nem dados pessoais inventados. Publicar os arquivos estáticos exige configurar um provedor; nenhum endereço de site publicado é presumido.
