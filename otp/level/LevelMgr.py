# 2013.08.22 22:15:33 Pacific Daylight Time
# Embedded file name: otp.level.LevelMgr
from direct.showbase.PythonUtil import Functor
import LevelMgrBase

class LevelMgr(LevelMgrBase.LevelMgrBase):
    __module__ = __name__

    def __init__(self, level, entId):
        LevelMgrBase.LevelMgrBase.__init__(self, level, entId)
        self.geom = loader.loadModel(self.modelFilename)
        if not self.geom:
            import pdb
            pdb.set_trace()
        self.zoneNums = []
        self.level.zoneNum2zoneId = {}
        self.level.zoneId2zoneNum = {}
        self.accept(self.level.getEntityOfTypeCreateEvent('zone'), self.handleZoneCreated)

    def destroy(self):
        del self.level.zoneIds
        del self.level.zoneId2zoneNum
        del self.level.zoneNum2zoneId
        self.geom.removeNode()
        del self.geom
        LevelMgrBase.LevelMgrBase.destroy(self)

    def handleZoneCreated(self, entId):
        zoneEnt = self.level.getEntity(entId)
        self.zoneNums.append(zoneEnt.entId)
        self.privAssignZoneIds()
        self.accept(self.level.getEntityDestroyEvent(entId), Functor(self.handleZoneDestroy, entId))

    def handleZoneDestroy(self, entId):
        zoneEnt = self.level.getEntity(entId)
        del self.level.zoneId2zoneNum[self.level.zoneNum2zoneId[zoneEnt.entId]]
        del self.level.zoneNum2zoneId[zoneEnt.entId]
        self.zoneNums.remove(zoneEnt.entId)
        self.privAssignZoneIds()

    def privAssignZoneIds(self):
        self.zoneNums.sort()
        for i in range(len(self.zoneNums)):
            zoneNum = self.zoneNums[i]
            zoneEnt = self.level.getEntity(zoneNum)
            zoneId = self.level.zoneIds[i]
            zoneEnt.setZoneId(zoneId)
            self.level.zoneNum2zoneId[zoneNum] = zoneId
            self.level.zoneId2zoneNum[zoneId] = zoneNum
# okay decompyling C:\Users\Maverick\Documents\Visual Studio 2010\Projects\Unfreezer\py2\otp\level\LevelMgr.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2013.08.22 22:15:33 Pacific Daylight Time
