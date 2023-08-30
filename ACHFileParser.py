from specialized_classes import *

class ACHFileParser:
    def __init__(self, file_path):
        self.file_path = file_path
        self.records = []
        self.current_standard_entry_class_code = None
        self.record_type_mappings = {
            'ACK': {'6': AckEntryDetailRecord, '7': AckAddendaRecord},
            'ADV': {'8': AdvBatchControlRecord, '6':AdvDetailEntryRecord},
            'ARC': {'6': ArcDetailEntryRecord},
            'ATX': {'6': AtxEntryDetailRecord, '7': AtxAddendaRecord},
            'BOC': {'6': BocDetailEntryRecord},
            'CCD': {'6': CcdDetailEntryRecord, '7': CcdAddendaRecord},
            'CIE': {'6': CieEntryDetailRecord, '7': CieAddendaRecord},
            'CTX': {'6': CTXEntryDetailRecord, '7': CTXAddendaRecord},
            'DNE': {'6': DNEEntryDetail, '7': DNEAddenda},
            'ENR': {'6': ENREntryDetail, '7': ENRAddenda},
            'MTE': {'6': MTEEntryDetail, '7': MTEAddenda},
            'POP': {'6': POPDetailRecord},
            'POS': {'6': POSEntryDetailRecord, '7': POSAddendaRecord},
            'PPD': {'6': PPDDetailRecord},
            'RCK': {'6': RCKDetailRecord},
            'SHR': {'6': SHREntryDetailRecord, '7': SHRAddendaRecord},
            'TEL': {'6': TELDetailRecord},
            'TRC': {'6': TRCEntryDetailRecord},
            'TRX': {'6': TRXEntryDetailRecord, '7': TRXAddendaRecord},
            'WEB': {'6': WEBDetailRecord},
            'XCK': {'6': XCKDetailRecord},
            'IAT': {'6': IATBatchHeaderRecord}
        }

    def parse(self):
        with open(self.file_path, 'r') as file:
            for line in file:
                line = line.rstrip('\n')

                if line[0] == '1':
                    self.records.append(FileHeaderRecord(line))
                elif line[0] == '5':
                    batch_header = BatchHeaderRecord(line)
                    self.current_standard_entry_class_code = batch_header.standard_entry_class_code  # Set the flag
                    self.records.append(batch_header)
                elif self.current_standard_entry_class_code in self.record_type_mappings:
                    record_class = self.record_type_mappings[self.current_standard_entry_class_code].get(line[0], None)
                    if record_class:
                        self.records.append(record_class(line))
                elif line[0] == '8':
                    self.records.append(BatchControlRecord(line))
                elif line[0] == '9':
                    self.records.append(AdvFileControlRecord(line))

                # Reset the flag when we reach the end of a batch
                if line[0] == '8':
                    self.current_standard_entry_class_code = None
                
        return self.records


