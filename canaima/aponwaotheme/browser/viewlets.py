from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.layout.viewlets import common
from plone.app.layout.links.viewlets import FaviconViewlet

class GlobalSectionsViewlet(common.GlobalSectionsViewlet):
    render = ViewPageTemplateFile('templates/global_sections.pt')
    
class SearchBoxViewlet(common.SearchBoxViewlet):
    render = ViewPageTemplateFile('templates/searchbox.pt')

class Favicon(FaviconViewlet):
    render = ViewPageTemplateFile('templates/favicon.pt')
