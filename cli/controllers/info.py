from cement import Controller, ex


class Info(Controller):
    class Meta:
        label = "info"
        stacked_on = "base"
        stacked_type = "embedded"

    @ex(help="Info command help")
    def info(self):
        """Info docstring"""

        headers = ["NAME", "AGE", "ADDRESS"]
        data = [
            ["Krystin Bartoletti", 47, "PSC 7591, Box 425, APO AP 68379"],
            ["Cris Hegan", 54, "322 Reubin Islands, Leylabury, NC 34388"],
            ["George Champlin", 25, "Unit 6559, Box 124, DPO AA 25518"],
        ]

        self.app.render(
            data,
            headers=headers,
            handler="tabulate",
            tablefmt="grid",
            numalign="left",
            stralign="left",
        )
