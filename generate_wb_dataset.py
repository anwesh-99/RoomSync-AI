"""
Generate realistic synthetic user dataset for West Bengal with primary focus on Kolkata.
"""

import json
import random
import uuid
from datetime import datetime, timezone
from pathlib import Path
from werkzeug.security import generate_password_hash

# Set fixed seed for reproducibility
random.seed(42)

# Default password for all synthetic users: password123
DEFAULT_PASSWORD_HASH = generate_password_hash("password123")

# Kolkata PG & Tech/Academic Hubs (Weight: High)
KOLKATA_HUBS = [
    {"city": "Kolkata", "locality": "Salt Lake Sector V", "lat": 22.5804, "lng": 88.4378, "weight": 14},
    {"city": "Kolkata", "locality": "Salt Lake Sector I", "lat": 22.5910, "lng": 88.4110, "weight": 7},
    {"city": "Kolkata", "locality": "Salt Lake Sector II", "lat": 22.5867, "lng": 88.4200, "weight": 6},
    {"city": "Kolkata", "locality": "Salt Lake Sector III", "lat": 22.5695, "lng": 88.4150, "weight": 5},
    {"city": "Kolkata", "locality": "New Town Action Area I", "lat": 22.5855, "lng": 88.4687, "weight": 12},
    {"city": "Kolkata", "locality": "New Town Action Area II", "lat": 22.6022, "lng": 88.4795, "weight": 8},
    {"city": "Kolkata", "locality": "Jadavpur", "lat": 22.4988, "lng": 88.3718, "weight": 10},
    {"city": "Kolkata", "locality": "Kestopur (VIP Road)", "lat": 22.5936, "lng": 88.4239, "weight": 9},
    {"city": "Kolkata", "locality": "Gariahat", "lat": 22.5195, "lng": 88.3653, "weight": 7},
    {"city": "Kolkata", "locality": "Ballygunge", "lat": 22.5280, "lng": 88.3610, "weight": 5},
    {"city": "Kolkata", "locality": "Park Street", "lat": 22.5510, "lng": 88.3524, "weight": 4},
    {"city": "Kolkata", "locality": "Bhowanipore", "lat": 22.5325, "lng": 88.3475, "weight": 5},
    {"city": "Kolkata", "locality": "Tollygunge", "lat": 22.4930, "lng": 88.3470, "weight": 5},
    {"city": "Kolkata", "locality": "Behala", "lat": 22.4980, "lng": 88.3180, "weight": 4},
    {"city": "Kolkata", "locality": "Kasba (Ruby EM Bypass)", "lat": 22.5120, "lng": 88.3950, "weight": 7},
    {"city": "Kolkata", "locality": "Dum Dum", "lat": 22.6225, "lng": 88.3965, "weight": 5},
    {"city": "Kolkata", "locality": "Shyambazar", "lat": 22.6001, "lng": 88.3708, "weight": 4},
    {"city": "Kolkata", "locality": "Rajarhat Chinar Park", "lat": 22.6158, "lng": 88.4418, "weight": 6},
    {"city": "Howrah", "locality": "Shibpur (IIEST)", "lat": 22.5620, "lng": 88.3050, "weight": 5},
    {"city": "Kolkata", "locality": "College Street", "lat": 22.5744, "lng": 88.3639, "weight": 4},
    {"city": "Kolkata", "locality": "Lake Gardens", "lat": 22.5030, "lng": 88.3580, "weight": 4},
    {"city": "Kolkata", "locality": "Garia", "lat": 22.4630, "lng": 88.3920, "weight": 4},
]

# Other Major West Bengal Academic & Tech Hubs (Weight: Low)
OTHER_WB_HUBS = [
    {"city": "Kharagpur", "locality": "IIT Kharagpur Campus Area", "lat": 22.3149, "lng": 87.3105, "weight": 4},
    {"city": "Durgapur", "locality": "City Centre & Bidhannagar", "lat": 23.5204, "lng": 87.3119, "weight": 4},
    {"city": "Siliguri", "locality": "Sevoke Road & Matigara", "lat": 26.7271, "lng": 88.4353, "weight": 3},
    {"city": "Kalyani", "locality": "AIIMS & University Area", "lat": 22.9751, "lng": 88.4344, "weight": 3},
    {"city": "Asansol", "locality": "Ushagram & College Area", "lat": 23.6739, "lng": 86.9524, "weight": 2},
    {"city": "Burdwan", "locality": "Golapbag Campus Area", "lat": 23.2324, "lng": 87.8615, "weight": 2},
]

