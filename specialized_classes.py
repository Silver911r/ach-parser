
class Record:
    def __init__(self, line):
        self.line = line.strip()

class FileHeaderRecord(Record):
    def __init__(self, line):
        super().__init__(line)
        self.parse_fields()

    def parse_fields(self):
        self.record_type = self.line[0:1]  # Positions 01-01
        self.priority_code = self.line[1:3]  # Positions 02-03
        self.immediate_destination = self.line[3:13]  # Positions 04-13
        self.immediate_origin = self.line[13:23]  # Positions 14-23
        self.file_creation_date = self.line[23:29]  # Positions 24-29
        self.file_creation_time = self.line[29:33]  # Positions 30-33 (Optional)
        self.file_id_modifier = self.line[33:34]  # Positions 34-34
        self.record_size = self.line[34:37]  # Positions 35-37
        self.blocking_factor = self.line[37:39]  # Positions 38-39
        self.format_code = self.line[39:40]  # Positions 40-40
        self.immediate_destination_name = self.line[40:63]  # Positions 41-63
        self.immediate_origin_or_company_name = self.line[63:86]  # Positions 64-86
        self.reference_code = self.line[86:94]  # Positions 87-94 (Optional)

class BatchHeaderRecord(Record):
    def __init__(self, line):
        super().__init__(line)
        self.parse_fields()

    def parse_fields(self):
        self.record_type = self.line[0:1]  # Positions 01-01
        self.service_class_code = self.line[1:4]  # Positions 02-04
        self.company_name = self.line[4:20]  # Positions 05-20 (Optional)
        self.company_discretionary_data = self.line[20:40]  # Positions 21-40 (Optional)
        self.company_identification = self.line[40:50]  # Positions 41-50
        self.standard_entry_class_code = self.line[50:53]  # Positions 51-53
        self.company_entry_description = self.line[53:63]  # Positions 54-63
        self.company_descriptive_date = self.line[63:69]  # Positions 64-69 (Optional)
        self.effective_entry_date = self.line[69:75]  # Positions 70-75 (Required)
        self.settlement_date_julian = self.line[75:78]  # Positions 76-78 (Filled by ACH Operator)
        self.originator_status_code = self.line[78:79]  # Positions 79-79
        self.originating_dfi_identification = self.line[79:87]  # Positions 80-87
        self.batch_number = self.line[87:94]  # Positions 88-94

class BatchControlRecord(Record):
    def __init__(self, line):
        super().__init__(line)
        self.parse_fields()

    def parse_fields(self):
        self.record_type = self.line[0:1]  # Positions 01-01
        self.service_class_code = self.line[1:4]  # Positions 02-04
        self.entry_addenda_count = self.line[4:10]  # Positions 05-10
        self.entry_hash = self.line[10:20]  # Positions 11-20
        self.total_debit_entry_dollar = self.line[20:32]  # Positions 21-32
        self.total_credit_entry_dollar = self.line[32:44]  # Positions 33-44
        self.company_identification = self.line[44:54]  # Positions 45-54
        self.message_authentication_code = self.line[54:73]  # Positions 55-73 (Optional)
        self.reserved = self.line[73:79]  # Positions 74-79
        self.originating_dfi_identification = self.line[79:87]  # Positions 80-87
        self.batch_number = self.line[87:94]  # Positions 88-94

class AckEntryDetailRecord(Record):
    def __init__(self, line):
        super().__init__(line)
        self.parse_fields()

    def parse_fields(self):
        self.record_type = self.line[0:1]
        self.transaction_code = self.line[1:3]
        self.receiving_dfi_identification = self.line[3:11]
        self.check_digit = self.line[11:12]
        self.dfi_account_number = self.line[12:29]
        self.amount = self.line[29:39]
        self.original_entry_trace_number = self.line[39:54]
        self.receiving_company_name = self.line[54:76]
        self.discretionary_data = self.line[76:78]
        self.addenda_record_indicator = self.line[78:79]
        self.trace_number = self.line[79:94]

class AckAddendaRecord(Record):
    def __init__(self, line):
        super().__init__(line)
        self.parse_fields()

    def parse_fields(self):
        self.record_type = self.line[0:1]
        self.addenda_type_code = self.line[1:3]
        self.payment_related_information = self.line[3:83]
        self.addenda_sequence_number = self.line[83:87]
        self.entry_detail_sequence_number = self.line[87:94]

