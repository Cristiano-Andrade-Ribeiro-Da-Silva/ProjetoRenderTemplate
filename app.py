from flask import Flask, render_template, request, redirect
from data import listas_configuracao as listas
import random

app = Flask(__name__)

# Aqui está todas as minhas rotas

@app.route("/")
def pagina_principal():
    cores = random.choice(listas.lista_cores)
    curiosidade = random.choice(listas.lista_curiosidades)
    return render_template("principal.html", cores_html = cores, curiosidade_html = curiosidade)


@app.route("/sobre")
def pagina_sobre():
    cor = random.choice(listas.lista_cores)
    curiosidade = random.choice(listas.lista_curiosidades)
    img = random.choice(listas.lista_img)
    return render_template("sobre.html", cor_html = cor,  curiosidade_html = curiosidade, img_html = img)


@app.route("/cadastro")
def pagina_cadastro():
    return render_template("cadastro.html", frases_html = listas.lista_curiosidades)


@app.route("/post/cadastrarfrase", methods=["POST"])
def post_cadastrarfrase():
    frases_html = request.form.get("frase")
    listas.lista_curiosidades.append(frases_html)
    return redirect ("/cadastro")



@app.route("/cadastrocores", methods=["GET"])
def pag_cores():
    return render_template("lista-cores.html", lista_cores_html = listas.lista_cadastro_cor)


@app.route("/post/cadastrarcor", methods=["POST"])
def post_cadastrarcor():
    cor_html = request.form.get("cores")
    listas.lista_cadastro_cor.append(cor_html)
    return redirect("/cadastrocores")


@app.route("/cores/delete/<indice_cor>", methods=["GET"])
def delete_cores(indice_cor):
    # converte o 'indece_cor' para um numero inteiro pois estava em string
    indice_cor = int(indice_cor)
    #exclui a cor da lista através do indice
    listas.lista_cadastro_cor.pop(indice_cor)
    return redirect("/cadastrocores")


app.run(debug= True)