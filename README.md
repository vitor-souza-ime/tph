# TPH: Visualização Computacional de Superfícies — Toroide, Paraboloide e Hiperboloide

Este projeto tem como objetivo apresentar, por meio de recursos computacionais em Python, a visualização tridimensional de superfícies clássicas da Geometria Analítica: **Toroide**, **Paraboloide de Revolução**, **Hiperboloide de Uma Folha** e **Hiperboloide de Duas Folhas**.

A proposta visa apoiar o ensino e a aprendizagem de superfícies de revolução através da modelagem matemática e plotagem gráfica em 3D.

## Demonstração das Superfícies

As superfícies geradas são:

- 🔵 **Toroide**
- 🔺 **Paraboloide de Revolução**
- 🌀 **Hiperboloide de Uma Folha**
- 🧿 **Hiperboloide de Duas Folhas**

As figuras são renderizadas usando `matplotlib` com projeção tridimensional.

## Estrutura do Projeto

```

tph/
├── main.py          # Script principal com funções de plotagem
├── README.md        # Este arquivo

````

## Requisitos

- Python 3.8 ou superior
- numpy
- matplotlib

### Instalação

Clone o repositório e instale os pacotes necessários:

```bash
git clone https://github.com/vitor-souza-ime/tph.git
cd tph
pip install -r requirements.txt
````

*Você também pode instalar manualmente:*

```bash
pip install numpy matplotlib
```

## Como Executar

No terminal, dentro da pasta do projeto, execute:

```bash
python main.py
```

O script exibirá quatro superfícies 3D em sequência.

## Objetivos Educacionais

Este projeto pode ser utilizado em disciplinas como:

* Geometria Analítica
* Cálculo Vetorial
* Cálculo Diferencial e Integral III
* Modelagem Matemática
* Computação Gráfica Educacional

## Licença

Este projeto é licenciado sob a [MIT License](LICENSE).