class AdvBatchControlRecord(Record):
    def __init__(self, line):
        super().__init__(line)
        self.parse_fields()

    def parse_fields(self):
        self.record_type = self.line[0:1]
        self.service_class_code = self.line[1:4]
        self.entry_addenda_count = self.line[4:10]
        self.entry_hash = self.line[10:20]
        self.total_debit_dollar_amount = self.line[20:40]
        self.total_credit_dollar_amount = self.line[40:60]
        self.ach_operator_data = self.line[60:79]
        self.originating_dfi_identification = self.line[79:87]
        self.batch_number = self.line[87:94]

class AdvFileControlRecord(Record):
    def __init__(self, line: str):
        self.record_type_code = line[0:1]  # Should always be '9'
        self.batch_count = int(line[1:7].strip())
        self.block_count = int(line[7:13].strip())
        self.entry_addenda_count = int(line[13:21].strip())
        self.entry_hash = int(line[21:31].strip())
        self.total_debit_entry_dollar_amount = int(line[31:51].strip())  # Convert to actual dollar amount later
        self.total_credit_entry_dollar_amount = int(line[51:71].strip())  # Convert to actual dollar amount later
        # No need to parse reserved since it's blank

class AdvDetailEntryRecord(Record):
    def __init__(self, line):
        self.record_type_code = line[0:1]
        self.transaction_code = line[1:3]
        self.receiving_dfi_identification = line[3:11]
        self.check_digit = line[11:12]
        self.dfi_account_number = line[12:27]
        self.amount = line[27:39]
        self.advice_routing_number = line[39:48]
        self.file_identification = line[48:53]
        self.ach_operator_data = line[53:54]
        self.individual_name = line[54:76]
        self.discretionary_data = line[76:78]
        self.addenda_record_indicator = line[78:79]
        self.routing_number_of_ach_operator = line[79:87]
        self.julian_date = line[87:90]
        self.sequence_number = line[90:94]

class ArcDetailEntryRecord(Record):
    def __init__(self, line):
        self.record_type_code = line[0:1]
        self.transaction_code = line[1:3]
        self.receiving_dfi_identification = line[3:11]
        self.check_digit = line[11:12]
        self.dfi_account_number = line[12:29]
        self.amount = line[29:39]
        self.check_serial_number = line[39:54]
        self.individual_name = line[54:76]
        self.discretionary_data = line[76:78]
        self.addenda_record_indicator = line[78:79]
        self.trace_number = line[80:94]

class AtxEntryDetailRecord(Record):
    def __init__(self, line):
        self.record_type_code = line[0:1]
        self.transaction_code = line[1:3]
        self.receiving_dfi_identification = line[3:11]
        self.check_digit = line[11:12]
        self.dfi_account_number = line[12:29]
        self.amount = line[29:39]
        self.identification_number = line[39:54]
        self.number_of_addenda_records = line[54:58]
        self.receiving_company_name_or_id = line[58:74]
        self.reserved = line[74:76]
        self.discretionary_data = line[76:78]
        self.addenda_record_indicator = line[78:79]
        self.trace_number = line[80:94]

class AtxAddendaRecord(Record):
    def __init__(self, line):
        self.record_type_code = line[0:1]
        self.addenda_type_code = line[1:3]
        self.payment_related_information = line[3:83]
        self.addenda_sequence_number = line[83:87]
        self.entry_detail_sequence_number = line[87:94]

class BocDetailEntryRecord(Record):
    def __init__(self, line):
        self.record_type_code = line[0:1]
        self.transaction_code = line[1:3]
        self.receiving_dfi_identification = line[3:11]
        self.check_digit = line[11:12]
        self.dfi_account_number = line[12:29]
        self.amount = line[29:39]
        self.check_serial_number = line[39:54]
        self.individual_name = line[54:76]
        self.discretionary_data = line[76:78]
        self.addenda_record_indicator = line[78:79]
        self.trace_number = line[79:94]

