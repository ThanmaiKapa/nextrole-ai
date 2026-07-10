import json

from pathlib import Path

PROFILE_PATH = Path("data/master_profile.json")


def profile_exists():
    """
    Returns True only if the profile file exists
    and contains data.
    """
    if not PROFILE_PATH.exists():
        return False

    try:
        with open(PROFILE_PATH, "r") as file:
            profile = json.load(file)

        return bool(profile)

    except (json.JSONDecodeError, FileNotFoundError):
        return False


def load_profile():
    """
    Load the master profile from the JSON file.
    Returns a dictionary if found, otherwise None.
    """
    if profile_exists():
        with open(PROFILE_PATH, "r") as file:
            return json.load(file)

    return None


def save_profile(profile_data):
    """
    Save the master profile to the JSON file.
    """
    PROFILE_PATH.parent.mkdir(parents=True, exist_ok=True)

    with open(PROFILE_PATH, "w") as file:
        json.dump(profile_data, file, indent=4)

def update_profile(section, data):
    """
    Update a specific section of the master profile.
    Creates the profile if it doesn't already exist.
    """

    if profile_exists():
        profile = load_profile()
    else:
        profile = {}

    profile[section] = data

    save_profile(profile)