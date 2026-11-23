"""Next Frame agent - Phase 1: prove the 4am schedule and email work."""
import datetime as dt, yaml, zoneinfo
from agent.emailer import send_email

def main():
    cfg = yaml.safe_load(open("config.yaml", encoding="utf-8"))
    tz = zoneinfo.ZoneInfo(cfg["schedule"]["timezone"])
    now = dt.datetime.now(tz).strftime("%Y-%m-%d %H:%M")
    send_email(
        f"{cfg['channel']['name']} agent is alive",
        f"Hello! The agent started at {now} ({cfg['schedule']['timezone']}).\n"
        f"Plan: {cfg['videos_per_day']} videos/day, upload as {cfg['upload']['privacy']}.\n"
        "Phase 1 works. Next: finding viral gaming videos.",
    )
    print("Email sent:", now)

if __name__ == "__main__":
    main()
