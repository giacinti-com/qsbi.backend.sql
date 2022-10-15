import os
import sqlite3
from pathlib import Path
from typing import Generator

import pytest

from qsbi.backend.sql.seq_session import get_session

TEST_DIR: str = os.path.dirname(os.path.abspath(__file__))


@pytest.fixture(scope="session")
def example_dump() -> str:
    return f"{TEST_DIR}/example.sql"


@pytest.fixture(scope="session")
def example_json() -> str:
    return f"{TEST_DIR}/example.json"


@pytest.fixture(scope="session")
def reference_db(tmp_path_factory, example_dump) -> Path:
    ref_db: Path = tmp_path_factory.mktemp("data") / "example.db"
    with sqlite3.connect(ref_db) as conn:
        with open(example_dump) as file:
            conn.cursor().executescript(file.read())
    return ref_db


@pytest.fixture(scope="session", autouse=True)
def mock_db_url(session_mocker, reference_db) -> None:
    session_mocker.patch("qsbi.backend.sql.seq_session.get_qsbi_url", return_value=f"sqlite:///{reference_db}")


@pytest.fixture(scope="session")
def get_test_session(mock_db_url) -> Generator:
    sess = get_session()
    try:
        yield sess
    finally:
        sess.close()
