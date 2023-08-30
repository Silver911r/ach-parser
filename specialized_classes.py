
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

    def to_dict(self):
        return {
            'record_type': self.record_type,
            'priority_code': self.priority_code,
            'immediate_destination': self.immediate_destination,
            'immediate_origin': self.immediate_origin,
            'file_creation_date': self.file_creation_date,
            'file_creation_time': self.file_creation_time,
            'file_id_modifier': self.file_id_modifier,
            'record_size': self.record_size,
            'blocking_factor': self.blocking_factor,
            'format_code': self.format_code,
            'immediate_destination_name': self.immediate_destination_name,
            'immediate_origin_or_company_name': self.immediate_origin_or_company_name,
            'reference_code': self.reference_code
        }


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

    def to_dict(self):
        return {
            'record_type': self.record_type,
            'service_class_code': self.service_class_code,
            'company_name': self.company_name,
            'company_discretionary_data': self.company_discretionary_data,
            'company_identification': self.company_identification,
            'standard_entry_class_code': self.standard_entry_class_code,
            'company_entry_description': self.company_entry_description,
            'company_descriptive_date': self.company_descriptive_date,
            'effective_entry_date': self.effective_entry_date,
            'settlement_date_julian': self.settlement_date_julian,
            'originator_status_code': self.originator_status_code,
            'originating_dfi_identification': self.originating_dfi_identification,
            'batch_number': self.batch_number
        }


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

    def to_dict(self):
        return {
            'record_type': self.record_type,
            'service_class_code': self.service_class_code,
            'entry_addenda_count': self.entry_addenda_count,
            'entry_hash': self.entry_hash,
            'total_debit_entry_dollar': self.total_debit_entry_dollar,
            'total_credit_entry_dollar': self.total_credit_entry_dollar,
            'company_identification': self.company_identification,
            'message_authentication_code': self.message_authentication_code,
            'reserved': self.reserved,
            'originating_dfi_identification': self.originating_dfi_identification,
            'batch_number': self.batch_number
        }


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

    def to_dict(self):
        return {
            'record_type': self.record_type,
            'transaction_code': self.transaction_code,
            'receiving_dfi_identification': self.receiving_dfi_identification,
            'check_digit': self.check_digit,
            'dfi_account_number': self.dfi_account_number,
            'amount': self.amount,
            'original_entry_trace_number': self.original_entry_trace_number,
            'receiving_company_name': self.receiving_company_name,
            'discretionary_data': self.discretionary_data,
            'addenda_record_indicator': self.addenda_record_indicator,
            'trace_number': self.trace_number
        }


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

    def to_dict(self):
        return {
            'record_type': self.record_type,
            'addenda_type_code': self.addenda_type_code,
            'payment_related_information': self.payment_related_information,
            'addenda_sequence_number': self.addenda_sequence_number,
            'entry_detail_sequence_number': self.entry_detail_sequence_number
        }


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

    def to_dict(self):
        return {
            'record_type': self.record_type,
            'service_class_code': self.service_class_code,
            'entry_addenda_count': self.entry_addenda_count,
            'entry_hash': self.entry_hash,
            'total_debit_dollar_amount': self.total_debit_dollar_amount,
            'total_credit_dollar_amount': self.total_credit_dollar_amount,
            'ach_operator_data': self.ach_operator_data,
            'originating_dfi_identification': self.originating_dfi_identification,
            'batch_number': self.batch_number
        }


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
    
    def to_dict(self):
        return {
            'record_type_code': self.record_type_code,
            'batch_count': self.batch_count,
            'block_count': self.block_count,
            'entry_addenda_count': self.entry_addenda_count,
            'entry_hash': self.entry_hash,
            'total_debit_entry_dollar_amount': self.total_debit_entry_dollar_amount,
            'total_credit_entry_dollar_amount': self.total_credit_entry_dollar_amount
        }


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

    def to_dict(self):
        return {
            'record_type_code': self.record_type_code,
            'transaction_code': self.transaction_code,
            'receiving_dfi_identification': self.receiving_dfi_identification,
            'check_digit': self.check_digit,
            'dfi_account_number': self.dfi_account_number,
            'amount': self.amount,
            'advice_routing_number': self.advice_routing_number,
            'file_identification': self.file_identification,
            'ach_operator_data': self.ach_operator_data,
            'individual_name': self.individual_name,
            'discretionary_data': self.discretionary_data,
            'addenda_record_indicator': self.addenda_record_indicator,
            'routing_number_of_ach_operator': self.routing_number_of_ach_operator,
            'julian_date': self.julian_date,
            'sequence_number': self.sequence_number
        }


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

    def to_dict(self):
        return {
            'record_type_code': self.record_type_code,
            'transaction_code': self.transaction_code,
            'receiving_dfi_identification': self.receiving_dfi_identification,
            'check_digit': self.check_digit,
            'dfi_account_number': self.dfi_account_number,
            'amount': self.amount,
            'check_serial_number': self.check_serial_number,
            'individual_name': self.individual_name,
            'discretionary_data': self.discretionary_data,
            'addenda_record_indicator': self.addenda_record_indicator,
            'trace_number': self.trace_number,
        }


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

    def to_dict(self):
        return {
            'record_type_code': self.record_type_code,
            'transaction_code': self.transaction_code,
            'receiving_dfi_identification': self.receiving_dfi_identification,
            'check_digit': self.check_digit,
            'dfi_account_number': self.dfi_account_number,
            'amount': self.amount,
            'identification_number': self.identification_number,
            'number_of_addenda_records': self.number_of_addenda_records,
            'receiving_company_name_or_id': self.receiving_company_name_or_id,
            'reserved': self.reserved,
            'discretionary_data': self.discretionary_data,
            'addenda_record_indicator': self.addenda_record_indicator,
            'trace_number': self.trace_number,
        }


