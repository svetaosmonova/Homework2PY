import requests

base_url = "https://ru.yougile.com"
token = ""

headers = {
     "Content-Type": "application/json",
      "Authorization": f"Bearer {token}"
}


def test_create_projects():
    payload = {
        "title": "ГосУслуги"
    }

    response = requests.post(base_url + '/api-v2/projects',  json=payload, headers=headers)
    assert response.status_code == 201

def test_edit():
    payload = {
        "title": "ГосУслуги"
    }

    response = requests.post(base_url + '/api-v2/projects', json=payload, headers=headers)
    assert response.status_code == 201

    payload = {
        "deleted": False,
        "title": "МФЦ"
    }

    id = response.json()["id"]
    response = requests.put(base_url + f'/api-v2/projects/{id}', json=payload, headers=headers)

    # Проверка успешного изменения проекта
    assert response.status_code == 200, "Проект не был успешно изменён"


def test_get_projects():
    payload = {
        "title": "ГосУслуги"
    }

    response = requests.post(base_url + '/api-v2/projects', json=payload, headers=headers)
    id = response.json()["id"]
    assert response.status_code == 201

    response = requests.get(base_url + f'/api-v2/projects/{id}', headers=headers)
    assert response.status_code == 200


def test_negative_create_projects():
    payload = {
        "title": ""
    }

    response = requests.post(base_url + '/api-v2/projects',  json=payload, headers=headers)
    assert response.status_code == 400


def test_edit_negative():
    payload = {
        "title": "ГосУслуги"
    }

    response = requests.post(base_url + '/api-v2/projects', json=payload, headers=headers)
    assert response.status_code == 201

    payload = {
        "deleted": False,
        "title": "МФЦ"
    }

    id = 123
    response = requests.put(base_url + f'/api-v2/projects/{id}', json=payload, headers=headers)

    # Проверка успешного изменения проекта
    assert response.status_code == 404, "Проект не был успешно изменён"


def test_negative_get_projects():

    id = 123

    response = requests.get(base_url + f'/api-v2/projects/{id}', headers=headers)
    assert response.status_code == 404
