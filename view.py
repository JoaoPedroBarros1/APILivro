from flask import Flask, jsonify, request
from main import app, db
from models import Livro


@app.route("/livro", methods=['GET'])
def get_livro():
    livros = Livro.query.all()
    livros_dic = []
    for livro in livros:
        livro_dic = {
            'id_livro': livro.id_livro,
            'titulo': livro.titulo,
            'autor': livro.autor,
            'ano_publicacao': livro.ano_publicacao
        }
        livros_dic.append(livro_dic)

    return jsonify(
        mensagem='Lista de Livros',
        livros=livros_dic
    )


@app.route('/livro', methods=['POST'])
def post_livro():
    livro = request.json
    novo_livro = Livro(
        id_livro=livro.get('id_livro'),
        titulo=livro.get('titulo'),
        autor=livro.get('autor'),
        ano_publicacao=livro.get('ano_publicacao')
    )

    db.session.add(novo_livro)
    db.session.commit()

    return jsonify(
        mensagem='Livro Cadastrado com Sucesso',
        livro={
            'id_livro': novo_livro.id_livro,
            'titulo': novo_livro.titulo,
            'autor': novo_livro.autor,
            'ano_publicacao': novo_livro.ano_publicacao
        }
    )
