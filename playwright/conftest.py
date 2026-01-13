from idlelib.rpc import request_queue

import pytest


@pytest.fixture(scope="session")
def user_credentials(request):
    return request.user_credentials