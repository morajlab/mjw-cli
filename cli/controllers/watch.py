from cement import Controller, ex


class Watch(Controller):
    class Meta:
        label = "watch"
        stacked_on = "base"
        stacked_type = "embedded"

    @ex(help="Watch command help")
    def watch(self):
        """Watch docstring"""

        print("This is watch command")
