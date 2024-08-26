"""
VPR API tests
"""
from fastapi.testclient import TestClient
from src.main import app
import os

client = TestClient(app)

def create_setup():
    with open('src/output/testname.pptx', 'w') as file:
        file.write("Test")

def assert_file_exists(filename: str="testname", delete: bool=True):
    filepath = f'src/output/{filename}.pptx'
    assert os.path.isfile(filepath)
    if delete:
        os.remove(filepath)

# Tests

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
    assert_file_exists("expanded")

def test_create_presentation_docx():
    response = client.post(
        '/create',
        files={'file': open('tests/data/testpacket.docx', 'rb')}
    )
    assert response.status_code == 201
    assert_file_exists("expanded")

def test_create_presentation_custom_name():
    response = client.post(
        '/create?name=ritquizbowl',
        files={'file': open('tests/data/testpacket.docx', 'rb')}
    )
    assert response.status_code == 201
    assert_file_exists(filename='ritquizbowl') 

def test_create_presentation_bad_type():
    response = client.post(
        '/create?name=ritquizbowl',
        files={'file': open('tests/test_main.py', 'rb')}
    )

    assert response.status_code == 400
    assert response.json() == {'detail': 'File must be a plain text file or Word document'}

def test_create_presentation_bad_format():
    pass

# Get presentation - GET

def test_get_presentation():
    create_setup()
    response = client.get('/presentation/testname')

    assert response.status_code == 200
    assert response.headers['Content-Disposition'] == 'attachment'
    assert response.headers['Content-Type'] == 'application/vnd.openxmlformats-officedocument.presentationml.presentation'
    assert_file_exists(filename='testname')

def test_get_presentation_missing():
    response = client.get('/presentation/badname')
    assert response.status_code == 404
    assert response.json() == {"detail": "No presentation with that name exists"}

# Delete presentation - DELETE

def test_delete_presentation():
    create_setup()
    assert_file_exists(delete=False)
    response = client.delete('/presentation/testname')

    assert response.status_code == 200
    assert not os.path.isfile('src/output/testname.pptx')

def test_delete_presentation_missing():
    create_setup()
    response = client.delete('/presentation/badname')

    assert response.status_code == 404
    assert response.json() == {"detail": "No presentation with that name exists"}
    assert_file_exists()

# Delete presentation preflight - OPTIONS

def test_preflight():
    response = client.options('/presentation/fakename')
    assert response.status_code == 204
    assert response.headers == {
        'Access-Control-Allow-Origin': 'http://localhost:3000',
        'Access-Control-Allow-Methods': 'POST, GET, DELETE, OPTIONS'
    }