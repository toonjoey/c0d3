# 2013.08.22 22:26:54 Pacific Daylight Time
# Embedded file name: toontown.tutorial.TutorialManager
from pandac.PandaModules import *
from direct.distributed import DistributedObject
from direct.directnotify import DirectNotifyGlobal
from toontown.hood import ZoneUtil

class TutorialManager(DistributedObject.DistributedObject):
    __module__ = __name__
    notify = DirectNotifyGlobal.directNotify.newCategory('TutorialManager')
    neverDisable = 1

    def __init__(self, cr):
        DistributedObject.DistributedObject.__init__(self, cr)

    def generate(self):
        DistributedObject.DistributedObject.generate(self)
        messenger.send('tmGenerate')
        self.accept('requestTutorial', self.d_requestTutorial)
        self.accept('requestSkipTutorial', self.d_requestSkipTutorial)
        self.accept('rejectTutorial', self.d_rejectTutorial)

    def disable(self):
        self.ignoreAll()
        ZoneUtil.overrideOff()
        DistributedObject.DistributedObject.disable(self)

    def d_requestTutorial(self):
        self.sendUpdate('requestTutorial', [])

    def d_rejectTutorial(self):
        self.sendUpdate('rejectTutorial', [])

    def d_requestSkipTutorial(self):
        self.sendUpdate('requestSkipTutorial', [])

    def skipTutorialResponse(self, allOk):
        messenger.send('skipTutorialAnswered', [allOk])

    def enterTutorial(self, branchZone, streetZone, shopZone, hqZone):
        base.localAvatar.cantLeaveGame = 1
        ZoneUtil.overrideOn(branch=branchZone, exteriorList=[streetZone], interiorList=[shopZone, hqZone])
        messenger.send('startTutorial', [shopZone])
        self.acceptOnce('stopTutorial', self.__handleStopTutorial)
        self.acceptOnce('toonArrivedTutorial', self.d_toonArrived)

    def __handleStopTutorial(self):
        base.localAvatar.cantLeaveGame = 0
        self.d_allDone()
        ZoneUtil.overrideOff()

    def d_allDone(self):
        self.sendUpdate('allDone', [])

    def d_toonArrived(self):
        self.sendUpdate('toonArrived', [])
# okay decompyling C:\Users\Maverick\Documents\Visual Studio 2010\Projects\Unfreezer\py2\toontown\tutorial\TutorialManager.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2013.08.22 22:26:54 Pacific Daylight Time
