# create_commits.py
import os
import subprocess
import random
from datetime import datetime, timedelta

# ----- CONFIG -----
n_commits = 122
start = datetime(2024, 9, 1, 0, 0, 0)      # inclusive start
end   = datetime(2025, 1, 31, 23, 59, 59)  # inclusive end
filename = 'commit_history_placeholder.py'
# -------------------

def random_date(start_dt, end_dt):
    """Return a random datetime between start_dt and end_dt (inclusive)."""
    delta = end_dt - start_dt
    # include both endpoints by adding 1 second to range
    rand_seconds = random.randrange(int(delta.total_seconds()) + 1)
    return start_dt + timedelta(seconds=rand_seconds)

def is_git_repo():
    try:
        subprocess.check_output(['git', 'rev-parse', '--is-inside-work-tree'],
                                stderr=subprocess.STDOUT)
        return True
    except subprocess.CalledProcessError:
        return False

if not is_git_repo():
    print('This directory is not a git repository. Run `git init` first and re-run this script.')
    raise SystemExit(1)

# Make sure placeholder file exists initially
if not os.path.exists(filename):
    with open(filename, 'w') as f:
        f.write('# Placeholder for backdated commits\n')

for i in range(n_commits):
    ts = random_date(start, end)
    iso_ts_for_msg = ts.strftime('%Y-%m-%d %H:%M:%S')

    if i < n_commits - 1:
        # append something to file so commit has a change
        with open(filename, 'a') as f:
            f.write(f'# Backdated commit {i+1} at {iso_ts_for_msg}\\n')

        subprocess.check_call(['git', 'add', filename])

        env = os.environ.copy()
        env['GIT_AUTHOR_DATE'] = ts.strftime('%Y-%m-%dT%H:%M:%S')
        env['GIT_COMMITTER_DATE'] = env['GIT_AUTHOR_DATE']

        subprocess.check_call(['git', 'commit', '-m', f'Backdated commit {i+1} ({iso_ts_for_msg})'], env=env)
        print(f'Created backdated commit {i+1} timestamped {iso_ts_for_msg}')

    else:
        # Final commit: remove the file, commit with a backdated timestamp as well
        if os.path.exists(filename):
            os.remove(filename)
        subprocess.check_call(['git', 'add', '-A'])

        env = os.environ.copy()
        env['GIT_AUTHOR_DATE'] = ts.strftime('%Y-%m-%dT%H:%M:%S')
        env['GIT_COMMITTER_DATE'] = env['GIT_AUTHOR_DATE']

        subprocess.check_call(['git', 'commit', '-m', f'Backdated final cleanup commit ({iso_ts_for_msg})'], env=env)
        print(f'Created final backdated cleanup commit timestamped {iso_ts_for_msg}')

print('Done — 122 backdated commits created between', start, 'and', end)