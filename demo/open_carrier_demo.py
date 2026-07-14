"""Public entry point for the private-source WGY carrier 3D demo."""

import json
import urllib.request
import webbrowser

DEMO_URL = "https://wgy-carrier-operations-demo.wgy577-sortie.workers.dev/"
DEMO_API = f"{DEMO_URL}api/demo"


def get_demo_info(timeout: float = 10.0) -> dict:
    request = urllib.request.Request(
        DEMO_API,
        headers={"Accept": "application/json", "User-Agent": "WGY-Sortie-Project/1.0"},
    )
    with urllib.request.urlopen(request, timeout=timeout) as response:
        return json.load(response)


def open_demo(capture_sortie: bool = False) -> bool:
    target = f"{DEMO_URL}?capture=sortie" if capture_sortie else DEMO_URL
    return webbrowser.open(target)


if __name__ == "__main__":
    print(json.dumps(get_demo_info(), ensure_ascii=False, indent=2))
    open_demo()
