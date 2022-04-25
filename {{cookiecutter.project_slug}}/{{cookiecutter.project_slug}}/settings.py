import glob
import os
import sys
import warnings

import environ

PROJECT_DIR = os.path.dirname(__file__)
PROJECT_NAME = os.path.basename(PROJECT_DIR)
BASE_DIR = os.path.dirname(PROJECT_DIR)

env = environ.Env()
secret_env_path = os.path.join(PROJECT_DIR, "env/.env")
if os.path.isfile(secret_env_path):
    environ.Env.read_env(secret_env_path)
environ.Env.read_env(
    env.str("DJANGO_ENV_PATH", os.path.join(PROJECT_DIR, "env/env.default"))
)

SITE_ID = env.int("SITE_ID")

conffiles = glob.glob(os.path.join(os.path.dirname(__file__), "settings", "*.conf"))

for f in sorted(conffiles):
    with open(os.path.abspath(f)) as fp:
        exec(compile(fp.read(), os.path.abspath(f), "exec"))
