# Next Frame agent - Phase 1 setup (about 10 minutes, free)

## A. Gmail app password (so the agent can email you)
1. Google Account > Security > turn on **2-Step Verification**.
2. Search "App passwords" in your Google Account, create one named `nextframe`, copy the 16 letters.

## B. Put the project on GitHub
1. github.com > **New repository** > name `next-frame-agent` > **Private** > Create.
2. Click **uploading an existing file**, drag in everything from this folder
   (keep the `.github` folder - if it won't upload, create the file
   `.github/workflows/daily.yml` with "Add file > Create new file" and paste it in).

## C. Add two secrets
Repo > Settings > Secrets and variables > Actions > **New repository secret**:
- `EMAIL_ADDRESS` = your Gmail address
- `EMAIL_APP_PASSWORD` = the 16-letter app password

## D. Test now
Repo > **Actions** tab > "Next Frame daily agent" > **Run workflow**.
In about a minute you should get the email "Next Frame agent is alive".

## Notes
- It then runs by itself every day at 4:00 AM Pakistan time, even with your laptop off.
- GitHub can start scheduled runs 10-30 minutes late.
- GitHub pauses schedules after 60 days with no repo activity; open the repo now and then.
