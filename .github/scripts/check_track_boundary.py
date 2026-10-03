import os
import sys
import yaml


def main():
    author = os.environ["PR_AUTHOR"]
    changed = [f for f in os.environ["CHANGED_FILES"].splitlines() if f.strip()]

    with open(".github/track-owners.yml") as f:
        owners = yaml.safe_load(f) or {}

    allowed_track = None
    for track, usernames in owners.items():
        if author in (usernames or []):
            allowed_track = track
            break

    if allowed_track is None:
        print(f"info: @{author} isn't listed in .github/track-owners.yml -- "
              f"skipping the track-boundary check (organizers/admins exempt).")
        return 0

    allowed_prefix = f"tracks/{allowed_track}/"
    violations = [f for f in changed if not f.startswith(allowed_prefix)]

    if violations:
        print(f"BLOCKED: @{author} is assigned to '{allowed_track}' but this "
              f"PR also touches files outside tracks/{allowed_track}/:")
        for v in violations:
            print(f"  - {v}")
        print("\nOpen a separate PR for changes outside your track.")
        return 1

    print(f"OK: all changed files are inside tracks/{allowed_track}/.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
