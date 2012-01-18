import re, urllib, hashlib
from django import template

register = template.Library()

class GravatarUrlNode(template.Node):
    def __init__(self, email):
        self.email = template.Variable(email)

    def render(self, context):
        size = 40
        default = "wavatar"
        try:
            email = self.email.resolve(context)
            gravatar_url = "http://www.gravatar.com/avatar/" + hashlib.md5(email.lower()).hexdigest() + "?"
            gravatar_url += urllib.urlencode({'d':default, 's':str(size)})
            print gravatar_url
            return gravatar_url
        except template.VariableDoesNotExist:
            print "except"
            return ''

@register.tag
def get_gravatar_url(parser, token):
    try:
        tag_name, arg = token.contents.split()
    except ValueError:
        raise template.TemplateSyntaxError, "%s tag requires arguments" % token.contents.split()[0]
    return GravatarUrlNode(arg)
