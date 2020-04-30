import play, os, sys

class BatchHarness:
    def __init__(self, basePath):
        self.e = engine.getEngineInterface()
        self.iterator = os.walk(basePath)
        productID = self.e.getValue(play.paramInstrumentProductIdentifier, 0)
        self.e.sendEvent(play.engineEventSavePatch, "/tmp/Play.batch_start.ewi", productID, True, -1, 0)
        self.log = False
        self.logLoads = False
        self.saveToFile = False
        self.abortOnException = False

    def openLog(self, path, append = False):
        ''''Opens a log file for writing. Pass True as the second parameter to append instead of overwriting'''
        self.log = open(path, append and 'a' or 'w')

    def closelog(self):
        '''Closes the log file.'''
        if self.log:
            self.log.close()
            self.log = False
        
    def output(self, message, suppressNewLine = False):
        '''Outputs a message to the console and, if open, the log file. Pass True as the second parameter to avoid writing a newline.'''
        # first write to the console
        sys.stdout.write(message)
        if not suppressNewLine:
            sys.stdout.write("\n")
            
        # then if there's a log file opened, write to it too
        if self.log:
            self.log.write(message)
            if not suppressNewLine:
                self.log.write("\n")
            self.log.flush()

    def go(self):
        '''Iterate over all instruments in all patches inside the basePath passed to the constructor.'''
        # First remove any loaded instruments, specifically including the one containing the batch script.
        for i in range(self.e.getValue(play.paramEngineNumInstruments) - 1, -1, -1):
            self.e.sendEvent(play.engineEventDeleteInstrument, i)
        # Then iterate over all of the files in the directory.
        for root, dirs, files in self.iterator:
            try:
                for fpath in files:
                    fullpath = os.path.join(root, fpath)
                    if fpath.endswith('.ewi'):
                        self.load(fullpath)
                        nInstruments = self.e.getValue(play.paramEngineNumInstruments)
                        for i in range(nInstruments):
                            if self.logLoads:
                                self.output("\tProcessing instrument %s" % self.e.getValue(play.paramInstrumentName, i))
                            self.process(fullpath, i)
                        self.unload()
            except Exception as e:
                self.output(repr(e))
                # Clean up the loaded instrument before continuing
                self.saveToFile = False # never save if there's been an error
                self.unload()
                if self.abortOnException:
                    break
        self.e.sendEvent(play.engineEventLoadPatch, "/tmp/Play.batch_start.ewi")
        
    def load(self, path):
        '''Loads a patch file from disk.'''
        if self.logLoads:
            self.output("Loading file %s" % path)
        self.e.sendEvent(play.engineEventLoadPatch, path)

    def save(self, path):
        '''Flags the loaded patch to be saved before being unloaded.'''
        self.saveToFile = path

    def unload(self):
        '''Unloads all loaded instruments. If save() has been called previously, the patch will be saved before unloading.'''
        if self.saveToFile:
            if self.logLoads:
                self.output("\tSaving file %s" % self.saveToFile)
            self.e.sendEvent(play.engineEventSaveInstrument, self.saveToFile)
            self.saveToFile = False
        for i in range(self.e.getValue(play.paramEngineNumInstruments) - 1, -1, -1):
            if self.logLoads:
                self.output("\tUnloading instrument %s" % self.e.getValue(play.paramInstrumentName, i))
            self.e.sendEvent(play.engineEventDeleteInstrument, i)

    def process(self, path, iInstrument):
        '''Do your processing work in this function. You may use self.save(path) if you make any changes.'''
        for iCol in range(self.e.getValue(play.paramArticulationNumColumns, iInstrument)):
            self.output("\t\tLoading mic %s" % self.e.getValue(play.paramArticulationColumnName, iInstrument, iCol))
            self.e.setValue(play.paramArticulationColumnLoaded, True, iInstrument, iCol)
            self.e.setValue(play.paramArticulationColumnLoaded, False, iInstrument, iCol)
             
def onMain():
    '''This function is invoked when you click the "Execute Script" button.'''
    batch = BatchHarness(r"/Users/michaelault/Desktop/Libraries/QL Stormdrum 3/SD3 Instruments")
    batch.openLog(r"/Users/michaelault/Desktop/SD3final.txt")
    batch.logLoads = True
    # optional: batch.abortOnException = True
    batch.go()
    batch.closeLog()



























































