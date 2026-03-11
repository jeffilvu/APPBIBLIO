from flask import jsonify, request
from extensions import db
from models import Livro

def init_routes(app):
    #Consultar 
    @app.route('/livros',methods = ['GET'])
    def obter_livros():
        livros = Livro.query.all() # select * from livro
        return jsonify([livro.to_dict() for livro in livros])

    #consultar por id
    @app.route('/livros/<int:idEnviado>',methods = ['GET'])
    def obter_livro_por__id(idEnviado):
        livro = Livro.query.get(idEnviado) # select * from livro where id = idEnviado
        if livro:
            return jsonify(livro.to_dict())
        return jsonify({"mensagem": "Livro nao encontrado"}), 404


    #editar
    @app.route('/livros/<int:idEnviado>',methods = ['PUT'])  
    def editar_livro_por_id(idEnviado):
        livro = Livro.query.get(idEnviado) # select * from livro where id = idEnviado

        if not livro:
            return jsonify({"mensagem": "Livro nao encontrado"}), 404

        dados = request.get_json() #envia o json das novas infos do livro

        livro.titulo = dados.get('titulo', livro.titulo) #altera
        livro.autor = dados.get('autor', livro.autor)

        db.session.commit()

        return jsonify(livro.to_dict())


    # Criar
    @app.route('/livros',methods = ['POST'])  
    def incluir_novo_livro():
        dados = request.get_json()
        novo_livro = Livro(titulo=dados['titulo'], autor=dados['autor'])

        db.session.add(novo_livro) #insert
        db.session.commit()

        return jsonify(novo_livro.to_dict()), 201

    # excluir
    @app.route('/livros/<int:idEnviado>',methods = ['DELETE'])  
    def excluir_livro(idEnviado):
        livro = Livro.query.get(idEnviado) # select * from livro where id = idEnviado

        if livro:
            db.session.delete(livro)
            db.session.commit()
            return jsonify({"mensagem": "Livro excluído com sucesso"})
        return jsonify({"mensagem": "Livro não encontrado"}), 404

        