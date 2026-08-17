from dataclasses import dataclass, field
from typing import Optional, Union

@dataclass
class EsiJournalEntry:
    type: str
    issuer: str
    amount: Union[int, float]
    bounty: Union[int, float] = field(default=0)
    date: str = field(default_factory=str)

    @property
    def effective_bounty(self) -> Union[int, float]:
        if self.type == 'kill' and self.issuer == 'npc':
            return self.bounty if self.bounty else self.amount
        return self.bounty

    @property
    def effective_amount(self) -> Union[int, float]:
        if self.type == 'kill' and self.issuer == 'npc':
            return self.bounty if self.bounty else self.amount
        return self.amount

    def get_combined_value(self) -> Union[int, float]:
        return self.effective_bounty

    def filter_by_significance(self, threshold: float = 0.0) -> bool:
        return self.get_combined_value() >= threshold

    def __post_init__(self):
        self._type = self.type if self.type else 'journal'
        self._issuer = self.issuer if self.issuer else 'unknown'
        self._bounty = self.bounty if self.bounty else self.amount

    @property
    def raw_bounty(self) -> Union[int, float]:
        return self._bounty

    @property
    def raw_amount(self) -> Union[int, float]:
        return self.amount