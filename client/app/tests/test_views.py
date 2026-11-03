def test_home_view(client):
    response = client.get("/")
    assert response.status_code == 200


def test_resume_view(client):
    response = client.get("/resume/")
    assert response.status_code == 200


def test_project_view(client):
    response = client.get("/project/")
    assert response.status_code == 200


def test_hermes_blog_view(client):
    response = client.get("/hermes/")
    assert response.status_code == 200
    assert b"How AI News gets onto the site." in response.data
    assert b'href="/hermes/"' in response.data


def test_404_view(client):
    response = client.get("/blah/")
    assert response.status_code == 404
