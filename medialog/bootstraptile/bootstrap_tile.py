# -*- coding: utf-8 -*-

# Basic implementation taken from
# http://davisagli.com/blog/using-tiles-to-provide-more-flexible-plone-layouts

from collective.cover import _
from collective.cover.tiles.base import IPersistentCoverTile
from collective.cover.tiles.base import PersistentCoverTile
from plone.app.textfield import RichText
from plone.app.textfield.interfaces import ITransformer
from plone.app.textfield.value import RichTextValue
from plone.tiles.interfaces import ITileDataManager
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from zope.interface import implements
from zope import schema


from collective.cover.tiles.richtext import RichTextTile
from collective.cover.tiles.richtext import IRichTextTile

class IBootstrapTile(IRichTextTile):

    text = RichText(title=u'Text')
    klasse = schema.TextLine(title=u'CSS Classes')
    style = schema.TextLine(title=u'Style')
    data-wow-duration = schema.Int(title=u'data-wow-duration')
    data-wow-delay = schema.Int(title=u'data-wow-delay')

class BootstrapTile(RichTextTile):

    implements(IRichTextTile)

    index = ViewPageTemplateFile('bootstrap_tile.pt')

    is_configurable = True
    short_name = _(u'msg_short_name_richtext', default=u'Rich Text')

    def getKlasse(self):
        """ Return class info stored in the tile.
        """
        return self.data['klasse']

    def getDatawowdelay(self):
        """ Return data wow delay info stored in the tile.
        """
        return self.data['data-wow-delay']
        
    def getDatawowduration(self):
        """ Return data wow duration info stored in the tile.
        """
        return self.data['data-wow-duration']
        
    def getStyle(self):
        """ Return style, maybe we need to filter this (safe html).
        """
        return self.data['style']