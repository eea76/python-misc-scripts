import play, pickle, math
 
KEYWORDS = ('pan', 'volume', 'ituning', 'iname')
JUST_PRINT = True

class BatchBitch:
    """ load a bunch of files, and set a parameter on each instrument. """
   
    def __init__(self, e=None):
        if e is None:
            self.e = engine.getEngineInterface()
        else:
            self.e = e
        self.commit = True
        for name in KEYWORDS:
            setattr(self, name, None)
       
    def _clear(self):
        print('Deleting All Instruments')
        while self.e.getValue(play.paramEngineNumInstruments) > 0:
            self.e.sendEvent(play.engineEventDeleteInstrument, 0)
       
    def _load(self, fpath):
        self.outfile.write('Loading Patch: %s\n' % fpath)
        self.outfile.flush()
        self.e.sendEvent(play.engineEventLoadPatch, fpath)
   
    def _save(self, fpath):
        print('** Saving Patch: %s' % fpath)
        productId = self.e.getValue(play.paramInstrumentProductIdentifier, 0)
        self.e.sendEvent(play.engineEventSavePatch, fpath, productId, True, -1, 0)
     
    def _print(self, filename, **kwargs):
        nInstruments = self.e.getValue(play.paramEngineNumInstruments)
        for i in range(nInstruments):
            name = self.e.getValue(play.paramInstrumentName, i)
            print('%s\n' % name)
            self.outfile.write("INSTRUMENT '%s': %s\n" % (name, filename))
            self.outfile.flush()
            iProduct = self.e.getValue(play.paramFileProductIndex, filename)
            if iProduct < 0:
                self.outfile.write("**** Product not known\n")
                self.outfile.flush()
            else:
                productID = self.e.getValue(play.paramConfigProductInfo, iProduct, play.productIdentifier)
                if productID is None or productID < 0:
                    self.outfile.write("**** Product not known\n")
                    self.outfile.flush()
        self.outfile.write("\n")
                
    def _set(self, **kwargs):
        nInstruments = self.e.getValue(play.paramEngineNumInstruments)
        regionDict = {}
        for i in range(nInstruments):
            if self.pan != None:
                orig = self.e.getValue(play.paramInstrumentPanUnscaled, i)
                print('** Setting Pan: %s => %s' % (orig, self.pan))
                self.e.setValue(play.paramInstrumentPanUnscaled, self.pan, i)
            if self.volume != None:
                orig = self.e.getValue(play.paramInstrumentVolumeUnscaled, i)
                print('** Setting Volume: %s => %s' % (orig, self.volume))
                self.e.setValue(play.paramInstrumentVolumeUnscaled, self.volume, i)
            if self.ituning != None:
                orig = self.e.getValue(play.paramInstrumentTuneUnscaled, i)
                self.e.setValue(play.paramInstrumentTuneUnscaled, self.ituning, i)
                new = self.e.getValue(play.paramInstrumentTuneUnscaled, i)
                print('** Setting Tuning: %s => %s' % (orig, new))
               
            if self.iname != None:
                orig = self.e.getValue(play.paramInstrumentName, i)
                new = orig + self.iname
                self.e.setValue(play.paramInstrumentName, new, i)
                print('** Setting Inst. Name: %s => %s' % (orig, orig + self.iname))
               
 
 
    ###### USE THESE MEHODS OUTSIDE THE CLASS ######
   
    def go(self, files, **kwargs):
        """ load each file, set the param, save the file. """
        for kw in KEYWORDS:
            setattr(self, kw, None)
        for kw in kwargs.keys():
            if not kw in KEYWORDS:
                raise KeyError('Invalid keyword: %s' % kw)
        self.__dict__.update(kwargs)
        self._save('/tmp/Play.batch_start.ewi')
        self.outfile = open(r"/Users/elon/Desktop/HOP Gold.txt", "w")#, encoding="utf-8")
        for fpath in files:
            self._clear()
            self._load(fpath)
            #self._set()
            self._print(fpath)
            #if self.commit:
                #self._save(fpath)
        self._clear()
        self._load('/tmp/Play.batch_start.ewi')
        for kw in kwargs.keys():
            setattr(self, kw, None)
        self.outfile.close()

 
 
def onMain():
    import os
   
    print('Finding patches in %s:' % ROOT)
    patch_files = []
    for root, dirs, files in os.walk(ROOT):
        for fpath in files:
            fullpath = os.path.join(root, fpath)
            if fpath.endswith('.ewi'):
                patch_files.append(fullpath)
                print('    Found: %s' % fullpath)
    mybitch = BatchBitch(engine.getEngineInterface())
    mybitch.commit = True
    kwargs = {}
    
    mybitch.go(patch_files) ##Call Intstrument functions here##
 
 
#ROOT = ''
ROOT = r"/Volumes/2TB Mac/Play Libraries/Hollywood Orchestral Percussion Gold/Hollywood Orch Percussion Instruments"
