class CcdDetailEntryRecord(Record):
    def __init__(self, line):
        self.record_type_code = line[0:1]
        self.transaction_code = line[1:3]
        self.receiving_dfi_identification = line[3:11]
        self.check_digit = line[11:12]
        self.dfi_account_number = line[12:29].strip()
        self.amount = float(line[29:39]) / 100  # Assuming it's in cents and converting it to dollars
        self.identification_number = line[39:54].strip()
        self.receiving_company_name = line[54:76].strip()
        self.discretionary_data = line[76:78].strip()
        self.addenda_record_indicator = line[78:79]
        self.trace_number = line[79:94]

class CcdAddendaRecord(Record):
    def __init__(self, line):
        self.record_type_code = line[0:1]
        self.addenda_type_code = line[1:3]
        self.payment_related_info = line[3:83].strip()
        self.addenda_sequence_number = int(line[83:87])
        self.entry_detail_sequence_number = line[87:94]

class CieEntryDetailRecord(Record):
    def __init__(self, line):
        self.record_type_code = line[0:1]
        self.transaction_code = line[1:3]
        self.receiving_dfi_id = line[3:11]
        self.check_digit = line[11:12]
        self.dfi_account_number = line[12:29].strip()
        self.amount = float(line[29:39]) / 100  # Assuming the amount is in cents and converting to dollars
        self.individual_name = line[39:54].strip()
        self.individual_identification_number = line[54:76].strip()
        self.discretionary_data = line[76:78].strip()
        self.addenda_record_indicator = line[78:79]
        self.trace_number = line[79:94]

class CieAddendaRecord(Record):
    def __init__(self, line):
        self.record_type_code = line[0:1]
        self.addenda_type_code = line[1:3]
        self.payment_related_information = line[3:83].strip()
        self.addenda_sequence_number = int(line[83:87])
        self.entry_detail_sequence_number = int(line[87:94])

class CTXEntryDetailRecord(Record):
    def __init__(self, line):
        self.record_type_code = line[0:1]
        self.transaction_code = line[1:3]
        self.receiving_dfi_identification = line[3:11]
        self.check_digit = line[11:12]
        self.dfi_account_number = line[12:29].strip()
        self.amount = int(line[29:39]) / 100  # Convert to float with 2 decimal places
        self.identification_number = line[39:54].strip()
        self.number_of_addenda_records = int(line[54:58])
        self.receiving_company_name_or_id = line[58:74].strip()
        self.discretionary_data_field = line[76:78].strip()
        self.addenda_record_indicator = line[78:79]
        self.trace_number = line[79:94]

    def __repr__(self):
        return f"<CTXEntryDetailRecord(record_type_code={self.record_type_code}, transaction_code={self.transaction_code}, ...)>"

class CTXAddendaRecord(Record):
    def __init__(self, line):
        self.record_type_code = line[0:1]
        self.addenda_type_code = line[1:3]
        self.payment_related_information = line[3:83].strip()
        self.addenda_sequence_number = int(line[83:87])
        self.entry_detail_sequence_number = int(line[87:94])

    def __repr__(self):
        return f"<CTXAddendaRecord(record_type_code={self.record_type_code}, addenda_type_code={self.addenda_type_code}, ...)>"

class DNEEntryDetail:
    def __init__(self, line):
        self.record_type_code = line[0:1]
        self.transaction_code = int(line[1:3])
        self.receiving_dfi_identification = line[3:11]
        self.check_digit = int(line[11:12])
        self.dfi_account_number = line[12:29].strip()
        self.amount = float(line[29:39])  # It's mandatory to have 10 zeros
        self.identification_number = line[39:54].strip() if line[39:54].strip() else None
        self.individual_name = line[54:76].strip() if line[54:76].strip() else None
        self.discretionary_data = line[76:78].strip() if line[76:78].strip() else None
        self.addenda_record_indicator = int(line[78:79])
        self.trace_number = int(line[79:94])

    def __repr__(self):
        return f"<DNEEntryDetail(record_type_code={self.record_type_code}, transaction_code={self.transaction_code}, ...)>"

    def validate(self):
        # Here you can add some validations. For instance, for DNE, the amount must be zero.
        if self.amount != 0:
            raise ValueError("Invalid DNE Record: Amount must be zero.")
