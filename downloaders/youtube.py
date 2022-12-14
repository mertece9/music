# ππππ ππππ ππππ πππππ πππππππππ @SHAILENDRA34 | @HYPER_AD13 | @ShiningOff
# ππππ« πππ«π¨ π©π©π₯π¬ ππ₯π’π¬π‘ ππ¨π§'π­ π«ππ¦π¨π―π π­π‘π’π¬ π₯π’π§π ππ«π¨π¦ π‘ππ«π π


from os import path

from yt_dlp import YoutubeDL

from config import BOT_NAME as bn, DURATION_LIMIT
from helpers.errors import DurationLimitError

ydl_opts = {
    "format": "bestaudio/best",
    "verbose": True,
    "geo-bypass": True,
    "nocheckcertificate": True,
    "outtmpl": "downloads/%(id)s.%(ext)s",
}
ydl = YoutubeDL(ydl_opts)


def download(url: str) -> str:
    info = ydl.extract_info(url, False)
    duration = round(info["duration"] / 60)

    if duration > DURATION_LIMIT:
        raise DurationLimitError(
            f"Video izleme sΔ±nΔ±rΔ± aΕΔ±ldΔ± {DURATION_LIMIT} Dakikadan(s) video sΓΌresi {duration} dakika(s)"
        )

    ydl.download([url])
    return path.join("downloads", f"{info['id']}.{info['ext']}")
