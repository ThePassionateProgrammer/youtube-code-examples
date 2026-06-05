"""Before: action lookup table.

This removes a giant conditional, but the behavior still has no identity.
Run:
    python src/before_example.py
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Callable


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

    def email_document(self, document: Document, recipient: str = "team@example.com") -> str:
        document.emailed_to.append(recipient)
        return f"emailed:{document.title}:to:{recipient}"

def perform_with_conditional(action: str, 
    document: Document, service: DocumentService) -> str:
    """The  trap: every new action modifies this conditional."""
    if action == "save":
        return service.save_document(document)
    elif action == "print":
        return service.print_document(document)
    elif action == "email":
        return service.email_document(document)
    raise ValueError(f"Unknown action: {action}")

def perform_with_function_map(action: str, 
    document: Document, service: DocumentService) -> str:
    """Better dispatch, but the action has no identity."""
    actions: dict[str, Callable[[Document], str]] = {
        "save": service.save_document,
        "print": service.print_document,
        "email": service.email_document,
    }
    return actions[action](document)


if __name__ == "__main__":
    doc = Document("CD-ROM Parts Catalog")
    service = DocumentService()
    print(perform_with_function_map("save", doc, service))
    print(doc)
