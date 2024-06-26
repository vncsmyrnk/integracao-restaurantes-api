from entities.models import Ingrediente


def test_ingrediente_get(client, session_scope):
    with session_scope() as session:
        pass

    response = client.get("/api/ingrediente")

    session.query.assert_called_once_with(Ingrediente)
    session.query().all.assert_called_once()
    assert response.status_code == 200


def test_ingrediente_get_by_id(client, session_scope):
    with session_scope() as session:
        pass

    ingrediente_to_search = Ingrediente(
        id=1, nome="Ingrediente", descricao="descricao"
    )
    session.add(ingrediente_to_search)

    response = client.get("/api/ingrediente/1")

    session.query.assert_called_once_with(Ingrediente)
    session.query().filter.assert_called_once()
    session.query().filter().first.assert_called_once()
    assert response.status_code == 200
    assert response.json["nome"] == "Ingrediente"
    assert response.json["descricao"] == "descricao"


def test_ingrediente_set(client, session_scope):
    with session_scope() as session:
        pass

    response = client.post(
        "/api/ingrediente",
        json={"nome": "Ingrediente", "descricao": "descricao", "medida": "kg"},
    )

    session.add.assert_called_once()
    session.commit.assert_called_once()
    session.refresh.assert_called_once()
    assert response.status_code == 200
    assert response.json["nome"] == "Ingrediente"
    assert response.json["descricao"] == "descricao"
    assert response.json["medida"] == "kg"


def test_ingrediente_set_without_unrequired(client, session_scope):
    with session_scope() as session:
        pass

    response = client.post(
        "/api/ingrediente", json={"nome": "Ingrediente", "medida": "l"}
    )

    session.add.assert_called_once()
    session.commit.assert_called_once()
    session.refresh.assert_called_once()
    assert response.status_code == 200
    assert response.json["nome"] == "Ingrediente"
    assert response.json["medida"] == "l"


def test_ingrediente_set_without_required(client):
    response = client.post("/api/ingrediente", json={})

    assert response.status_code == 400


def test_ingrediente_set_without_required_nome(client):
    response = client.post("/api/ingrediente", json={"medida": "kg"})

    assert response.status_code == 400


def test_ingrediente_set_without_required_medida(client):
    response = client.post("/api/ingrediente", json={"nome": "Ingrediente"})

    assert response.status_code == 400


def test_ingrediente_set_incorrect_medida(client):
    response = client.post(
        "/api/ingrediente",
        json={"nome": "Ingrediente", "medida": "t"},
    )

    assert response.status_code == 400


def test_ingrediente_delete(client, session_scope):
    with session_scope() as session:
        pass

    ingrediente_to_delete = Ingrediente(
        id=1, nome="Ingrediente", descricao="descricao", medida="un"
    )
    session.add(ingrediente_to_delete)

    response = client.delete("/api/ingrediente/1")

    session.query.assert_called_once_with(Ingrediente)
    session.query().filter().first.assert_called_once()
    session.commit.assert_called_once()
    session.delete.assert_called_once()
    assert response.status_code == 200
    assert response.json["nome"] == "Ingrediente"
    assert response.json["descricao"] == "descricao"
    assert response.json["medida"] == "un"