class AtxAddendaRecord(Record):
    def __init__(self, line):
        self.record_type_code = line[0:1]
        self.addenda_type_code = line[1:3]
        self.payment_related_information = line[3:83]
        self.addenda_sequence_number = line[83:87]
        self.entry_detail_sequence_number = line[87:94]
    
    def to_dict(self):
        return {
            'record_type_code': self.record_type_code,
            'addenda_type_code': self.addenda_type_code,
            'payment_related_information': self.payment_related_information,
            'addenda_sequence_number': self.addenda_sequence_number,
            'entry_detail_sequence_number': self.entry_detail_sequence_number,
        }


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
    
    def to_dict(self):
        return {
            'record_type_code': self.record_type_code,
            'transaction_code': self.transaction_code,
            'receiving_dfi_identification': self.receiving_dfi_identification,
            'check_digit': self.check_digit,
            'dfi_account_number': self.dfi_account_number,
            'amount': self.amount,
            'check_serial_number': self.check_serial_number,
            'individual_name': self.individual_name,
            'discretionary_data': self.discretionary_data,
            'addenda_record_indicator': self.addenda_record_indicator,
            'trace_number': self.trace_number,
        }


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
    
    def to_dict(self):
        return {
            'record_type_code': self.record_type_code,
            'transaction_code': self.transaction_code,
            'receiving_dfi_identification': self.receiving_dfi_identification,
            'check_digit': self.check_digit,
            'dfi_account_number': self.dfi_account_number,
            'amount': self.amount,
            'identification_number': self.identification_number,
            'receiving_company_name': self.receiving_company_name,
            'discretionary_data': self.discretionary_data,
            'addenda_record_indicator': self.addenda_record_indicator,
            'trace_number': self.trace_number,
        }


class CcdAddendaRecord(Record):
    def __init__(self, line):
        self.record_type_code = line[0:1]
        self.addenda_type_code = line[1:3]
        self.payment_related_info = line[3:83].strip()
        self.addenda_sequence_number = int(line[83:87])
        self.entry_detail_sequence_number = line[87:94]
    
    def to_dict(self):
        return {
            'record_type_code': self.record_type_code,
            'addenda_type_code': self.addenda_type_code,
            'payment_related_info': self.payment_related_info,
            'addenda_sequence_number': self.addenda_sequence_number,
            'entry_detail_sequence_number': self.entry_detail_sequence_number,
        }


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

    def to_dict(self):
        return {
            'record_type_code': self.record_type_code,
            'transaction_code': self.transaction_code,
            'receiving_dfi_id': self.receiving_dfi_id,
            'check_digit': self.check_digit,
            'dfi_account_number': self.dfi_account_number,
            'amount': self.amount,
            'individual_name': self.individual_name,
            'individual_identification_number': self.individual_identification_number,
            'discretionary_data': self.discretionary_data,
            'addenda_record_indicator': self.addenda_record_indicator,
            'trace_number': self.trace_number,
        }


class CieAddendaRecord(Record):
    def __init__(self, line):
        self.record_type_code = line[0:1]
        self.addenda_type_code = line[1:3]
        self.payment_related_information = line[3:83].strip()
        self.addenda_sequence_number = int(line[83:87])
        self.entry_detail_sequence_number = int(line[87:94])

    def to_dict(self):
        return {
            'record_type_code': self.record_type_code,
            'addenda_type_code': self.addenda_type_code,
            'payment_related_information': self.payment_related_information,
            'addenda_sequence_number': self.addenda_sequence_number,
            'entry_detail_sequence_number': self.entry_detail_sequence_number,
        }


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

    def to_dict(self):
        return {
            'record_type_code': self.record_type_code,
            'transaction_code': self.transaction_code,
            'receiving_dfi_identification': self.receiving_dfi_identification,
            'check_digit': self.check_digit,
            'dfi_account_number': self.dfi_account_number,
            'amount': self.amount,
            'identification_number': self.identification_number,
            'number_of_addenda_records': self.number_of_addenda_records,
            'receiving_company_name_or_id': self.receiving_company_name_or_id,
            'discretionary_data_field': self.discretionary_data_field,
            'addenda_record_indicator': self.addenda_record_indicator,
            'trace_number': self.trace_number
        }

    def __repr__(self):
        return f"<CTXEntryDetailRecord(record_type_code={self.record_type_code}, transaction_code={self.transaction_code}, ...)>"

class CTXAddendaRecord(Record):
    def __init__(self, line):
        self.record_type_code = line[0:1]
        self.addenda_type_code = line[1:3]
        self.payment_related_information = line[3:83].strip()
        self.addenda_sequence_number = int(line[83:87])
        self.entry_detail_sequence_number = int(line[87:94])

    def to_dict(self):
        return {
            'record_type_code': self.record_type_code,
            'addenda_type_code': self.addenda_type_code,
            'payment_related_information': self.payment_related_information,
            'addenda_sequence_number': self.addenda_sequence_number,
            'entry_detail_sequence_number': self.entry_detail_sequence_number
        }

    def __repr__(self):
        return f"<CTXAddendaRecord(record_type_code={self.record_type_code}, addenda_type_code={self.addenda_type_code}, ...)>"

