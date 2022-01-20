import os


class TemplateHandler:
    def __init__(self, app):
        self.app = app

    def renderTo(self, src, dest, data, force=False, exclude=None, ignore=None):
        self.app.template.copy(src, dest, data, force, exclude, ignore)

        for cur_dir, sub_dirs, files in os.walk(dest):
            for _file in files:
                split_file_name = os.path.splitext(_file)

                if split_file_name[1] == ".jinja" or split_file_name[1] == ".jinja2":
                    os.rename(
                        os.path.join(cur_dir, _file),
                        os.path.join(cur_dir, split_file_name[0]),
                    )
