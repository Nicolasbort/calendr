import hashlib
from time import time

from calendr.settings import OTP_PERIOD, OTP_SECRET
from django_otp.oath import TOTP


def full_name(profile) -> str:
    return f"{profile.first_name} {profile.last_name}".strip()


def generate_totp(profile) -> TOTP:
    raw_secret = f"{OTP_SECRET}-{profile.email}-{str(profile.email_verified)}"
    secret = hashlib.sha256(bytes(raw_secret, "utf-8")).digest()

    totp = TOTP(key=secret, step=int(OTP_PERIOD), digits=6)
    totp.time = time()

    return totp


def generate_token(profile) -> str:
    totp = profile.generate_totp()

    return totp.token()


def verify_token(profile, token: str) -> bool:
    totp = profile.generate_totp()

    return totp.verify(token)
