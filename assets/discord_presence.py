from pypresence import Presence
import datetime as dt
import time


def rich_presence():
    client_id = "1144714449563955302"
    RPC = Presence(client_id)
    RPC.connect()
    RPC.update(
        state="applio.org",
        details="Ultimate voice cloning tool.",
        buttons=[
            {"label": "Home", "url": "https://applio.org"},
            {"label": "Download", "url": "https://applio.org/download"},
        ],
        large_image="logo",
        large_text="experimenting with applio",
        start=dt.datetime.now().timestamp(),
    )
    return RPC


if __name__ == "__main__":
    rpc = rich_presence()

    try:
        while True:
            time.sleep(15)
    except KeyboardInterrupt:
        rpc.close()
