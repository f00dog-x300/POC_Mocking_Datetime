import datetime


def is_weekend():
    now = datetime.datetime.now()
    if now.weekday() in range(0, 5):
        return True, now.weekday()
    return False

if __name__ == "__main__":
    print(is_weekend())