class DNEEntryDetail(Record):
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
    
    def to_dict(self):
        return {
            'record_type_code': self.record_type_code,
            'transaction_code': self.transaction_code,
            'receiving_dfi_identification': self.receiving_dfi_identification,
            'check_digit': self.check_digit,
            'dfi_account_number': self.dfi_account_number,
            'amount': self.amount,
            'identification_number': self.identification_number,
            'individual_name': self.individual_name,
            'discretionary_data': self.discretionary_data,
            'addenda_record_indicator': self.addenda_record_indicator,
            'trace_number': self.trace_number
        }

    def __repr__(self):
        return f"<DNEEntryDetail(record_type_code={self.record_type_code}, transaction_code={self.transaction_code}, ...)>"

    def validate(self):
        # Here you can add some validations. For instance, for DNE, the amount must be zero.
        if self.amount != 0:
            raise ValueError("Invalid DNE Record: Amount must be zero.")

class DNEAddenda(Record):
    def __init__(self, line):
        self.record_type_code = line[0:1]
        self.addenda_type_code = int(line[1:3])
        self.payment_related_info = line[3:83].strip() if line[3:83].strip() else None
        self.addenda_sequence_number = int(line[83:87])
        self.entry_detail_sequence_number = int(line[87:94])

    def to_dict(self):
        return {
            'record_type_code': self.record_type_code,
            'addenda_type_code': self.addenda_type_code,
            'payment_related_info': self.payment_related_info,
            'addenda_sequence_number': self.addenda_sequence_number,
            'entry_detail_sequence_number': self.entry_detail_sequence_number
        }

    def __repr__(self):
        return f"<DNEAddenda(record_type_code={self.record_type_code}, addenda_type_code={self.addenda_type_code}, ...)>"
    
    def validate(self):
        # Validation logic, e.g., ensure the addenda_sequence_number starts from 1.
        if self.addenda_sequence_number < 1:
            raise ValueError("Invalid DNE Addenda Record: Addenda Sequence Number must start from 1.")

class ENREntryDetail(Record):
    def __init__(self, line):
        self.record_type_code = line[0:1]
        self.transaction_code = int(line[1:3])
        self.receiving_dfi_identification = line[3:11]
        self.check_digit = int(line[11:12])
        self.dfi_account_number = line[12:29].strip() if line[12:29].strip() else None
        self.amount = int(line[29:39])
        self.identification_number = line[39:54].strip() if line[39:54].strip() else None
        self.number_of_addenda_records = int(line[54:58])
        self.receiving_name = line[58:74].strip()
        self.discretionary_data_field = line[76:78].strip() if line[76:78].strip() else None
        self.addenda_record_indicator = int(line[78:79])
        self.trace_number = int(line[79:94])

    def to_dict(self):
        return {
            'record_type_code': self.record_type_code,
            'transaction_code': self.transaction_code,
            'receiving_dfi_identification': self.receiving_dfi_identification,
            'check_digit': self.check_digit,
            'dfi_account_number': self.dfi_account_number,
            'amount': self.amount,
            'identification_number': self.identification_number,
            'number_of_addenda_records': self.number_of_addenda_records,
            'receiving_name': self.receiving_name,
            'discretionary_data_field': self.discretionary_data_field,
            'addenda_record_indicator': self.addenda_record_indicator,
            'trace_number': self.trace_number
        }

    def __repr__(self):
        return f"<ENREntryDetail(record_type_code={self.record_type_code}, transaction_code={self.transaction_code}, ...)>"

    def validate(self):
        if self.amount != 0:
            raise ValueError("Invalid ENR Entry Detail: Amount must be 0.")
        if self.addenda_record_indicator not in [0, 1]:
            raise ValueError("Invalid ENR Entry Detail: Addenda Record Indicator must be 0 or 1.")

class ENRAddenda(Record):
    def __init__(self, line):
        self.record_type_code = line[0:1]
        self.addenda_type_code = int(line[1:3])
        self.payment_related_info = line[3:83].strip() if line[3:83].strip() else None
        self.addenda_sequence_number = int(line[83:87])
        self.entry_detail_sequence_number = int(line[87:94])

    def to_dict(self):
        return {
            'record_type_code': self.record_type_code,
            'addenda_type_code': self.addenda_type_code,
            'payment_related_info': self.payment_related_info,
            'addenda_sequence_number': self.addenda_sequence_number,
            'entry_detail_sequence_number': self.entry_detail_sequence_number
        }

    def __repr__(self):
        return f"<ENRAddenda(record_type_code={self.record_type_code}, addenda_type_code={self.addenda_type_code}, ...)>"
        
    def validate(self):
        if self.record_type_code != '7':
            raise ValueError("Invalid ENR Addenda: Record Type Code must be '7'.")
        if self.addenda_type_code != 5:
            raise ValueError("Invalid ENR Addenda: Addenda Type Code must be 05.")
        if self.addenda_sequence_number < 1:
            raise ValueError("Invalid ENR Addenda: Addenda Sequence Number must start at 1.")

