from cement import Controller, ex


class Test(Controller):
    class Meta:
        label = "test"
        stacked_on = "base"
        stacked_type = "embedded"

    @ex(help="Test command help")
    def test(self):
        """Test docstring"""

        self.app.log.info("Test command executed.")
