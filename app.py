from flask import Flask, render_template, request, redirect, url_for
from sqlalchemy import select
from database import Base, engine, SessionLocal
from models import User, Book
app = Flask(__name__)
Base.metadata.create_all(engine)
@app.route("/")
def index():
    with SessionLocal() as session:
        usuarios = session.scalars(
            select(User).order_by(User.nome)
        ).all()
        livros = session.scalars(
            select(Book).order_by(Book.titulo)
        ).all()
        return render_template(
            "index.html",
            usuarios=usuarios,
            livros=livros
        )
@app.route("/usuarios/novo", methods=["GET", "POST"])
def novo_usuario():
    if request.method == "POST":
        nome = request.form["nome"].strip()
        email = request.form["email"].strip()
        if not nome or not email:
            return "Preencha todos os campos.", 400
        with SessionLocal() as session:
            usuario = User(nome=nome, email=email)
            session.add(usuario)
            session.commit()
        return redirect(url_for("index"))
    return render_template("user_form.html")
@app.route("/livros/novo", methods=["GET", "POST"])
def novo_livro():
    with SessionLocal() as session:
        usuarios = session.scalars(
            select(User).order_by(User.nome)
        ).all()
        if request.method == "POST":
            titulo = request.form["titulo"].strip()
            user_id = request.form.get("user_id", type=int)
            usuario = session.get(User, user_id)
            if not titulo or usuario is None:
                return "Informe um título e selecione um usuário válido.", 400
            livro = Book(titulo=titulo, user=usuario)
            session.add(livro)
            session.commit()
            return redirect(url_for("index"))
        return render_template(
            "book_form.html",
            usuarios=usuarios
        )
if __name__ == "__main__":
    app.run(debug=True)