class MTEEntryDetail(Record):
    def __init__(self, line):
        self.record_type_code = line[0:1]
        self.transaction_code = int(line[1:3])
        self.receiving_dfi_identification = line[3:11]
        self.check_digit = int(line[11:12])
        self.dfi_account_number = line[12:29].strip() if line[12:29].strip() else None
        self.amount = float(line[29:39]) / 100  # Assuming that the amount is given in cents
        self.individual_name = line[39:54].strip()
        self.identification_number = line[54:76].strip()
        self.discretionary_data = line[76:78].strip() if line[76:78].strip() else None
        self.addenda_record_indicator = int(line[78:79])
        self.trace_number = int(line[79:94])

    def to_dict(self):
        return {
            'record_type_code': self.record_type_code,
            'transaction_code': self.transaction_code,
            'receiving_dfi_identification': self.receiving_dfi_identification,
            'check_digit': self.check_digit,
            'dfi_account_number': self.dfi_account_number,
            'amount': self.amount,
            'individual_name': self.individual_name,
            'identification_number': self.identification_number,
            'discretionary_data': self.discretionary_data,
            'addenda_record_indicator': self.addenda_record_indicator,
            'trace_number': self.trace_number
        }

    def __repr__(self):
        return f"<MTEEntryDetail(record_type_code={self.record_type_code}, transaction_code={self.transaction_code}, ...)>"

    def validate(self):
        if self.record_type_code != '6':
            raise ValueError("Invalid MTE Entry: Record Type Code must be '6'.")
        if not 0 < self.transaction_code < 100:
            raise ValueError("Invalid MTE Entry: Transaction Code must be a two-digit number.")
        if self.addenda_record_indicator not in [0, 1]:
            raise ValueError("Invalid MTE Entry: Addenda Record Indicator must be 0 or 1.")

class MTEAddenda(Record):
    def __init__(self, line):
        self.record_type_code = line[0:1]
        self.addenda_type_code = int(line[1:3])
        self.transaction_description = line[3:10].strip() if line[3:10].strip() else None
        self.network_identification_code = line[10:13].strip() if line[10:13].strip() else None
        self.terminal_identification_code = line[13:19].strip()
        self.transaction_serial_number = line[19:25].strip()
        self.transaction_date = line[25:29]
        self.transaction_time = line[29:35]
        self.terminal_location = line[35:62].strip()
        self.terminal_city = line[62:77].strip()
        self.terminal_state = line[77:79].strip()
        self.trace_number = int(line[79:94])

    def to_dict(self):
        return {
            'record_type_code': self.record_type_code,
            'addenda_type_code': self.addenda_type_code,
            'transaction_description': self.transaction_description,
            'network_identification_code': self.network_identification_code,
            'terminal_identification_code': self.terminal_identification_code,
            'transaction_serial_number': self.transaction_serial_number,
            'transaction_date': self.transaction_date,
            'transaction_time': self.transaction_time,
            'terminal_location': self.terminal_location,
            'terminal_city': self.terminal_city,
            'terminal_state': self.terminal_state,
            'trace_number': self.trace_number
        }

    def __repr__(self):
        return f"<MTEAddenda(record_type_code={self.record_type_code}, addenda_type_code={self.addenda_type_code}, ...)>"

    def validate(self):
        if self.record_type_code != '7':
            raise ValueError("Invalid MTE Addenda: Record Type Code must be '7'.")
        if self.addenda_type_code != 2:
            raise ValueError("Invalid MTE Addenda: Addenda Type Code must be '02'.")

class POPDetailRecord(Record):
    def __init__(self, line):
        self.record_type_code = line[0:1]
        self.transaction_code = int(line[1:3])
        self.receiving_dfi_identification = line[3:11]
        self.check_digit = int(line[11:12])
        self.dfi_account_number = line[12:29].strip()
        self.amount = float(line[29:39]) / 100  # Assuming the last two digits are cents
        self.check_serial_number = line[39:48].strip()
        self.terminal_city = line[48:52].strip()
        self.terminal_state = line[52:54].strip()
        self.individual_name = line[54:76].strip()
        self.discretionary_data = line[76:78].strip() if line[76:78].strip() else None
        self.addenda_record_indicator = int(line[78:79])
        self.trace_number = int(line[79:94])

    def to_dict(self):
        return {
            'record_type_code': self.record_type_code,
            'transaction_code': self.transaction_code,
            'receiving_dfi_identification': self.receiving_dfi_identification,
            'check_digit': self.check_digit,
            'dfi_account_number': self.dfi_account_number,
            'amount': self.amount,
            'check_serial_number': self.check_serial_number,
            'terminal_city': self.terminal_city,
            'terminal_state': self.terminal_state,
            'individual_name': self.individual_name,
            'discretionary_data': self.discretionary_data,
            'addenda_record_indicator': self.addenda_record_indicator,
            'trace_number': self.trace_number
        }

    def __repr__(self):
        return f"<POPDetailRecord(record_type_code={self.record_type_code}, transaction_code={self.transaction_code}, ...)>"

    def validate(self):
        if self.record_type_code != '6':
            raise ValueError("Invalid POP Entry: Record Type Code must be '6'.")
        # Add more validation rules as needed

