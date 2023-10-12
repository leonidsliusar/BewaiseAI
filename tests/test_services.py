from app.core.services import execute_task


async def test_execute_task(mocker, mock_fetch, mock_add, question):
    mocker.patch("app.core.services._fetch_question", return_value=mock_fetch)
    mocker.patch("app.core.services._add_question", return_value=mock_add)
    assert await execute_task(..., ...) == question.serializeDB.obj
