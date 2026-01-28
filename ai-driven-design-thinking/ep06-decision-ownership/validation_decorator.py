class Validator:
    def validate(self, request):
        raise NotImplementedError()

class BaseValidator(Validator):
    def validate(self, request):
        return []

class RequiredFieldValidator(Validator):
    def __init__(self, next_validator):
        self.next = next_validator

    def validate(self, request):
        errors = self.next.validate(request)
        if not request.get("name"):
            errors.append("name is required")
        return errors

class EmailValidator(Validator):
    def __init__(self, next_validator):
        self.next = next_validator

    def validate(self, request):
        errors = self.next.validate(request)
        if "@" not in request.get("email", ""):
            errors.append("invalid email")
        return errors
    
    # Factory 
    def build_validator():
    return RequiredFieldValidator(
        EmailValidator(
            BaseValidator()
        )
    )
    