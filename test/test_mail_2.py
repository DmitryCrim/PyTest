import pytest

@pytest.fixture()
def set_up():
    print('Вход выполнен')

def test_sending_mail_1():
    print('Письмо отправлено')


def test_sending_mail_2():
    print('Письмо отправлено')