ALL_HUBS = KOLKATA_HUBS + OTHER_WB_HUBS
HUB_WEIGHTS = [h["weight"] for h in ALL_HUBS]

# Realistic Bengal Home Districts/Cities
HOME_LOCATIONS = [
    {"home_city": "Kolkata", "home_locality": "Baghbazar", "lat": 22.6025, "lng": 88.3670},
    {"home_city": "Kolkata", "home_locality": "Baranagar", "lat": 22.6366, "lng": 88.3748},
    {"home_city": "Howrah", "home_locality": "Salkia", "lat": 22.6050, "lng": 88.3450},
    {"home_city": "Hooghly", "home_locality": "Serampore", "lat": 22.7523, "lng": 88.3426},
    {"home_city": "Hooghly", "home_locality": "Chinsurah", "lat": 22.9015, "lng": 88.3941},
    {"home_city": "North 24 Parganas", "home_locality": "Barasat", "lat": 22.7218, "lng": 88.4831},
    {"home_city": "North 24 Parganas", "home_locality": "Barrackpore", "lat": 22.7667, "lng": 88.3667},
    {"home_city": "South 24 Parganas", "home_locality": "Sonarpur", "lat": 22.4411, "lng": 88.4336},
    {"home_city": "South 24 Parganas", "home_locality": "Baruipur", "lat": 22.3654, "lng": 88.4325},
    {"home_city": "Nadia", "home_locality": "Krishnanagar", "lat": 23.4013, "lng": 88.4955},
    {"home_city": "Nadia", "home_locality": "Ranaghat", "lat": 23.1804, "lng": 88.5800},
    {"home_city": "Burdwan", "home_locality": "Burdwan Sadar", "lat": 23.2324, "lng": 87.8615},
    {"home_city": "Birbhum", "home_locality": "Bolpur Santiniketan", "lat": 23.6800, "lng": 87.6800},
    {"home_city": "Midnapore", "home_locality": "Kharagpur", "lat": 22.3460, "lng": 87.2320},
    {"home_city": "Midnapore", "home_locality": "Tamluk", "lat": 22.3000, "lng": 87.9200},
    {"home_city": "Bankura", "home_locality": "Bankura Town", "lat": 23.2325, "lng": 87.0715},
    {"home_city": "Purulia", "home_locality": "Purulia Town", "lat": 23.3321, "lng": 86.3652},
    {"home_city": "Murshidabad", "home_locality": "Berhampore", "lat": 24.1042, "lng": 88.2514},
    {"home_city": "Malda", "home_locality": "English Bazar", "lat": 25.0108, "lng": 88.1411},
    {"home_city": "Siliguri", "home_locality": "Pradhan Nagar", "lat": 26.7271, "lng": 88.4353},
    {"home_city": "Jalpaiguri", "home_locality": "Jalpaiguri Town", "lat": 26.5400, "lng": 88.7200},
    {"home_city": "Darjeeling", "home_locality": "Kurseong", "lat": 26.8800, "lng": 88.2800},
    {"home_city": "Cooch Behar", "home_locality": "Cooch Behar Sadar", "lat": 26.3239, "lng": 89.4510},
]

MALE_FIRST_NAMES = [
    "Sourav", "Anirban", "Sayan", "Subham", "Debojyoti", "Aritra", "Arpan", "Aniket",
    "Indranil", "Pritam", "Tathagata", "Kaushik", "Ritwik", "Subhankar", "Dipanjan",
    "Sagnik", "Arkadipta", "Rajdeep", "Nilanjan", "Abhirup", "Debjit", "Sayantan",
    "Rohan", "Arnab", "Somnath", "Shounak", "Tridib", "Souvik", "Avik", "Pratik",
    "Joydeep", "Siddhartha", "Sudipto", "Snehasis", "Abhishek", "Anupam", "Debashis",
    "Tanmoy", "Pinaki", "Shuvro", "Kallol", "Mainak", "Souradeep", "Saptarshi"
]

