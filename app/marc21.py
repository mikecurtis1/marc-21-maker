from escape_string import EscapeString


class MARC21Maker:
    def __init__(self, leader_record_status="n", leader_type_of_record="a", leader_bibliographic_level="m"):
        self._marc21_mime_type = "application/marc"

        self._field_terminator = chr(30)
        self._record_terminator = chr(29)
        self._subfield_indicator = chr(31)
        self._subfield_indicator_graphic = "$"

        self._control_field_tags = ['FMT', '001', '003', '005', '006', '007', '008', '009']

        self._leader = ""
        self._data = {}
        self._directory = ""
        self._content = ""
        self._mrc = ""

        self._leader_record_length = "00000"
        self._leader_record_status = leader_record_status
        self._leader_type_of_record = leader_type_of_record
        self._leader_bibliographic_level = leader_bibliographic_level

        self._leader_type_of_control = " "
        self._leader_character_coding_scheme = "a"
        self._leader_indicator_count = "2"
        self._leader_subfield_code_count = "2"
        self._leader_base_address_of_data = "00000"
        self._leader_encoding_level = " "
        self._leader_descriptive_cataloging_form = " "
        self._leader_multipart_resource_record_level = " "
        self._leader_entry_map = "4500"

    def add_control_field(self, tag, content=""):
        if tag not in self._control_field_tags:
            raise Exception(f"{tag} not allowed control field")

        field = content
        self._add_field(tag, field)

    def add_data_field(self, tag, i1, i2, content):
        if len(tag) != 3:
            raise Exception("Tag must be 3 chars")

        field = i1 + i2
        content = self._get_escaped_content(content)
        field += content

        self._add_field(tag, field)

    def _add_field(self, tag, field):
        field += self._field_terminator
        length = self._get_field_length(field)
        start_pos = self._get_next_start_pos()

        self._data[tag + length + start_pos] = field
        self._build_mrc()

    def _get_escaped_content(self, content):
        e = EscapeString(content)
        result = ""

        for arr in e.get_escaped().values():
            if arr["is_escaped"]:
                result += arr["chr"]
            else:
                if arr["chr"] == self._subfield_indicator_graphic:
                    result += self._subfield_indicator
                else:
                    result += arr["chr"]

        return result

    def _get_field_length(self, field):
        return str(len(field)).zfill(4)

    def _get_next_start_pos(self):
        return str(len("".join(self._data.values()))).zfill(5)

    def _build_mrc(self):
        if not self._data:
            raise Exception("No data")

        self._build_directory()
        self._build_contents()

        record_length = self._calculate_record_length()
        self._leader_record_length = record_length
        self._leader_base_address_of_data = self._calculate_base_address()

        self._build_leader()

        self._mrc = self._leader + self._directory + self._content

    def _build_directory(self):
        self._directory = "".join(self._data.keys()) + self._field_terminator

    def _build_contents(self):
        self._content = "".join(self._data.values()) + self._record_terminator

    def _calculate_record_length(self):
        total = 24 + len(self._directory) + len(self._content)
        return str(total).zfill(5)

    def _calculate_base_address(self):
        total = 24 + len(self._directory)
        return str(total).zfill(5)

    def _build_leader(self):
        self._leader = (
            self._leader_record_length +
            self._leader_record_status +
            self._leader_type_of_record +
            self._leader_bibliographic_level +
            self._leader_type_of_control +
            self._leader_character_coding_scheme +
            self._leader_indicator_count +
            self._leader_subfield_code_count +
            self._leader_base_address_of_data +
            self._leader_encoding_level +
            self._leader_descriptive_cataloging_form +
            self._leader_multipart_resource_record_level +
            self._leader_entry_map
        )

    def get_mrc(self):
        return self._mrc
