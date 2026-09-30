# Executar o portfólio

Os projetos agora também têm repositórios independentes. Use os links do README e os comandos de cada projeto para obter sua versão atual. Os comandos abaixo continuam válidos para as cópias da primeira entrega neste repositório.

Pré-requisito: Python 3.11 ou superior. Os projetos usam apenas a biblioteca padrão. No Windows, use `py` se `python` não estiver disponível.

Baixe o repositório pelo botão Code → Download ZIP ou clone:

```bash
git clone https://github.com/DiogoLazzarotto/DiogoLazzarotto.git
cd DiogoLazzarotto
```

## Relatórios

```bash
cd projects/relatorios-producao-python
python src/report.py examples/producao.csv --start 2026-09-21 --end 2026-09-25 --output output
python -m unittest discover -s tests -v
```

Abra `output/relatorio.html`. Use Imprimir → Salvar como PDF no navegador. Volte à raiz antes do próximo projeto.

## SQL

```bash
cd projects/analise-logistica-sql
python demo.py
python -m unittest discover -s tests -v
```

O script cria o banco em memória e imprime consultas e resultados; não exige instalar SQLite separadamente.

## Planejamento de entregas

```bash
cd projects/planejamento-entregas
python server.py
```

Abra http://127.0.0.1:8000. O banco local é criado automaticamente com dados fictícios. Encerre com Ctrl+C. Para reiniciar a demonstração, pare o servidor e remova `planner.db` (isso apaga seus registros locais).

```bash
python -m unittest discover -s tests -v
```

## Página de portfólio

```bash
cd projects/portfolio-web
python -m http.server 8080 --bind 127.0.0.1
```

Abra http://127.0.0.1:8080. A página está pronta para hospedagem estática, mas hospedagem não faz parte do código.
