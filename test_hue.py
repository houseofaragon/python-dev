from distutils import errors
import pytest
from hue import get_hue_base_url

# with pytest.raises(SyntaxError):
def test_get_hue_base_url_run_time_error():
    assert get_hue_base_url() == 'http://192.168.1.5/api/KB75bFWzLxj101-8ZVeqrrAvs2utaAjEV43AkLmG'

