"""10-option key for the open/closed amenity flagship (UE-H-01)."""

from __future__ import annotations

CORRECT_KEY = "B"

OPTIONS = {
    "A": "Amenities raise utility and rents in both models by the same amounts.",
    "B": "Closed city: population fixed, u* rises, rents rise with incumbents' WTP. Open city: u* is pinned, in-migration bids up rents until the utility gain is capitalised away from mobile residents; landowners capture the rent. 'Residents are better off' is not a common prediction.",
    "C": "Open city: utility of residents must rise, otherwise nobody would migrate in.",
    "D": "Closed city: rents cannot rise, because population is fixed and so is housing demand.",
    "E": "Perfectly elastic housing supply would make rents rise more in the open city.",
    "F": "The two models are identical if housing supply has any positive slope.",
    "G": "Open-city rents fall because extra people share the amenity.",
    "H": "Closed-city utility cannot rise: a Walrasian housing market absorbs every surplus.",
    "I": "Landowners lose in the open city because construction dilutes rent.",
    "J": "Owner-occupiers make the two models the same, so the commentator is right after a relabelling.",
}


def keyed_option() -> str:
    return CORRECT_KEY
