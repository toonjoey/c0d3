# 2013.08.22 22:20:36 Pacific Daylight Time
# Embedded file name: toontown.fishing.ThreewayBingo
from direct.directnotify import DirectNotifyGlobal
from toontown.fishing import BingoGlobals
from toontown.fishing import BingoCardBase

class ThreewayBingo(BingoCardBase.BingoCardBase):
    __module__ = __name__
    notify = DirectNotifyGlobal.directNotify.newCategory('ThreewayBingo')

    def __init__(self, cardSize = BingoGlobals.CARD_SIZE, rowSize = BingoGlobals.CARD_ROWS, colSize = BingoGlobals.CARD_COLS):
        BingoCardBase.BingoCardBase.__init__(self, cardSize, rowSize, colSize)
        self.gameType = BingoGlobals.THREEWAY_CARD
        self.rowResult = 0
        self.fDiagResult = 0
        self.bDiagResult = 0

    def checkForWin(self, id):
        rowId = int(id / BingoGlobals.CARD_ROWS)
        colId = id % BingoGlobals.CARD_COLS
        if rowId == 2:
            self.rowResult = self.rowCheck(rowId)
        if self.fDiagCheck(id):
            self.fDiagResult = 1
        if self.bDiagCheck(id):
            self.bDiagResult = 1
        if self.rowResult and self.fDiagResult and self.bDiagResult:
            return BingoGlobals.WIN
        return BingoGlobals.NO_UPDATE

    def checkForColor(self, id):
        return self.onRow(2, id) | self.onFDiag(id) | self.onBDiag(id)

    def checkForBingo(self):
        id = self.cardSize / 2
        if self.checkForWin(id):
            return BingoGlobals.WIN
        return BingoGlobals.NO_UPDATE
# okay decompyling C:\Users\Maverick\Documents\Visual Studio 2010\Projects\Unfreezer\py2\toontown\fishing\ThreewayBingo.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2013.08.22 22:20:37 Pacific Daylight Time
