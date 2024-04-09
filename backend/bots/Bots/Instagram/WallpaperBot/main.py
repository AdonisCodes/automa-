import json
import base64
from instagrapi import Client
from utils import promptGenerator, generateImage
import time
from random import randint
import threading


def load_accounts():
    accounts = {}
    with open("accounts.json", "r") as f:
        accounts = json.load(f)
    return accounts


def process_account(account_id, account_json, accounts):
    print(f"Processing Account: {account_id}")
    if account_json["login"]["cookies_base64"] is not None:
        print("Using Past Cookies to Authenticate...")
        decoded_bytes = base64.b64decode(account_json["login"]["cookies_base64"])
        decoded_string = decoded_bytes.decode("utf-8")
        path = f"/tmp/{account_id}.json"
        with open(path, "w") as f:
            f.write(decoded_string)

        client = Client()
        client.load_settings(path)
    else:
        print("Brand New Login...")
        client = Client()
        client.login(
            account_json["login"]["username"], account_json["login"]["password"]
        )
        client.dump_settings(f"/tmp/{account_id}.json")
        cookies = json.load(open(f"/tmp/{account_id}.json"))
        cookies_base64 = base64.b64encode(json.dumps(cookies).encode("utf-8")).decode(
            "utf-8"
        )
        account_json["login"]["cookies_base64"] = cookies_base64
        with open("accounts.json", "w") as f:
            json.dump(accounts, f)

    schedule = account_json["schedule"]

    def post():
        print("Posting...")
        prompt = promptGenerator(theme=account_json["style"])
        image_path, revised_prompt = generateImage(prompt)
        revised_prompt += " " + account_json["hashtags"]
        print(f"Generated: {revised_prompt}")
        try:
            client.photo_upload(path=image_path, caption=revised_prompt, usertags=[])
        except:
            print("ERROR")
        print(f"Posted: {revised_prompt}")

    while True:
        print(f"Waiting for account {account_id}...")
        time.sleep(randint(schedule - 10, schedule + 10))
        print(f"Time to Post for account {account_id}!")
        post()


def main():
    print("Loading Accounts...")
    accounts = load_accounts()

    threads = []
    for account_id, account_json in accounts.items():
        thread = threading.Thread(
            target=process_account, args=(account_id, account_json, accounts)
        )
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()


if __name__ == "__main__":
    main()
