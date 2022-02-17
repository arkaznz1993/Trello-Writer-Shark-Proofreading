class CustomFieldOption:
    all_custom_field_options = []

    def __init__(self, id, id_custom_field, field_value):
        self.id = id
        self.id_custom_field = id_custom_field
        self.field_value = field_value
        CustomFieldOption.all_custom_field_options.append(self)

    def __repr__(self):
        return f"CustomFieldOption('{self.id}', '{self.id_custom_field}', '{self.field_value}')"

    @classmethod
    def instantiate_from_list(cls, db_list):
        for row in db_list:
            CustomFieldOption(row[0], row[1], row[2])

    @classmethod
    def get_custom_field_by_id(cls, id):
        for custom_field_option in CustomFieldOption.all_custom_field_options:
            if id == custom_field_option.id:
                return custom_field_option
