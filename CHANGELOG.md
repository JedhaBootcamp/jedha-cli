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
