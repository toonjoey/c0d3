# 2013.08.22 22:20:33 Pacific Daylight Time
# Embedded file name: toontown.fishing.FishBrowser
from toontown.toonbase import ToontownGlobals
from direct.directnotify import DirectNotifyGlobal
from direct.gui.DirectGui import *
from pandac.PandaModules import *
from toontown.toonbase import TTLocalizer
import GenusPanel
import FishGlobals

class FishBrowser(DirectScrolledList):
    __module__ = __name__
    notify = DirectNotifyGlobal.directNotify.newCategory('FishBrowser')

    def __init__(self, parent = aspect2d, **kw):
        self.parent = parent
        gui = loader.loadModel('phase_3.5/models/gui/friendslist_gui')
        optiondefs = (('parent', self.parent, None),
         ('relief', None, None),
         ('incButton_image', (gui.find('**/FndsLst_ScrollUp'),
           gui.find('**/FndsLst_ScrollDN'),
           gui.find('**/FndsLst_ScrollUp_Rllvr'),
           gui.find('**/FndsLst_ScrollUp')), None),
         ('incButton_relief', None, None),
         ('incButton_scale', (1.3, 1.3, -1.3), None),
         ('incButton_pos', (0, 0, -0.525), None),
         ('incButton_image3_color', Vec4(0.8, 0.8, 0.8, 0.5), None),
         ('decButton_image', (gui.find('**/FndsLst_ScrollUp'),
           gui.find('**/FndsLst_ScrollDN'),
           gui.find('**/FndsLst_ScrollUp_Rllvr'),
           gui.find('**/FndsLst_ScrollUp')), None),
         ('decButton_relief', None, None),
         ('decButton_scale', (1.3, 1.3, 1.3), None),
         ('decButton_pos', (0, 0, 0.525), None),
         ('decButton_image3_color', Vec4(0.8, 0.8, 0.8, 0.5), None),
         ('numItemsVisible', 1, None),
         ('items', map(str, FishGlobals.getGenera()), None),
         ('scrollSpeed', 4, None),
         ('itemMakeFunction', GenusPanel.GenusPanel, None),
         ('itemMakeExtraArgs', None, None))
        gui.removeNode()
        self.defineoptions(kw, optiondefs)
        DirectScrolledList.__init__(self, parent)
        self.initialiseoptions(FishBrowser)
        return None

    def destroy(self):
        DirectScrolledList.destroy(self)
        self.parent = None
        return

    def update(self):
        pass

    def show(self):
        if not self.parent.isHidden():
            self['items'][self.index].show()
            DirectScrolledList.show(self)

    def hide(self):
        self['items'][self.index].hide()
        DirectScrolledList.hide(self)
# okay decompyling C:\Users\Maverick\Documents\Visual Studio 2010\Projects\Unfreezer\py2\toontown\fishing\FishBrowser.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2013.08.22 22:20:33 Pacific Daylight Time
