from authentication_page import admin_page


def test_admin_page():
    page = admin_page(name="admin", password="1234")
    assert page == "Authentication Successful"


def test_admin_page_invalid():
    page = admin_page(name="user", password="1234")
    assert page == "Authentication Failed"