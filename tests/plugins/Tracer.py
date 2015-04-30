from nose2.events import Plugin
from ..ReqTracer import Requirements

class Tracer(Plugin):
    configSection = 'tracer'
    commandLineSwitch = ('T', 'with-tracing', 'Turn on tracing')

    #def startTest(self, event):
        

with open('tracerResults.txt', 'w') as f:
    f.write("ReqTracer.requirements:\n")
    f.writelines("%s\n" % l for l in Requirements)
        
