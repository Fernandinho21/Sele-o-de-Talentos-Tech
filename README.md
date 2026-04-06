<<<<<<< HEAD
# 🍔 Sistema de Lanchonete

Pequena aplicação Python que simula as regras de negócio de uma lanchonete, desenvolvida para fins educacionais com foco em testes unitários automatizados.

---

## 📁 Estrutura do Projeto

```
lanchonete/
├── cardapio.py          # Gerenciamento do cardápio
├── carrinho.py          # Carrinho de pedidos e cupons de desconto
├── entrega.py           # Cálculo da taxa de entrega
├── test_lanchonete.py   # Testes unitários (Pytest)
└── README.md
```

---

## ▶️ Como Executar

### Pré-requisitos
- Python 3.8+
- pytest
- pytest-cov

### Instalação das dependências
```bash
pip install pytest pytest-cov
```

### Rodar os testes
```bash
cd lanchonete
pytest test_lanchonete.py -v
```

### Rodar com relatório de cobertura
```bash
pytest test_lanchonete.py -v --cov=. --cov-report=term-missing
```

---

## 📋 Regras de Negócio Testadas

### 1. Cardápio (`cardapio.py`)

| Regra | Comportamento |
|---|---|
| Nome do item não pode ser vazio ou só espaços | Lança `ValueError` |
| Preço deve ser maior que zero | Lança `ValueError` |
| Categoria deve ser `lanche`, `bebida` ou `sobremesa` | Lança `ValueError` se inválida |
| Não pode cadastrar item com nome duplicado | Lança `ValueError` |
| Busca por item inexistente | Lança `KeyError` |
| Remoção de item inexistente | Lança `KeyError` |

---

### 2. Carrinho de Pedidos (`carrinho.py`)

| Regra | Comportamento |
|---|---|
| Quantidade adicionada deve ser >= 1 | Lança `ValueError` |
| Item deve existir no cardápio para ser adicionado | Lança `KeyError` |
| Adicionar o mesmo item duas vezes acumula a quantidade | Soma as quantidades |
| Não é possível remover mais do que a quantidade no carrinho | Lança `ValueError` |
| Remover item com quantidade resultante 0 o exclui do carrinho | Remove automaticamente |
| Subtotal = soma de (preço × quantidade) de todos os itens | Cálculo correto |
| Cupom `LANCHE10` aplica 10% de desconto no subtotal | Retorna valor do desconto |
| Cupom `LANCHE20` aplica 20% de desconto no subtotal | Retorna valor do desconto |
| Cupom inválido ou inexistente | Lança `ValueError` |
| Total = subtotal − desconto + taxa de entrega | Total nunca negativo |

**Cupons válidos:**
| Código | Desconto |
|---|---|
| `LANCHE10` | 10% no subtotal |
| `LANCHE20` | 20% no subtotal |
| `FRETE0` | Sem desconto (uso futuro para frete grátis) |

---

### 3. Taxa de Entrega (`entrega.py`)

| Distância | Taxa |
|---|---|
| Até 2 km | Grátis (R$ 0,00) |
| De 2,01 km até 5 km | R$ 5,00 |
| De 5,01 km até 10 km | R$ 10,00 |
| Acima de 10 km | Entrega não disponível → Lança `ValueError` |
| Distância zero ou negativa | Lança `ValueError` |

---

## ✅ Cobertura de Testes

Execute o comando abaixo para gerar o relatório de cobertura:

```bash
pytest test_lanchonete.py --cov=. --cov-report=term-missing
```

O projeto conta com **+30 testes unitários** cobrindo cenários válidos e inválidos de todas as regras de negócio.
=======
# Sele-o-de-Talentos-Tech
avaliação facultativa 
>>>>>>> 57b28494d89cac61b7446b3f6c1515d1e6993e98
![covarge](https://github.com/user-attachments/assets/a2b65809-92c9-4ea4-ab5c-1c897f06d835)
