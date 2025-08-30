from test.util.abstract_integration_test import (
    AbstractIntegrationTest,
    get_fast_api_client,
)


class TestBMI(AbstractIntegrationTest):
    BASE_PATH = "/bmi"

    @classmethod
    def setup_class(cls):
        super().setup_class()
        cls.fast_api_client = get_fast_api_client()

    def test_calculate_bmi(self):
        response = self.fast_api_client.post(
            self.create_url(""),
            json={
                "weight_kg": 70,
                "height_m": 1.75,
                "age": 30,
                "gender": "male",
                "pregnant": False,
                "athlete": False,
                "waist_cm": 80,
                "lang": "es",
            },
        )
        assert response.status_code == 200
        data = response.json()
        assert data["bmi"] == round(70 / (1.75**2), 2)
        assert data["category"] == "Peso normal"
        assert data["group"] == "Adulto"

    def test_missing_fields(self):
        response = self.fast_api_client.post(
            self.create_url(""),
            json={"height_m": 1.8, "age": 25, "gender": "male"},
        )
        assert response.status_code == 422
