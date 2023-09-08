import pytest

from unittest import mock
from faker import Faker
from requests.exceptions import HTTPError
from src.tool_manager import geocoding
from tools.constants import (
    ADDRESS_COMPONENTS_LITERAL_STR,
    FORMATTED_ADDRESS_LITERAL_STR,
    GEOMETRY_LITERAL_STR,
    PLACE_ID_LITERAL_STR,
    SUCCESSFUL_RESPONSE_DICT,
    TYPES_LITERAL_STR,
)

fake: Faker = Faker()


class TestToolManager:
    def test_geocoding(self):
        ST_TEST: int = fake.pyint(100, 5000, 100)
        ADDRESS_TEST: str = fake.address()

        mock_function = mock.create_autospec(
            geocoding, return_value=SUCCESSFUL_RESPONSE_DICT, spec_set=True
        )

        result: dict = mock_function(st=ST_TEST, address=ADDRESS_TEST)
        keys_list: list = [
            ADDRESS_COMPONENTS_LITERAL_STR,
            FORMATTED_ADDRESS_LITERAL_STR,
            GEOMETRY_LITERAL_STR,
            PLACE_ID_LITERAL_STR,
            TYPES_LITERAL_STR,
        ]

        assert sorted(result.keys()) == sorted(keys_list)

    @pytest.mark.parametrize(
        "st,address,msg_error",
        [("0", None, "400"), (None, "0", "400"), (None, None, "400")],
    )
    def test_geoconding_with_error(self, st, address, msg_error):
        mock_function = mock.create_autospec(
            geocoding, return_value=None, spec_set=True, side_effect=HTTPError(400)
        )
        mock.MagicMock()
        with pytest.raises(HTTPError) as exe:
            mock_function(st=st, address=address)
        assert msg_error in str(exe.value)
