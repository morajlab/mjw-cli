from cement import App, TestApp, init_defaults
from cement.core.exc import CaughtSignal
from .core.exc import CLIError
from .controllers import base, story, cache, lint, format, info, watch, hook, test

# configuration defaults
CONFIG = init_defaults("cli", "plugin.mjwplugin")
CONFIG["plugin.mjwplugin"]["enabled"] = "true"


class CLI(App):
    """CLI primary application."""

    class Meta:
        label = "cli"

        # configuration defaults
        config_defaults = CONFIG

        # call sys.exit() on close
        exit_on_close = True

        # load additional framework extensions
        extensions = ["yaml", "colorlog", "jinja2", "tabulate"]

        # configuration handler
        config_handler = "yaml"

        # configuration file suffix
        config_file_suffix = ".yml"

        # set the log handler
        log_handler = "colorlog"

        # set the output handler
        output_handler = "jinja2"

        template_handler = "jinja2"

        # register handlers
        handlers = [
            base.Base,
            story.Story,
            cache.Cache,
            lint.Lint,
            format.Format,
            info.Info,
            watch.Watch,
            hook.Hook,
            test.Test
        ]


class CLITest(TestApp, CLI):
    """A sub-class of CLI that is better suited for testing."""

    class Meta:
        label = "cli"


def main():
    with CLI() as app:
        try:
            app.run()

        except AssertionError as e:
            print("AssertionError > %s" % e.args[0])
            app.exit_code = 1

            if app.debug is True:
                import traceback

                traceback.print_exc()

        except CLIError as e:
            print("CLIError > %s" % e.args[0])
            app.exit_code = 1

            if app.debug is True:
                import traceback

                traceback.print_exc()

        except CaughtSignal as e:
            # Default Cement signals are SIGINT and SIGTERM, exit 0 (non-error)
            print("\n%s" % e)
            app.exit_code = 0


if __name__ == "__main__":
    main()
