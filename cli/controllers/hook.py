import subprocess
import pathlib
from ..core.path import getNodeBinPath, getCurrentAbsPath
from cement import Controller, ex


class Hook(Controller):
    class Meta:
        label = "hook"
        stacked_on = "base"
        stacked_type = "embedded"

    @ex(
        help="Hook command help",
        arguments=[
          (
            ["path"],
            {
              "help": "Hook path",
              "default": ".",
              "nargs": "?",
              "type": pathlib.Path
            }
          ),
          (
            ["-I", "--install"],
            {
              "help": "Install git hooks",
              "action": "store_true",
              "dest": "install"
            }
          )
        ]
      )
    def hook(self):
        """Hook docstring"""

        path = self.app.pargs.path

        if self.app.pargs.install is True:
          subprocess.run([getNodeBinPath("husky"), "install"], cwd=getCurrentAbsPath(path))

        self.app.log.info("Hook command executed.")