FEMALE_FIRST_NAMES = [
    "Ananya", "Debolina", "Riya", "Arpita", "Madhumita", "Shreya", "Sneha", "Payel",
    "Poulomi", "Oindrila", "Sampurna", "Titas", "Ishani", "Sreemoyee", "Priyanka",
    "Sarmistha", "Ditipriya", "Soumili", "Paulomi", "Moumita", "Tanusree", "Rituparna",
    "Swagata", "Trisha", "Debashree", "Aindrila", "Chandrima", "Sohini", "Ushasi",
    "Sanchari", "Monami", "Anwesha", "Bidisha", "Subhashree", "Pritha", "Madhurima",
    "Dipti", "Barnali", "Paramita", "Soma", "Adrija", "Bhaswati", "Dipanwita"
]

SURNAMES = [
    "Banerjee", "Chatterjee", "Mukherjee", "Ghosh", "Bose", "Das", "Roy", "Sen",
    "Dutta", "Bhattacharya", "Sarkar", "Ganguly", "Chakraborty", "Guha", "Mitra",
    "Majumdar", "Saha", "Pal", "Dey", "Poddar", "Mondal", "Biswas", "Choudhury",
    "Basak", "Bhowmick", "Samanta", "Mandal", "Kundu", "Bera", "Bagchi", "Lahiri",
    "Adhikary", "Nath", "Ghosh Dastidar", "Mallick", "Karmakar", "Barman"
]

OCCUPATIONS = [
    ("working_professional", 0.62),
    ("student", 0.30),
    ("freelancer", 0.08),
]

STUDENT_BIOS = [
    "M.Tech student at Jadavpur University. Quiet, focused on research, looking for clean sharing room.",
    "B.Tech 3rd year at Techno Main Salt Lake. Night owl coder, loves filter coffee and gaming.",
    "Pursuing Masters in Economics at Calcutta University. Tidy, avid reader, respects quiet study hours.",
    "PhD scholar at IIEST Shibpur. Simple lifestyle, vegetarian, needs peaceful room near metro / transport.",
    "Design student at NIFT Kolkata. Creative, friendly, loves music and art, tidy and organized.",
    "Medical intern at Medical College Kolkata. Unpredictable duty hours, neat and quiet flatmate preferred.",
    "Student at St. Xavier's College (Autonomous). Extrovert, loves football and music on weekends, responsible.",
    "Research intern at ISI Kolkata. Highly disciplined, quiet study routine, non-smoker, easy to get along with.",
    "Heritage Institute computer science undergrad. Looking for a flatmate in Kasba / Ruby or Salt Lake.",
    "MBA student in Salt Lake. Early riser, gym enthusiast, organized and practical about splitting expenses."
]

PRO_BIOS = [
    "Software Engineer at TCS Gitobitan, Sector V. Clean, non-smoker, looking for flat near Karunamoyee/New Town.",
    "Senior Consultant at PwC Sector V. Mostly working late hours or hybrid, quiet and respectful of personal space.",
    "Data Analyst at Cognizant Bantala. Weekend cyclist, cook on Sundays, non-drinker looking for tidy flatmate.",
    "Frontend Developer at Wipro Sector V. Loves football, late-night coding, easy-going and communicative.",
    "UI/UX Designer working at an IT park in New Town. Clean aesthetic, plant lover, respectful and quiet flatmate.",
    "Full-stack engineer at a fintech startup in Salt Lake. Early riser, works out daily, non-smoker, clean.",
    "Digital Marketer based in Park Street. Social on weekends, loves street food and photography, neat room.",
    "Accountant at an MNC in Dalhousie/BBD Bagh. Calm, organized, early sleep schedule, looking around Gariahat.",
    "Operations Lead at Flipkart Kolkata hub. Reliable, clear communicator, handles chores diligently.",
    "Cybersecurity analyst at IBM Sector V. Night owl, chill demeanor, keeps common areas spotless."
]

FREELANCE_BIOS = [
    "Freelance Content Strategist & Writer. Works from home, needs fast Wi-Fi and quiet atmosphere.",
    "Independent Web Developer. Flexible sleep schedule, minimalist lifestyle, tidy and independent.",
    "Freelance Photographer & Filmmaker. Traveling occasionally, creative, loves cinema and good conversations."
]

