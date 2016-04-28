import json

class JSONExport(object):
    def __init__(slef,filename):
        super(JSONExport, self).__init__()
        self._filename = filename

    def export(self,measure):
        print("--- Exporting to JSON ---")
        with open(self._filename + '.json', 'w') as jsonfile:
            json.dump(measure, jsonfile, indent = 4)
        print("---" + self._filename + ".json created! ---")
