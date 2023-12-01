def fetch_input(day, year=2023):
    import os

    import requests
    from dotenv import load_dotenv

    if os.path.exists(f"d{day}.txt"):
        print(f"Input for day {day} already fetched\n")
        return True

    load_dotenv()
    session = os.getenv('SESSION')
    url = f"https://adventofcode.com/{year}/day/{day}/input"
    headers = {'Cookie': f'session={session}'}
    print(f"Fetching input for day {day}...")
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print(f"Error fetching input for day {day}.")
        print(response.text)
        return False
    with open(f"d{day}.txt", 'w') as f:
        f.write(response.text)
        print(f"Input for day {day} saved to {f.name}.\n")
        return True