ALL_INTERESTS = [
    "coding", "football", "cricket", "reading", "photography", "travel", "gaming", "music",
    "fitness", "cooking", "movies", "chess", "art", "classical music", "guitar", "cycling",
    "anime", "board games", "writing", "hiking", "swimming", "coffee brewing"
]

def generate_phone():
    prefix = random.choice(["9830", "9831", "9836", "9433", "8981", "9051", "7003", "8420", "9874"])
    suffix = "".join([str(random.randint(0, 9)) for _ in range(6)])
    return f"{prefix}{suffix}"

def jitter(val, spread=0.015):
    """Jitter coordinate within ~1-1.8km radius"""
    return round(val + random.uniform(-spread, spread), 6)

def generate_user(idx, total):
    # Gender distribution: 52% male, 45% female, 3% non-binary
    g_rand = random.random()
    if g_rand < 0.52:
        gender = "male"
        first_name = random.choice(MALE_FIRST_NAMES)
        gender_pref = random.choices(["male", "any", "female"], weights=[0.65, 0.30, 0.05])[0]
    elif g_rand < 0.97:
        gender = "female"
        first_name = random.choice(FEMALE_FIRST_NAMES)
        gender_pref = random.choices(["female", "any", "male"], weights=[0.80, 0.18, 0.02])[0]
    else:
        gender = "non-binary"
        first_name = random.choice(MALE_FIRST_NAMES + FEMALE_FIRST_NAMES)
        gender_pref = "any"

    surname = random.choice(SURNAMES)
    full_name = f"{first_name} {surname}"

    # Target PG Hub (mainly Kolkata)
    hub = random.choices(ALL_HUBS, weights=HUB_WEIGHTS)[0]
    city = hub["city"]
    locality = hub["locality"]
    lat = jitter(hub["lat"])
    lng = jitter(hub["lng"])

    # Home origin
    home = random.choice(HOME_LOCATIONS)
    home_city = home["home_city"]
    home_locality = home["home_locality"]
    home_lat = jitter(home["lat"], spread=0.02)
    home_lng = jitter(home["lng"], spread=0.02)

    # Occupation
    occ_choice = random.choices([o[0] for o in OCCUPATIONS], weights=[o[1] for o in OCCUPATIONS])[0]
    if occ_choice == "student":
        age = random.randint(20, 25)
        bio = random.choice(STUDENT_BIOS)
        budget_min = random.choice([3500, 4000, 4500, 5000])
        budget_max = budget_min + random.choice([2000, 2500, 3000, 3500])
    elif occ_choice == "working_professional":
        age = random.randint(23, 33)
        bio = random.choice(PRO_BIOS)
        budget_min = random.choice([5500, 6000, 7000, 8000, 9000, 10000])
        budget_max = budget_min + random.choice([3000, 4000, 5000, 6000])
    else:
        age = random.randint(22, 30)
        bio = random.choice(FREELANCE_BIOS)
        budget_min = random.choice([5000, 6000, 7000])
        budget_max = budget_min + random.choice([3000, 4000])

    # 10 ML Feature Vector Dimensions (1-5 Likert scale)
    sleep_sched = random.choices([1, 2, 3, 4, 5], weights=[0.15, 0.20, 0.25, 0.25, 0.15])[0]
    cleanliness = random.choices([1, 2, 3, 4, 5], weights=[0.05, 0.15, 0.30, 0.35, 0.15])[0]
    noise_tol = random.choices([1, 2, 3, 4, 5], weights=[0.15, 0.25, 0.30, 0.20, 0.10])[0]
    cooking_freq = random.choices([1, 2, 3, 4, 5], weights=[0.25, 0.25, 0.25, 0.15, 0.10])[0]
    guest_freq = random.choices([1, 2, 3, 4, 5], weights=[0.25, 0.30, 0.25, 0.15, 0.05])[0]
    workout = random.choices([1, 2, 3, 4, 5], weights=[0.20, 0.25, 0.25, 0.20, 0.10])[0]
    intro_extro = random.choices([1, 2, 3, 4, 5], weights=[0.15, 0.25, 0.25, 0.25, 0.10])[0]
    comm_style = random.choices([1, 2, 3, 4, 5], weights=[0.10, 0.20, 0.35, 0.25, 0.10])[0]
    conflict_res = random.choices([1, 2, 3, 4, 5], weights=[0.10, 0.20, 0.35, 0.25, 0.10])[0]
    social_bat = random.choices([1, 2, 3, 4, 5], weights=[0.15, 0.25, 0.30, 0.20, 0.10])[0]

    # Lifestyle categorical choices
    smoking = random.choices(["never", "occasionally", "regularly"], weights=[0.75, 0.18, 0.07])[0]
    drinking = random.choices(["never", "occasionally", "regularly"], weights=[0.60, 0.32, 0.08])[0]
    veg_nonveg = random.choices(["nonveg", "eggetarian", "veg", "vegan"], weights=[0.78, 0.10, 0.10, 0.02])[0]
    pet_friendly = random.choices([True, False], weights=[0.35, 0.65])[0]
    move_in = random.choices(["immediate", "within_month", "flexible"], weights=[0.30, 0.50, 0.20])[0]

    # Interests (pick 3-5)
    num_interests = random.randint(3, 5)
    user_interests = random.sample(ALL_INTERESTS, num_interests)

    # Clean username for email
    clean_fn = "".join(c for c in first_name.lower() if c.isalnum())
    clean_sn = "".join(c for c in surname.lower() if c.isalnum())
    email = f"{clean_fn}.{clean_sn}{idx:02d}@cohabit.wb"

    uid = uuid.uuid4().hex

    return {
        "_id": uid,
        "full_name": full_name,
        "age": age,
        "gender": gender,
        "occupation": occ_choice,
        "phone": generate_phone(),
        "bio": bio,
        "city": city,
        "locality": locality,
        "latitude": lat,
        "longitude": lng,
        "home_city": home_city,
        "home_locality": home_locality,
        "home_latitude": home_lat,
        "home_longitude": home_lng,
        "sleep_schedule": sleep_sched,
        "cleanliness": cleanliness,
        "noise_tolerance": noise_tol,
        "cooking_frequency": cooking_freq,
        "guest_frequency": guest_freq,
        "workout_habit": workout,
        "introversion_extroversion": intro_extro,
        "communication_style": comm_style,
        "conflict_resolution": conflict_res,
        "social_battery": social_bat,
        "budget_min": budget_min,
        "budget_max": budget_max,
        "smoking": smoking,
        "drinking": drinking,
        "veg_nonveg": veg_nonveg,
        "gender_preference": gender_pref,
        "pet_friendly": pet_friendly,
        "preferred_move_in": move_in,
        "interests": user_interests,
        "avatar_url": None,
        "profile_complete": True,
        "is_looking": True,
        "email": email,
        "password_hash": DEFAULT_PASSWORD_HASH,
        "preferred_location_source": "west_bengal_kolkata",
        "created_at": datetime.now(timezone.utc).isoformat(),
        "_chat_messages": []
    }

def main():
    total_users = 520
    users = [generate_user(i + 1, total_users) for i in range(total_users)]

    # Paths to write
    base_dir = Path(__file__).resolve().parent
    balanced_path = base_dir / "local_data" / "users_local_balanced.json"
    local_path = base_dir / "local_data" / "users_local.json"
    synthesis_path = base_dir / "Ideas and Dataset Synthesis" / "west_bengal_users.json"
    legacy_odisha_path = base_dir / "Ideas and Dataset Synthesis" / "odisha_users.json"

    for p in [balanced_path, local_path, synthesis_path, legacy_odisha_path]:
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(json.dumps(users, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"Written {len(users)} users to {p.relative_to(base_dir)}")

    kolkata_count = sum(1 for u in users if u["city"] == "Kolkata")
    print(f"\nSuccessfully generated {len(users)} West Bengal users!")
    print(f" - Kolkata users: {kolkata_count} ({kolkata_count/len(users)*100:.1f}%)")
    print(f" - Other WB hubs: {len(users) - kolkata_count}")
    print(f" - All users have password: password123")

if __name__ == "__main__":
    main()