class POSEntryDetailRecord(Record):
    def __init__(self, line):
        self.record_type_code = line[0:1]
        self.transaction_code = int(line[1:3])
        self.receiving_dfi_identification = line[3:11]
        self.check_digit = int(line[11:12])
        self.dfi_account_number = line[12:29].strip()
        self.amount = float(line[29:39]) / 100  # Assuming last two digits are cents
        self.individual_identification_number = line[39:54].strip() if line[39:54].strip() else None
        self.individual_name = line[54:76].strip()
        self.card_transaction_type = line[76:78]
        self.addenda_record_indicator = int(line[78:79])
        self.trace_number = int(line[79:94])
    
    def to_dict(self):
        return {
            'record_type_code': self.record_type_code,
            'transaction_code': self.transaction_code,
            'receiving_dfi_identification': self.receiving_dfi_identification,
            'check_digit': self.check_digit,
            'dfi_account_number': self.dfi_account_number,
            'amount': self.amount,
            'individual_identification_number': self.individual_identification_number,
            'individual_name': self.individual_name,
            'card_transaction_type': self.card_transaction_type,
            'addenda_record_indicator': self.addenda_record_indicator,
            'trace_number': self.trace_number
        }


    def __repr__(self):
        return f"<POSEntryDetailRecord(record_type_code={self.record_type_code}, transaction_code={self.transaction_code}, ...)>"

    def validate(self):
        if self.record_type_code != '6':
            raise ValueError("Invalid POS Entry: Record Type Code must be '6'.")
        # You could add more validation logic based on your requirements

class POSAddendaRecord(Record):
    def __init__(self, line):
        self.record_type_code = line[0:1]
        self.addenda_type_code = line[1:3]
        self.reference_info_1 = line[3:10].strip() if line[3:10].strip() else None
        self.reference_info_2 = line[10:13].strip() if line[10:13].strip() else None
        self.terminal_identification_code = line[13:19].strip()
        self.transaction_serial_number = line[19:25].strip()
        self.transaction_date = line[25:29]
        self.authorization_code_or_card_exp_date = line[29:35].strip() if line[29:35].strip() else None
        self.terminal_location = line[35:62].strip()
        self.terminal_city = line[62:77].strip()
        self.terminal_state = line[77:79]
        self.trace_number = int(line[79:94])

    def to_dict(self):
        return {
            'record_type_code': self.record_type_code,
            'addenda_type_code': self.addenda_type_code,
            'reference_info_1': self.reference_info_1,
            'reference_info_2': self.reference_info_2,
            'terminal_identification_code': self.terminal_identification_code,
            'transaction_serial_number': self.transaction_serial_number,
            'transaction_date': self.transaction_date,
            'authorization_code_or_card_exp_date': self.authorization_code_or_card_exp_date,
            'terminal_location': self.terminal_location,
            'terminal_city': self.terminal_city,
            'terminal_state': self.terminal_state,
            'trace_number': self.trace_number
        }


    def __repr__(self):
        return f"<POSAddendaRecord(record_type_code={self.record_type_code}, addenda_type_code={self.addenda_type_code}, ...)>"
    
    def validate(self):
        if self.record_type_code != '7':
            raise ValueError("Invalid POS Addenda: Record Type Code must be '7'.")
        if self.addenda_type_code != '02':
            raise ValueError("Invalid POS Addenda: Addenda Type Code must be '02'.")
        # More validations can be added based on your specific needs

class PPDDetailRecord(Record):
    def __init__(self, line):
        self.record_type_code = line[0:1]
        self.transaction_code = line[1:3]
        self.receiving_dfi_identification = line[3:11]
        self.check_digit = line[11:12]
        self.dfi_account_number = line[12:29].strip() if line[12:29].strip() else None
        self.amount = float(line[29:39]) / 100  # convert to actual dollar amount
        self.individual_identification_number = line[39:54].strip()
        self.individual_name = line[54:76].strip()
        self.discretionary_data = line[76:78].strip() if line[76:78].strip() else None
        self.addenda_record_indicator = line[78:79]
        self.trace_number = int(line[79:94])

    def to_dict(self):
        return {
            'record_type_code': self.record_type_code,
            'transaction_code': self.transaction_code,
            'receiving_dfi_identification': self.receiving_dfi_identification,
            'check_digit': self.check_digit,
            'dfi_account_number': self.dfi_account_number,
            'amount': self.amount,
            'individual_identification_number': self.individual_identification_number,
            'individual_name': self.individual_name,
            'discretionary_data': self.discretionary_data,
            'addenda_record_indicator': self.addenda_record_indicator,
            'trace_number': self.trace_number
        }


    def __repr__(self):
        return f"<PPDDetailRecord(record_type_code={self.record_type_code}, transaction_code={self.transaction_code}, ...)>"

    def validate(self):
        if self.record_type_code != '6':
            raise ValueError("Invalid PPD Detail: Record Type Code must be '6'.")
        # More validations can be added based on your specific needs

class RCKDetailRecord(Record):
    def __init__(self, line):
        self.record_type_code = line[0:1]
        self.transaction_code = line[1:3]
        self.receiving_dfi_identification = line[3:11]
        self.check_digit = line[11:12]
        self.dfi_account_number = line[12:29].strip() if line[12:29].strip() else None
        self.amount = float(line[29:39]) / 100  # convert to actual dollar amount
        self.check_serial_number = line[39:54].strip()
        self.individual_name = line[54:76].strip()
        self.discretionary_data = line[76:78].strip() if line[76:78].strip() else None
        self.addenda_record_indicator = line[78:79]
        self.trace_number = int(line[79:94])

    def to_dict(self):
        return {
            'record_type_code': self.record_type_code,
            'transaction_code': self.transaction_code,
            'receiving_dfi_identification': self.receiving_dfi_identification,
            'check_digit': self.check_digit,
            'dfi_account_number': self.dfi_account_number,
            'amount': self.amount,
            'check_serial_number': self.check_serial_number,
            'individual_name': self.individual_name,
            'discretionary_data': self.discretionary_data,
            'addenda_record_indicator': self.addenda_record_indicator,
            'trace_number': self.trace_number
        }


    def __repr__(self):
        return f"<RCKDetailRecord(record_type_code={self.record_type_code}, transaction_code={self.transaction_code}, ...)>"
        
    def validate(self):
        if self.record_type_code != '6':
            raise ValueError("Invalid RCK Detail: Record Type Code must be '6'.")
        if not self.check_serial_number:
            raise ValueError("Invalid RCK Detail: Check Serial Number must be provided.")
        # More validations can be added based on your specific needs

