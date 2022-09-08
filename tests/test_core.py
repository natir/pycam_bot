import pycam_bot


def test_import_package() -> None:
    assert isinstance(pycam_bot.__all__, list)
