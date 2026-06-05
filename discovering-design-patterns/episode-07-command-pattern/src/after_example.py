"""After: Command Pattern.

The action becomes an object with identity, structure, and testable intent.
Run:
    python src/after_example.py
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Protocol, runtime_checkable


@dataclass
class Document:
    title: str
    saved: bool = False
    printed: bool = False
    emailed_to: list[str] = field(default_factory=list)


class DocumentService:
    def save_document(self, document: Document) -> str:
        document.saved = True
        return f"saved:{document.title}"

    def print_document(self, document: Document) -> str:
        document.printed = True
        return f"printed:{document.title}"

    def email_document(self, document: Document, recipient: str) -> str:
        document.emailed_to.append(recipient)
        return f"emailed:{document.title}:to:{recipient}"


@runtime_checkable
class Command(Protocol):
    """Command interface: every command knows how to execute itself."""

    name: str

    def execute(self) -> str:
        ...


@dataclass(frozen=True)
class SaveDocumentCommand:
    service: DocumentService
    document: Document
    name: str = "save"

    def execute(self) -> str:
        return self.service.save_document(self.document)


@dataclass(frozen=True)
class PrintDocumentCommand:
    service: DocumentService
    document: Document
    name: str = "print"

    def execute(self) -> str:
        return self.service.print_document(self.document)


@dataclass(frozen=True)
class EmailDocumentCommand:
    service: DocumentService
    document: Document
    recipient: str
    name: str = "email"

    def execute(self) -> str:
        return self.service.email_document(self.document, self.recipient)


@dataclass
class AuditLog:
    entries: list[str] = field(default_factory=list)

    def record(self, command: Command, result: str) -> None:
        self.entries.append(f"{command.name}:{result}")


@dataclass
class CommandQueue:
    audit_log: AuditLog
    queued: list[Command] = field(default_factory=list)

    def add(self, command: Command) -> None:
        self.queued.append(command)

    def run_all(self) -> list[str]:
        results: list[str] = []
        while self.queued:
            command = self.queued.pop(0)
            result = command.execute()
            self.audit_log.record(command, result)
            results.append(result)
        return results


class CommandFactory:
    """Selection test target: chooses which command object represents user intent."""

    def __init__(self, service: DocumentService, default_recipient: str = "team@example.com"):
        self.service = service
        self.default_recipient = default_recipient

    def create(self, action: str, document: Document) -> Command:
        if action == "save":
            return SaveDocumentCommand(self.service, document)
        if action == "print":
            return PrintDocumentCommand(self.service, document)
        if action == "email":
            return EmailDocumentCommand(self.service, document, self.default_recipient)
        raise ValueError(f"Unknown action: {action}")


if __name__ == "__main__":
    doc = Document("CD-ROM Parts Catalog")
    service = DocumentService()
    audit_log = AuditLog()
    queue = CommandQueue(audit_log)
    factory = CommandFactory(service)

    queue.add(factory.create("save", doc))
    queue.add(factory.create("email", doc))

    print(queue.run_all())
    print(audit_log.entries)
    print(doc)
