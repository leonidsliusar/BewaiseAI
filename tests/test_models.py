import datetime

import pytest

from app.core.models import Question


@pytest.mark.parametrize('data, expected_result', [({
                                                        "id": 183817,
                                                        "answer": "Italy",
                                                        "question": "foo",
                                                        "value": 200,
                                                        "airdate": "2017-01-13T20:00:00.000Z",
                                                        "created_at": "2022-12-30T21:23:14.600Z",
                                                        "updated_at": "2022-12-30T21:23:14.600Z",
                                                        "category_id": 5862,
                                                        "game_id": 5503,
                                                        "invalid_count": None,
                                                        "category": {
                                                            "id": 5862,
                                                            "title": "the 1860s",
                                                            "created_at": "2022-12-30T19:05:51.201Z",
                                                            "updated_at": "2022-12-30T19:05:51.201Z",
                                                            "clues_count": 20
                                                        }
                                                    }, {
                                                        "id": 183817,
                                                        "answer": "Italy",
                                                        "question": "foo",
                                                        "created_at": datetime.datetime.strptime(
                                                            "2022-12-30T21:23:14.600Z",
                                                            "%Y-%m-%dT%H:%M:%S.%fZ"
                                                        ).replace(tzinfo=datetime.timezone.utc),
                                                        }
                                                    )])
def test_serializeDB(data, expected_result):
    assert Question(**data).serializeDB.model_dump() == expected_result
