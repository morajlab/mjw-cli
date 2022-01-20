import subprocess
import pathlib
from cement import Controller, ex
from ..core.path import getNodeBinPath, getPipEnvBinPath, getCurrentAbsPath


class Format(Controller):
    class Meta:
        label = "format"
        stacked_on = "base"
        stacked_type = "embedded"

    @ex(
        help="Format command help",
        arguments=[
            (
                ["path"],
                {
                    "help": "[file/dir/glob ...]",
                    "default": ".",
                    "nargs": "*",
                    "type": pathlib.Path,
                },
            ),
            (
                ["-t", "--type"],
                {
                    "help": "Formatter type",
                    "choices": ["prettier", "black"],
                    "action": "store",
                    "dest": "type",
                },
            ),
            (
                ["-w", "--watch"],
                {
                    "help": "Watch mode",
                    "action": "store_true",
                    "dest": "watch",
                },
            ),
        ],
    )
    def format(self):
        """Format docstring"""

        formatter_type = self.app.pargs.type
        path = self.app.pargs.path
        path_array = []

        if type(path) is list:
            for p in path:
                path_array.append(getCurrentAbsPath(p))
        else:
            path_array.append(getCurrentAbsPath(path))

        if formatter_type is None or formatter_type == "prettier":
            subprocess.run(
                [
                    getNodeBinPath("prettier"),
                    "--write",
                    "--ignore-unknown",
                    *path_array,
                ],
                check=True,
            )

        if formatter_type is None or formatter_type == "black":
            subprocess.run([getPipEnvBinPath("black"), *path_array])

        self.app.log.info("Formatter executed.")
