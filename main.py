import requests

from autorization import accounts_manager
from check_bot import check_record


def main():
    accounts_manager.create_driver(username="ku7uzov@gmail.com", password="BpSiTm3!!bhm5q3")
    check_record()

if __name__ == "__main__":
    main()

