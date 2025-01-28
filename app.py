from flask import Flask, render_template
import random

app = Flask(__name__)

# Aqui está todas as minhas rotas

lista_cores_fundo = ["red",
                     "blue",
                     "green",
                     "#00ff00",
                     "#00ffff",
                     "#555555"]

lista_conquistas = [
    "Através de substâncias químicas liberadas pelas raízes e folhas, as plantas podem se comunicar, alertando sobre pragas, enviando sinais de perigo ou até mesmo cooperando para a sobrevivência mútua.",
                    
    " As raízes das plantas desempenham um papel fundamental na busca por água e nutrientes. Algumas raízes podem se estender por distâncias incríveis e formar complexas redes subterrâneas.",

    "Experimentos demonstraram que algumas plantas podem 'lembrar'de condições de estresse, como seca ou ataque de pragas, e desenvolver mecanismos de defesa mais eficientes em futuras situações semelhantes.",

    "O solo é um ecossistema vibrante, repleto de microrganismos que formam relações simbióticas com as plantas. Bactérias fixadoras de nitrogênio, por exemplo, fornecem nutrientes essenciais para o crescimento das plantas."]

@app.route("/sobre")
def pagina_sobre():
    cores = random.choice(lista_cores_fundo)
    conquistas = random.choice(lista_conquistas)
    return render_template("sobre.html", cores_html = cores,  conquistas_html = conquistas)






app.run(debug= True)