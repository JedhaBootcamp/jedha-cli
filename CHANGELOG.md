<a id='changelog-1.3.2'></a>

# 1.3.2 — 2024-09-03

## Added

- Clean Docker Network and stop previous containers before starting new ones. Fix the network IP range issue.
- Simple test to check labs startup.

<a id='changelog-1.3.1'></a>

# 1.3.1 — 2024-08-28

## Added

- Add new Essentials program labs.

## Changed

- Rename some Essentials program labs name.

<a id='changelog-1.3.0'></a>

# 1.3.0 — 2024-08-27

## Added

- Add new labs for essentials program.

<a id='changelog-1.2.6'></a>

# 1.2.6 — 2024-05-23

## Changed

- Add flag to CMS Dragon lab.

<a id='changelog-1.2.5'></a>

# 1.2.5 — 2024-05-21

## Fixed

- `cms_dragon` DB do not need `cms-dragon-db-volume`.

<a id='changelog-1.2.4'></a>

# 1.2.4 — 2024-05-21

## Changed

- Use same lab network name for every labs.

## Fixed

- Include missing folders for `cms_dragon` lab.

<a id='changelog-1.2.3'></a>

# 1.2.3 — 2024-05-06

## Changed

- Splitted the `vulnerable_and_outdated_software` lab into three separate labs: `cms_dragon`, `golden_club` and `jwt_integrity`.

## Fixed

- CMS Dragon: fixed the database connection issue that was preventing the CMS from starting.

<a id='changelog-1.2.2'></a>

# 1.2.2 — 2024-04-25

## Fixed

- Fix NFS lab.

<a id='changelog-1.2.1'></a>

# 1.2.1 — 2024-04-12

## Added

- 5 basic labs to learn protocols.

<a id='changelog-1.2.0'></a>

# 1.2.0 — 2024-04-05

## Added

- New `dl` command to download a lab without starting it. It solves some issues users may encounter if the download speed is too slow.
- New labs for stealth techniques.

<a id='changelog-1.1.6'></a>

# 1.1.6 — 2024-04-02

## Added

- Add 8 new labs for beginners.

<a id='changelog-1.1.5'></a>

# 1.1.5 — 2024-03-13

## Fixed

- Better docker compose command check: it uses `ls` instead of `ps`.

<a id='changelog-1.1.4'></a>

# 1.1.4 — 2024-03-13

## Fixed

- Sudo-fication of the is docker running check.

<a id='changelog-1.1.3'></a>

# 1.1.3 — 2024-03-13

## Added

- Check if Docker is running on all commands that require it.

<a id='changelog-1.1.2'></a>

# 1.1.2 — 2024-03-12

## Fixed

- While checking the running labs we compare to the known labs to avoid blocking situations if anoter docker compose project is running.

<a id='changelog-1.1.1'></a>

# 1.1.1 — 2024-03-12

## Fixed

- Fix a bug that cause crash because the docker compose command is not well formatted.

<a id='changelog-1.1.0'></a>

# 1.1.0 — 2024-03-12

## Changed

- Changed status command output to display limited information (we avoid giving too many clues). It manages three states: running, stopped, and errors.
- Status command now does not necesarily require an lab name argument. If no lab name is provided, the status command will display the list of all running. Otherwise it will display the status of the lab with the provided name.
- Start command now check if a lab is already running before starting it. If a lab is already running, the start command will return.

## Fixed

- Fix start command that used to run the subsystem command twice resulting in error because the subsystem was already running.
- Add timeout to the version check function to avoid hanging the process when the version check fails.

<a id='changelog-1.0.4'></a>

# 1.0.4 — 2024-02-22

## Fixed

- Missing 'requests' module.

<a id='changelog-1.0.3'></a>

# 1.0.3 — 2024-02-22

## Added

- Function that will check for updates and warn the user if a new version is available.
- Better description and IP addresses for the 'list' command.

## Changed

- Removed the 'ports' for 'expose' instead in Docker Compose YAML files with 2 or more services.

## Fixed

- Syntax errors and minor bugs fixes.

<a id='changelog-1.0.2'></a>

# 1.0.2 — 2024-01-25

## Changed

- sqli environment update.

<a id='changelog-1.0.1'></a>

# 1.0.1 — 2024-01-25

## Changed

- Update linux_privesc environment.
- Publish every ports for each labs.
