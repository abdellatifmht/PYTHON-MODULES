from datetime import datetime
from enum import Enum
from typing import Optional
from pydantic import BaseModel, Field, ValidationError, model_validator


class ContactType(str, Enum):
    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(..., min_length=5, max_length=15)
    timestamp: datetime = Field(...)
    location: str = Field(..., min_length=3, max_length=100)
    contact_type: ContactType = Field(...)
    signal_strength: float = Field(..., ge=0.0, le=10.0)
    duration_minutes: int = Field(..., ge=1, le=1440)
    witness_count: int = Field(..., ge=1, le=100)
    message_received: Optional[str] = Field(default=None, max_length=500)
    is_verified: bool = Field(default=False)

    @model_validator(mode='after')
    def validate_contact_rules(self) -> 'AlienContact':
        if not self.contact_id.startswith("AC"):
            raise ValueError(
                f"Contact ID must start with 'AC', got: {self.contact_id}"
            )

        if self.contact_type == ContactType.PHYSICAL and not self.is_verified:
            raise ValueError("Physical contact reports must be verified")

        if (
            self.contact_type == ContactType.TELEPATHIC
            and self.witness_count < 3
        ):
            raise ValueError(
                f"Telepathic contact requires at least 3 witnesses, "
                f"got {self.witness_count}"
            )

        if self.signal_strength > 7.0 and not self.message_received:
            raise ValueError(
                f"Strong signals (>{7.0}) should include received messages. "
                f"Signal strength: {self.signal_strength}"
            )
        return self


def display_contact(contact: AlienContact) -> None:
    print("Valid contact report:")
    print(f"ID: {contact.contact_id}")
    print(f"Type: {contact.contact_type.value}")
    print(f"Location: {contact.location}")
    print(f"Signal: {contact.signal_strength}/10")
    print(f"Duration: {contact.duration_minutes} minutes")
    print(f"Witnesses: {contact.witness_count}")
    if contact.message_received:
        print(f"Message: '{contact.message_received}'")
    print(f"Verified: {'Yes' if contact.is_verified else 'No'}")


def main() -> None:
    print("Alien Contact Log Validation")
    print("=" * 40)

    try:
        valid_contact = AlienContact(
            contact_id="AC_2024_001",
            timestamp=datetime.now(),
            location="Area 51, Nevada",
            contact_type=ContactType.RADIO,
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=5,
            message_received="Greetings from Zeta Reticuli",
            is_verified=True
        )
        display_contact(valid_contact)
    except ValidationError as e:
        print(f"Validation error: {e}")

    print("\n" + "=" * 40)

    try:
        AlienContact(
            contact_id="AC_2025_001",
            timestamp=datetime.now(),
            location="Test Location",
            contact_type=ContactType.TELEPATHIC,
            signal_strength=5.0,
            duration_minutes=30,
            witness_count=2
        )
    except ValidationError as e:
        print("Expected validation error:")
        for error in e.errors():
            print(error['msg'])


if __name__ == "__main__":
    main()
