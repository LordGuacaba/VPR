"""
VPR API tests
"""
from fastapi.testclient import TestClient
from src.main import app
from os import remove

client = TestClient(app)

def teardown():
    remove("src/output/expanded.pptx")

def test_hello_world():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}

# Create powerpoint - POST

def test_create_presentation_txt():
    response = client.post(
        '/create',
        files={'file': open('tests/data/testpacket.txt', 'rb')}
    )
    print(response.json())
    assert response.status_code == 201

    try:
        teardown()
        assert True
    except:
        assert False

def test_create_presentation_docx():
    response = client.post(
        '/create',
        files={'file': open('tests/data/testpacket.docx', 'rb')}
    )
    print(response.json())
    assert response.status_code == 201

    try:
        teardown()
        assert True
    except:
        assert False

def test_create_presentation_custom_name():
    pass

def test_create_presentation_bad_type():
    pass

def test_create_presentation_bad_format():
    pass

# Get presentation - GET

def test_get_presentation():

    pass

def test_get_presentation_missing():
    response = client.get('/presentation/badname')
    assert response.status_code == 404
    assert response.json() == {"detail": "No presentation with that name exists"}

# Delete presentation - DELETE

# Delete presentation preflight - OPTIONS

def test_preflight():
    response = client.options('/presentation/fakename')
    assert response.status_code == 204
    assert response.headers == {
        'Access-Control-Allow-Origin': 'http://localhost:3000',
        'Access-Control-Allow-Methods': 'POST, GET, DELETE, OPTIONS'
    }