import os
import subprocess
from cement import Controller, ex
from ..core.cache import Cache
from ..core.path import (
    getTemplatePath,
    getCachePath,
    getCurrentAbsPath,
    getProjectAbsPath,
    getNodeBinPath,
)


class Story(Controller):
    class Meta:
        label = "story"
        stacked_on = "base"
        stacked_type = "embedded"

    @ex(help="Story command help")
    def story(self):
        """Story docstring"""

        cwd = getCurrentAbsPath()
        dest_story_path = getCurrentAbsPath(".story")
        data = {"node_modules_path": getProjectAbsPath("node_modules"), "cwd": cwd}
        cache = Cache(key=cwd)
        cache.create(".story")

        if os.path.exists(os.path.join(dest_story_path, "main.ts")):
            data.update(
                {
                    "custom_config_callback": "import configCallback from '%s'"
                    % os.path.splitext(os.path.join(dest_story_path, "main.ts"))[0]
                }
            )

        if os.path.exists(os.path.join(cwd, "tsconfig.json")):
            data.update({"ts_config_path": os.path.join(cwd, "tsconfig.json")})
        elif os.path.exists(os.path.join(dest_story_path, "tsconfig.json")):
            data.update(
                {"ts_config_path": os.path.join(dest_story_path, "tsconfig.json")}
            )
        else:
            data.update(
                {
                    "ts_config_path": os.path.join(
                        cache.getPath(".story"), "tsconfig.json"
                    )
                }
            )

        self.app.mjw.template.renderTo(
            getTemplatePath("story"), cache.getPath(".story"), data, force=True
        )

        subprocess.run(
            [
                getNodeBinPath("start-storybook"),
                "-c",
                cache.getPath(".story"),
            ],
            check=True,
        )
