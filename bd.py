#importando sqlite
import sqlite3 as lite

#criando conexão
con = lite.connect('bddados.db')

#criando tabela de categoria
with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE Categoria(id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT)")


#criando tabela de receita
with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE Receita(id INTEGER PRIMARY KEY AUTOINCREMENT, categoria TEXT, adicionado_em DATE, valor DECIMAL)")


#criando tabela de gastos
with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE Gasto(id INTEGER PRIMARY KEY AUTOINCREMENT, categoria TEXT, retirado_em DATE, valor DECIMAL)")
