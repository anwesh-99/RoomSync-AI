"""
Redistribute preferred PG locations across West Bengal with focus on Kolkata hubs.
"""

import argparse
import json
import random
from pathlib import Path

# West Bengal PG hubs with Kolkata focus
WB_HUBS = [
    {"city": "Kolkata", "locality": "Salt Lake Sector V", "lat": 22.5804, "lng": 88.4378},
    {"city": "Kolkata", "locality": "Salt Lake Sector I", "lat": 22.5910, "lng": 88.4110},
    {"city": "Kolkata", "locality": "Salt Lake Sector II", "lat": 22.5867, "lng": 88.4200},
    {"city": "Kolkata", "locality": "New Town Action Area I", "lat": 22.5855, "lng": 88.4687},
    {"city": "Kolkata", "locality": "New Town Action Area II", "lat": 22.6022, "lng": 88.4795},
    {"city": "Kolkata", "locality": "Jadavpur", "lat": 22.4988, "lng": 88.3718},
    {"city": "Kolkata", "locality": "Kestopur (VIP Road)", "lat": 22.5936, "lng": 88.4239},
    {"city": "Kolkata", "locality": "Gariahat", "lat": 22.5195, "lng": 88.3653},
    {"city": "Kolkata", "locality": "Ballygunge", "lat": 22.5280, "lng": 88.3610},
    {"city": "Kolkata", "locality": "Park Street", "lat": 22.5510, "lng": 88.3524},
    {"city": "Kolkata", "locality": "Bhowanipore", "lat": 22.5325, "lng": 88.3475},
    {"city": "Kolkata", "locality": "Tollygunge", "lat": 22.4930, "lng": 88.3470},
    {"city": "Kolkata", "locality": "Behala", "lat": 22.4980, "lng": 88.3180},
    {"city": "Kolkata", "locality": "Kasba (Ruby)", "lat": 22.5120, "lng": 88.3950},
    {"city": "Kolkata", "locality": "Dum Dum", "lat": 22.6225, "lng": 88.3965},
    {"city": "Kolkata", "locality": "Rajarhat Chinar Park", "lat": 22.6158, "lng": 88.4418},
    {"city": "Howrah", "locality": "Shibpur (IIEST)", "lat": 22.5620, "lng": 88.3050},
    {"city": "Kharagpur", "locality": "IIT Kharagpur Area", "lat": 22.3149, "lng": 87.3105},
    {"city": "Durgapur", "locality": "City Centre", "lat": 23.5204, "lng": 87.3119},
    {"city": "Siliguri", "locality": "Sevoke Road", "lat": 26.7271, "lng": 88.4353},
    {"city": "Kalyani", "locality": "AIIMS Area", "lat": 22.9751, "lng": 88.4344},
]


def parse_args():
    parser = argparse.ArgumentParser(
        description="Evenly redistribute preferred PG locations across West Bengal & Kolkata."
    )
    parser.add_argument(
        "--input",
        default="local_data/users_local.json",
        help="Input JSON file path.",
    )
    parser.add_argument(
        "--output",
        default="local_data/users_local_balanced.json",
        help="Output JSON file path.",
    )
    parser.add_argument(
        "--seed",
        type=int,
        default=42,
        help="Random seed for stable redistribution.",
    )
    return parser.parse_args()


def jitter(val, spread=0.015):
    return round(val + random.uniform(-spread, spread), 6)


def rebalance(users):
    k = len(WB_HUBS)
    for i, user in enumerate(users):
        hub = WB_HUBS[i % k]
        user["city"] = hub["city"]
        user["locality"] = hub["locality"]
        user["latitude"] = jitter(hub["lat"])
        user["longitude"] = jitter(hub["lng"])
        user["preferred_location_source"] = "balanced_west_bengal"


def main():
    args = parse_args()
    random.seed(args.seed)

    in_path = Path(args.input)
    out_path = Path(args.output)

    if not in_path.exists():
        raise FileNotFoundError(f"Input file not found: {in_path}")

    users = json.loads(in_path.read_text(encoding="utf-8"))
    rebalance(users)

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(users, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Rebalanced {len(users)} users across West Bengal hubs -> {out_path}")


if __name__ == "__main__":
    main()
