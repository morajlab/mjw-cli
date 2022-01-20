from cement import Controller, ex
from ..core.cache import Cache as CacheHandler
from ..core.path import getCurrentAbsPath


class Cache(Controller):
    class Meta:
        label = "cache"
        stacked_on = "base"
        stacked_type = "embedded"

    @ex(
        help="Cache command help",
        arguments=[
            (
                ["-c", "--clean"],
                {
                    "help": "Clean all caches for specified path",
                    "action": "store",
                    "dest": "path",
                },
            ),
            (
                ["-C", "--clean-all"],
                {
                    "help": "Clean all caches",
                    "action": "store_true",
                    "dest": "clean_all",
                },
            ),
        ],
    )
    def cache(self):
        """Cache docstring"""

        if self.app.pargs.clean_all is True:
            CacheHandler.cleanAll()
            self.app.log.info("All caches cleaned.")

        if self.app.pargs.path is not None:
            abs_path = getCurrentAbsPath(self.app.pargs.path)
            cache_obj = CacheHandler(key=abs_path)
            cache_obj.clean()
            self.app.log.info("All caches cleaned for path '%s'." % abs_path)
