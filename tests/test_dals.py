from app.core.dals import DBManager


async def test_create(setup_and_teardown_db, question):
    # question.serializeDB.obj)
    assert await DBManager().create(question, setup_and_teardown_db) == []
    assert await DBManager().create(question, setup_and_teardown_db) == []
