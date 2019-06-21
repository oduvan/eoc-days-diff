from checkio_referee import RefereeRank, ENV_NAME



import settings_env
from tests import TESTS


class Referee(RefereeRank):
    TESTS = TESTS
    ENVIRONMENTS = settings_env.ENVIRONMENTS

    DEFAULT_FUNCTION_NAME = "days_diff"
    FUNCTION_NAMES = {
        "python_3": "days_diff",
        "js_node": "daysDiff"
    }
    ENV_COVERCODE = {
        ENV_NAME.PYTHON: '''
def cover(f, data):
    return f(tuple(data[0]), tuple(data[1]))
''',
            ENV_NAME.JS_NODE: '''

function cover(func, in_data) {
    return func.apply(this, in_data)
}

    '''
    }