import json

from hamcrest import assert_that, equal_to, has_entries


class TestRoot:
    def test_read_root(self, client):
        response = client.get("/")
        response_object = json.loads(response.text)
        assert_that(response.status_code, equal_to(200), f"status code was {response.status_code}")
        expected = {
            "message": "Welcome to UrFU ML Engineering 2022, Group 20 project",
            "practice": "Practice 4 - Fast API with tests",
            "git_hub_back": "https://github.com/URFU-2022-machine-learning-engineering/sentiment_prediction_backend",
            "git_hub_front": "https://github.com/urfuMagDS2022SFgroup/streamlit_frontend",
            "authors": [
                "Vladimir Katin",
                "Anton Bessolitsyn",
                "Alexander Orlov",
                "Anna Bezhenar",
            ],
        }
        assert_that(response_object, has_entries(expected), f"expected {expected} but got {response_object}")
