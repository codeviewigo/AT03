import pytest
from main import get_cat


def test_get_cat(mocker):
    mock_get = mocker.patch('main.requests.get')
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        'id': 'csl',
        'url': 'https://cdn2.thecatapi.com/images/csl.jpg',
        'width': 500,
        'height': 333
    }

    data = get_cat()

    assert data == {
        'id': 'csl',
        'url': 'https://cdn2.thecatapi.com/images/csl.jpg',
        'width': 500,
        'height': 333
    }


def test_get_cat_with_error(mocker):
    mock_get = mocker.patch('main.requests.get')
    mock_get.return_value.status_code = 503

    data = get_cat()

    assert data == None
