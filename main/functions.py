
def generate_form_errors(forms):
    message =""
    for field in forms:
        if field.errors:
            message += field.errors
    for err in forms.non_field_errors():
        message += str(err)

    return message 