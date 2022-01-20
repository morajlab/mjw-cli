import subprocess
import pathlib
from cement import Controller, ex
from ..core.cache import Cache
from ..core.path import (
    getNodeBinPath,
    getTemplatePath,
    getCurrentAbsPath,
    getProjectAbsPath,
)


class Lint(Controller):
    class Meta:
        label = "lint"
        stacked_on = "base"
        stacked_type = "embedded"

    @ex(
        help="Lint command help",
        arguments=[
            (
                ["input"],
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
                    "help": "Linter type",
                    "choices": ["stylelint", "commitlint"],
                    "action": "store",
                    "dest": "type",
                },
            ),
        ],
    )
    def lint(self):
        """Lint docstring"""

        linter_type = self.app.pargs.type
        input_content = self.app.pargs.input

        data = {"node_modules_path": getProjectAbsPath("node_modules")}
        cache = Cache(key=getCurrentAbsPath())
        cache.create("lint")

        self.app.mjw.template.renderTo(
            getTemplatePath("lint"), cache.getPath("lint"), data, force=True
        )

        if linter_type is None or linter_type == "stylelint":
            input_array = []

            if type(input_content) is list:
                for i in input_content:
                    input_array.append(getCurrentAbsPath(i))
            else:
                input_array.append(getCurrentAbsPath(input_content))

                subprocess.run(
                    [
                        getNodeBinPath("stylelint"),
                        "--config",
                        cache.getPath("lint", ".stylelintrc.json"),
                        *input_array,
                    ],
                    check=True,
                )

        if linter_type is None or linter_type == "commitlint":
            subprocess.run(
                [
                    getNodeBinPath("commitlint"),
                    "--config",
                    cache.getPath("lint", "commitlint.config.js"),
                    "--edit",
                    *input_content,
                ],
                check=True,
            )

        self.app.log.info("Linter executed.")
