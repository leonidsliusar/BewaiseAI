from app.core.dals import DBManager


async def test_create(setup_and_teardown_db, question):
    obj = await DBManager().create(question, setup_and_teardown_db)
    assert [item.model_dump() for item in obj] == [item.model_dump() for item in question.serializeDB.obj]
    assert await DBManager().create(question, setup_and_teardown_db) == []
