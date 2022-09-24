from guardian import guard


def test_decorator_not_raises_if_zero_args():
    @guard.none()
    def function():
        return "Hi Everyone"

    function()
