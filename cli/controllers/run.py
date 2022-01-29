import subprocess
import pathlib
from cement import Controller, ex
from ..core.path import getCurrentAbsPath, getExtPath, getNodeBinPath


class Run(Controller):
    class Meta:
        label = "run"
        stacked_on = "base"
        stacked_type = "embedded"

    @ex(
        help="Run command help",
        arguments=[
            (["command"], {"help": "Command name"}),
            (["extra"], {"help": "Extra arguments", "nargs": "*"}),
        ],
    )
    def run(self):
        """Run docstring"""

        subprocess.run(
            [
                getNodeBinPath("ts-node"),
                getExtPath("run.ts"),
                self.app.pargs.command,
                "--root",
                getCurrentAbsPath(),
                *self.app.pargs.extra,
            ]
        )