class SHREntryDetailRecord(Record):
    def __init__(self, line):
        self.record_type_code = line[0:1]
        self.transaction_code = line[1:3]
        self.receiving_dfi_identification = line[3:11]
        self.check_digit = line[11:12]
        self.dfi_account_number = line[12:29].strip() if line[12:29].strip() else None
        self.amount = float(line[29:39]) / 100  # convert to actual dollar amount
        self.card_expiration_date = line[39:43].strip() if line[39:43].strip() else None
        self.document_reference_number = int(line[43:54])
        self.individual_card_account_number = int(line[54:76])
        self.card_transaction_type = line[76:78]
        self.addenda_record_indicator = line[78:79]
        self.trace_number = int(line[79:94])

    def to_dict(self):
        return {
            'record_type_code': self.record_type_code,
            'transaction_code': self.transaction_code,
            'receiving_dfi_identification': self.receiving_dfi_identification,
            'check_digit': self.check_digit,
            'dfi_account_number': self.dfi_account_number,
            'amount': self.amount,
            'card_expiration_date': self.card_expiration_date,
            'document_reference_number': self.document_reference_number,
            'individual_card_account_number': self.individual_card_account_number,
            'card_transaction_type': self.card_transaction_type,
            'addenda_record_indicator': self.addenda_record_indicator,
            'trace_number': self.trace_number
        }

    def __repr__(self):
        return f"<SHREntryDetailRecord(record_type_code={self.record_type_code}, transaction_code={self.transaction_code}, ...)>"

    def validate(self):
        if self.record_type_code != '6':
            raise ValueError("Invalid SHR Detail: Record Type Code must be '6'.")
        if not self.transaction_code:
            raise ValueError("Invalid SHR Detail: Transaction Code must be provided.")
        # Add more validation checks based on your specific needs

class SHRAddendaRecord(Record):
    def __init__(self, line):
        self.record_type_code = line[0:1]
        self.addenda_type_code = line[1:3]
        self.reference_info_1 = line[3:10].strip() if line[3:10].strip() else None
        self.reference_info_2 = line[10:13].strip() if line[10:13].strip() else None
        self.terminal_identification_code = line[13:19].strip() if line[13:19].strip() else None
        self.transaction_serial_number = line[19:25].strip() if line[19:25].strip() else None
        self.transaction_date = line[25:29]
        self.authorization_code_or_card_expiration_date = line[29:35].strip() if line[29:35].strip() else None
        self.terminal_location = line[35:62].strip() if line[35:62].strip() else None
        self.terminal_city = line[62:77].strip() if line[62:77].strip() else None
        self.terminal_state = line[77:79]
        self.trace_number = int(line[79:94])

    def to_dict(self):
        return {
            'record_type_code': self.record_type_code,
            'addenda_type_code': self.addenda_type_code,
            'reference_info_1': self.reference_info_1,
            'reference_info_2': self.reference_info_2,
            'terminal_identification_code': self.terminal_identification_code,
            'transaction_serial_number': self.transaction_serial_number,
            'transaction_date': self.transaction_date,
            'authorization_code_or_card_expiration_date': self.authorization_code_or_card_expiration_date,
            'terminal_location': self.terminal_location,
            'terminal_city': self.terminal_city,
            'terminal_state': self.terminal_state,
            'trace_number': self.trace_number
        }


    def __repr__(self):
        return f"<SHRAddendaRecord(record_type_code={self.record_type_code}, addenda_type_code={self.addenda_type_code}, ...)>"

    def validate(self):
        if self.record_type_code != '7':
            raise ValueError("Invalid SHR Addenda: Record Type Code must be '7'.")
        if self.addenda_type_code != '02':
            raise ValueError("Invalid SHR Addenda: Addenda Type Code must be '02'.")
        # Add more validation checks based on your specific needs

class TELDetailRecord(Record):
    def __init__(self, line):
        self.record_type_code = line[0:1]
        self.transaction_code = line[1:3]
        self.receiving_dfi_identification = line[3:11]
        self.check_digit = line[11:12]
        self.dfi_account_number = line[12:29].strip() if line[12:29].strip() else None
        self.amount = float(line[29:39]) / 100  # Convert to float with two decimal places
        self.individual_identification_number = line[39:54].strip() if line[39:54].strip() else None
        self.individual_name = line[54:76].strip()
        self.payment_type_code = line[76:78].strip() if line[76:78].strip() else None
        self.addenda_record_indicator = line[78:79]
        self.trace_number = int(line[79:94])

    def to_dict(self):
        return {
            'record_type_code': self.record_type_code,
            'transaction_code': self.transaction_code,
            'receiving_dfi_identification': self.receiving_dfi_identification,
            'check_digit': self.check_digit,
            'dfi_account_number': self.dfi_account_number,
            'amount': self.amount,
            'individual_identification_number': self.individual_identification_number,
            'individual_name': self.individual_name,
            'payment_type_code': self.payment_type_code,
            'addenda_record_indicator': self.addenda_record_indicator,
            'trace_number': self.trace_number
        }


    def __repr__(self):
        return f"<TELEntryDetailRecord(record_type_code={self.record_type_code}, transaction_code={self.transaction_code}, ...)>"

    def validate(self):
        if self.record_type_code != '6':
            raise ValueError("Invalid TEL Detail: Record Type Code must be '6'.")
        if not self.transaction_code:
            raise ValueError("Transaction code is required.")
        # Add more validation checks based on your specific needs

