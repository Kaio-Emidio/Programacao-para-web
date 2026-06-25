from flask import flash, jsonify, redirect, render_template, request, url_for

from app import app
from app.controllers.paciente_controller import PacienteController
from app.forms import PacienteForm
from app.models import Consulta, Medico, Paciente
from app.models.base import ValidationError


MODELS = {
    "pacientes": Paciente,
    "medicos": Medico,
    "consultas": Consulta,
}


@app.route("/")
def index():
    return jsonify(
        {
            "mensagem": "API de CRUD com armazenamento em JSON",
            "recursos": sorted(MODELS),
        }
    )


@app.route("/pacientes/listar")
def listar_pacientes():
    pacientes = PacienteController().listar()
    return render_template("pacientes/listar.html", pacientes=pacientes)


@app.route("/pacientes/criar", methods=["GET", "POST"])
def criar_paciente():
    form = PacienteForm()

    if form.validate_on_submit():
        try:
            PacienteController().criar(form.to_dict())
            flash("Paciente cadastrado com sucesso.")
            return redirect(url_for("listar_pacientes"))
        except ValidationError as error:
            flash(str(error))

    return render_template(
        "pacientes/formulario.html",
        form=form,
        title="Cadastrar paciente",
        submit_label="Cadastrar",
    )