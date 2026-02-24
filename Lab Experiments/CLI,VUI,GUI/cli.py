from common import save_response

TASK_PROMPT = "Please describe one short task or goal you're working on:"


def run_cli():
    print("CLI interface — simple task collector")
    name = input("Your name: ").strip()
    if not name:
        name = "(anonymous)"
    print(TASK_PROMPT)
    description = input("Description: ").strip()
    while True:
        rating_raw = input("Rate your satisfaction with this interface (1-5): ").strip()
        try:
            rating = int(rating_raw)
            if 1 <= rating <= 5:
                break
        except Exception:
            pass
        print("Please enter an integer between 1 and 5.")
    save_response("CLI", name, description, rating)
    print("Thanks — response saved.")


if __name__ == '__main__':
    run_cli()
