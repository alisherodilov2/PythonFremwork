from jinja2 import Template

class View:
    @staticmethod
    def render(template_str, context):
        template = Template(template_str)
        return template.render(context)