class TRCEntryDetailRecord(Record):
    def __init__(self, line):
        self.record_type_code = line[0:1]
        self.transaction_code = line[1:3]
        self.receiving_dfi_identification = line[3:11]
        self.check_digit = line[11:12]
        self.dfi_account_number = line[12:29].strip() if line[12:29].strip() else None
        self.amount = float(line[29:39]) / 100  # Convert to float with two decimal places
        self.check_serial_number = line[39:48].strip() if line[39:48].strip() else None
        self.process_control_field = line[48:54].strip()
        self.item_research_number = line[54:70].strip() if line[54:70].strip() else None
        self.item_type_indicator = line[76:78].strip() if line[76:78].strip() else None
        self.addenda_record_indicator = line[78:79].strip() if line[78:79].strip() else None
        self.trace_number = int(line[79:94])
    
    def to_dict(self):
        return {
            'record_type_code': self.record_type_code,
            'transaction_code': self.transaction_code,
            'receiving_dfi_identification': self.receiving_dfi_identification,
            'check_digit': self.check_digit,
            'dfi_account_number': self.dfi_account_number,
            'amount': self.amount,
            'check_serial_number': self.check_serial_number,
            'process_control_field': self.process_control_field,
            'item_research_number': self.item_research_number,
            'item_type_indicator': self.item_type_indicator,
            'addenda_record_indicator': self.addenda_record_indicator,
            'trace_number': self.trace_number
        }

    def __repr__(self):
        return f"<TRCEntryDetailRecord(record_type_code={self.record_type_code}, transaction_code={self.transaction_code}, ...)>"

    def validate(self):
        if self.record_type_code != '6':
            raise ValueError("Invalid TRC Detail: Record Type Code must be '6'.")
        if not self.transaction_code:
            raise ValueError("Transaction code is required.")
        # Add more validation checks based on your specific needs

class TRXEntryDetailRecord(Record):
    def __init__(self, line):
        self.record_type_code = line[0:1]
        self.transaction_code = line[1:3]
        self.receiving_dfi_identification = line[3:11]
        self.check_digit = line[11:12]
        self.dfi_account_number = line[12:29].strip() if line[12:29].strip() else None
        self.amount = float(line[29:39]) / 100  # Convert to float with two decimal places
        self.identification_number = line[39:54].strip() if line[39:54].strip() else None
        self.num_addenda_records = int(line[54:58])
        self.receiving_company_name_id = line[58:74].strip()
        self.item_type_indicator = line[76:78].strip() if line[76:78].strip() else None
        self.addenda_record_indicator = line[78:79]
        self.trace_number = int(line[79:94])

    def to_dict(self):
        return {
            'record_type_code': self.record_type_code,
            'transaction_code': self.transaction_code,
            'receiving_dfi_identification': self.receiving_dfi_identification,
            'check_digit': self.check_digit,
            'dfi_account_number': self.dfi_account_number,
            'amount': self.amount,
            'identification_number': self.identification_number,
            'num_addenda_records': self.num_addenda_records,
            'receiving_company_name_id': self.receiving_company_name_id,
            'item_type_indicator': self.item_type_indicator,
            'addenda_record_indicator': self.addenda_record_indicator,
            'trace_number': self.trace_number
        }

    def __repr__(self):
        return f"<TRXEntryDetailRecord(record_type_code={self.record_type_code}, transaction_code={self.transaction_code}, ...)>"

    def validate(self):
        if self.record_type_code != '6':
            raise ValueError("Invalid TRX Detail: Record Type Code must be '6'.")
        if not self.transaction_code:
            raise ValueError("Transaction code is required.")
        # Add more validation checks based on your specific needs

class TRXAddendaRecord(Record):
    def __init__(self, line):
        self.record_type_code = line[0:1]
        self.addenda_type_code = line[1:3]
        self.payment_related_information = line[3:83].strip() if line[3:83].strip() else None
        self.addenda_sequence_number = int(line[83:87])
        self.entry_detail_sequence_number = int(line[87:94])

    def to_dict(self):
        return {
            'record_type_code': self.record_type_code,
            'addenda_type_code': self.addenda_type_code,
            'payment_related_information': self.payment_related_information,
            'addenda_sequence_number': self.addenda_sequence_number,
            'entry_detail_sequence_number': self.entry_detail_sequence_number
        }

    def __repr__(self):
        return f"<TRXAddendaRecord(record_type_code={self.record_type_code}, addenda_type_code={self.addenda_type_code}, ...)>"
    
    def validate(self):
        if self.record_type_code != '7':
            raise ValueError("Invalid TRX Addenda: Record Type Code must be '7'.")
        if self.addenda_type_code != '05':
            raise ValueError("Invalid TRX Addenda: Addenda Type Code must be '05'.")
        # Add more validation as needed

