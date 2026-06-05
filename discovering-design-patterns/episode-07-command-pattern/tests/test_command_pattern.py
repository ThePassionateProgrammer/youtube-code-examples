from src.after_example import (
    AuditLog,
    CommandFactory,
    CommandQueue,
    Document,
    DocumentService,
    EmailDocumentCommand,
    SaveDocumentCommand,
)


class FakeDocumentService(DocumentService):
    def __init__(self):
        self.saved_documents = []
        self.printed_documents = []
        self.emails = []

    def save_document(self, document: Document) -> str:
        self.saved_documents.append(document.title)
        return f"fake-saved:{document.title}"

    def print_document(self, document: Document) -> str:
        self.printed_documents.append(document.title)
        return f"fake-printed:{document.title}"

    def email_document(self, document: Document, recipient: str) -> str:
        self.emails.append((document.title, recipient))
        return f"fake-emailed:{document.title}:to:{recipient}"


def test_behavior_command_executes_receiver():
    service = FakeDocumentService()
    document = Document("Catalog")
    command = SaveDocumentCommand(service, document)

    result = command.execute()

    assert result == "fake-saved:Catalog"
    assert service.saved_documents == ["Catalog"]


def test_structure_queue_can_run_commands_and_log_results():
    service = FakeDocumentService()
    document = Document("Catalog")
    audit_log = AuditLog()
    queue = CommandQueue(audit_log)

    queue.add(SaveDocumentCommand(service, document))
    queue.add(EmailDocumentCommand(service, document, "buyer@example.com"))

    results = queue.run_all()

    assert results == [
        "fake-saved:Catalog",
        "fake-emailed:Catalog:to:buyer@example.com",
    ]
    assert audit_log.entries == [
        "save:fake-saved:Catalog",
        "email:fake-emailed:Catalog:to:buyer@example.com",
    ]

def test_selection_factory_creates_command_that_represents_intent():
    service = FakeDocumentService()
    document = Document("Catalog")
    factory = CommandFactory(service, default_recipient="team@example.com")

    command = factory.create("email", document)

    assert isinstance(command, EmailDocumentCommand)
    assert command.name == "email"
    assert command.execute() == "fake-emailed:Catalog:to:team@example.com"


def test_unknown_action_is_rejected_at_selection_boundary():
    factory = CommandFactory(FakeDocumentService())
    document = Document("Catalog")

    try:
        factory.create("delete-everything", document)
    except ValueError as error:
        assert "Unknown action" in str(error)
    else:
        raise AssertionError("Expected ValueError")
