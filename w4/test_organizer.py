import pytest
from organizer import determine_destination_folder

def test_determine_destination_folder_documents():
    """Verifies that common document extensions correctly route to the Documents category."""
    assert determine_destination_folder(".pdf") == "Documents"
    assert determine_destination_folder(".txt") == "Documents"
    assert determine_destination_folder(".csv") == "Documents"

def test_determine_destination_folder_images():
    """Verifies that graphic file extensions correctly route to the Images category."""
    assert determine_destination_folder(".png") == "Images"
    assert determine_destination_folder(".jpg") == "Images"
    assert determine_destination_folder(".gif") == "Images"

def test_determine_destination_folder_unmatched():
    """Verifies that unknown or unmapped extensions safely fall back to the Others folder."""
    assert determine_destination_folder(".xyz") == "Others"
    assert determine_destination_folder(".bak") == "Others"