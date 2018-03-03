# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1505003389.788178
_enable_loop = True
_template_filename = '/home/reddit/src/reddit/r2/r2/templates/subscribebutton.html'
_template_uri = '/subscribebutton.html'
_source_encoding = 'utf-8'
from r2.lib.filters import websafe, unsafe, conditional_websafe
from pylons import request
from pylons import tmpl_context as c
from pylons import app_globals as g
from pylons.i18n import _, ungettext
_exports = ['subscribe_button']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 23
    ns = runtime.TemplateNamespace('__anon_0x7f3608ce6650', context._clean_inheritance_tokens(), templateuri=u'printablebuttons.html', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f3608ce6650')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f3608ce6650')._populate(_import_ns, [u'toggle_button'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        self = _import_ns.get('self', context.get('self', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 22
        __M_writer(u'\n')
        # SOURCE LINE 23
        __M_writer(u'\n\n')
        # SOURCE LINE 25
        __M_writer(conditional_websafe(self.subscribe_button(thing.sr, thing.data_attrs)))
        __M_writer(u'\n\n')
        # SOURCE LINE 40
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_subscribe_button(context,sr,data_attrs,css_class='subscribe-button'):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f3608ce6650')._populate(_import_ns, [u'toggle_button'])
        toggle_button = _import_ns.get('toggle_button', context.get('toggle_button', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 27
        __M_writer(u'\n    ')
        # SOURCE LINE 28
        __M_writer(conditional_websafe(toggle_button(
        class_name="fancy-toggle-button " + css_class,
        title=_("subscribe"),
        alt_title=_("unsubscribe"),
        callback="subscribe('%s')" % sr._fullname,
        cancelback="unsubscribe('%s')" % sr._fullname,
        css_class="add",
        alt_css_class="remove",
        reverse=sr.subscriber,
        login_required=True,
        data_attrs=data_attrs,
    )))
        # SOURCE LINE 39
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