class WEBDetailRecord(Record):
    def __init__(self, line):
        self.record_type_code = line[0:1]
        self.transaction_code = line[1:3]
        self.receiving_dfi_identification = line[3:11]
        self.check_digit = int(line[11:12])
        self.dfi_account_number = line[12:29].strip() if line[12:29].strip() else None
        self.amount = float(line[29:39]) / 100  # Convert to dollars from cents
        self.individual_identification_number = line[39:54].strip()
        self.individual_name = line[54:76].strip()
        self.payment_type_code = line[76:78].strip() if line[76:78].strip() else None
        self.addenda_record_indicator = int(line[78:79])
        self.trace_number = int(line[79:94])

    def to_dict(self):
        return {
            'record_type_code': self.record_type_code,
            'transaction_code': self.transaction_code,
            'receiving_dfi_identification': self.receiving_dfi_identification,
            'check_digit': self.check_digit,
            'dfi_account_number': self.dfi_account_number,
            'amount': self.amount,
            'individual_identification_number': self.individual_identification_number,
            'individual_name': self.individual_name,
            'payment_type_code': self.payment_type_code,
            'addenda_record_indicator': self.addenda_record_indicator,
            'trace_number': self.trace_number
        }

    def __repr__(self):
        return f"<WEBDetailRecord(record_type_code={self.record_type_code}, transaction_code={self.transaction_code}, ...)>"

    def validate(self):
        if self.record_type_code != '6':
            raise ValueError("Invalid WEB Detail: Record Type Code must be '6'.")
        # Add more validations, such as for transaction_code, receiving_dfi_identification, etc.

class XCKDetailRecord(Record):
    def __init__(self, line):
        self.record_type_code = line[0:1]
        self.transaction_code = line[1:3]
        self.receiving_dfi_identification = line[3:11]
        self.check_digit = int(line[11:12])
        self.dfi_account_number = line[12:29].strip() if line[12:29].strip() else None
        self.amount = float(line[29:39]) / 100  # Convert to dollars from cents
        self.check_serial_number = line[39:54].strip()
        self.process_control_field = line[54:60].strip() if line[54:60].strip() else None
        self.item_research_number = line[60:76].strip() if line[60:76].strip() else None
        self.discretionary_data = line[76:78].strip() if line[76:78].strip() else None
        self.addenda_record_indicator = int(line[78:79])
        self.trace_number = int(line[79:94])
    
    def to_dict(self):
        return {
            'record_type_code': self.record_type_code,
            'transaction_code': self.transaction_code,
            'receiving_dfi_identification': self.receiving_dfi_identification,
            'check_digit': self.check_digit,
            'dfi_account_number': self.dfi_account_number,
            'amount': self.amount,
            'check_serial_number': self.check_serial_number,
            'process_control_field': self.process_control_field,
            'item_research_number': self.item_research_number,
            'discretionary_data': self.discretionary_data,
            'addenda_record_indicator': self.addenda_record_indicator,
            'trace_number': self.trace_number
        }

    def __repr__(self):
        return f"<XCKDetailRecord(record_type_code={self.record_type_code}, transaction_code={self.transaction_code}, ...)"

    def validate(self):
        if self.record_type_code != '6':
            raise ValueError("Invalid XCK Detail: Record Type Code must be '6'.")
        # More validations here based on other fields.

class IATBatchHeaderRecord(Record):
    def __init__(self, line):
        self.record_type_code = line[0:1]
        self.service_class_code = line[1:4]
        self.iat_indicator = line[4:20].strip()  # Optional, so strip whitespaces
        self.foreign_exchange_indicator = line[20:22]
        self.foreign_exchange_reference_indicator = line[22:23]
        self.foreign_exchange_reference = line[23:38].strip()  # Optional
        self.iso_destination_country_code = line[38:40]
        self.originator_identification = line[40:50].strip()
        self.standard_entry_class_code = line[50:53]
        self.company_entry_description = line[53:63].strip()
        self.iso_originating_currency_code = line[63:66]
        self.iso_destination_currency_code = line[66:69]
        self.effective_entry_date = line[69:75]
        self.settlement_date = line[75:78].strip()  # Filled by ACH Operator
        self.originator_status_code = line[78:79]
        self.gateway_operator_identification = line[79:87]
        self.batch_number = int(line[87:94])

    def to_dict(self):
        return {
            'record_type_code': self.record_type_code,
            'service_class_code': self.service_class_code,
            'iat_indicator': self.iat_indicator,
            'foreign_exchange_indicator': self.foreign_exchange_indicator,
            'foreign_exchange_reference_indicator': self.foreign_exchange_reference_indicator,
            'foreign_exchange_reference': self.foreign_exchange_reference,
            'iso_destination_country_code': self.iso_destination_country_code,
            'originator_identification': self.originator_identification,
            'standard_entry_class_code': self.standard_entry_class_code,
            'company_entry_description': self.company_entry_description,
            'iso_originating_currency_code': self.iso_originating_currency_code,
            'iso_destination_currency_code': self.iso_destination_currency_code,
            'effective_entry_date': self.effective_entry_date,
            'settlement_date': self.settlement_date,
            'originator_status_code': self.originator_status_code,
            'gateway_operator_identification': self.gateway_operator_identification,
            'batch_number': self.batch_number
        }

    def __repr__(self):
        return f"<IATBatchHeaderRecord(record_type_code={self.record_type_code}, service_class_code={self.service_class_code}, ...)"

    def validate(self):
        if self.record_type_code != '5':
            raise ValueError("Invalid IAT Batch Header: Record Type Code must be '5'.")
        if self.service_class_code not in ['200', '220', '225']:
            raise ValueError("Invalid Service Class Code. Must be '200', '220', or '225'")
        # ...other validations...
