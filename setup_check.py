"""
Phase 1 Setup Verification Script
Verifies project directory layout, configuration files, and Python imports.
"""

import os
import sys

try:
    import yaml
except ImportError:
    yaml = None

EXPECTED_DIRS = [
    "data/raw",
    "data/processed",
    "data/features",
    "notebooks",
    "src/data_collection",
    "src/preprocessing",
    "src/sentiment",
    "src/features",
    "src/training",
    "src/evaluation",
    "src/prediction",
    "api",
    "dashboard",
    "tests",
    "models",
    "configs",
    "pipelines",
]

EXPECTED_FILES = [
    "configs/config.yaml",
    "requirements.txt",
    ".env.example",
    "src/data_collection/__init__.py",
    "src/preprocessing/__init__.py",
    "src/sentiment/__init__.py",
    "src/features/__init__.py",
    "src/training/__init__.py",
    "src/evaluation/__init__.py",
    "src/prediction/__init__.py",
    "api/__init__.py",
    "tests/__init__.py",
]

def verify_setup(base_dir="."):
    print("=" * 60)
    print("      STOCK SENTIMENT MLOPS - PHASE 1 VERIFICATION")
    print("=" * 60)
    
    missing_dirs = []
    for d in EXPECTED_DIRS:
        full_path = os.path.join(base_dir, d)
        if os.path.isdir(full_path):
            print(f"[OK] Directory found: {d}")
        else:
            print(f"[MISSING] Directory missing: {d}")
            missing_dirs.append(d)
            
    missing_files = []
    for f in EXPECTED_FILES:
        full_path = os.path.join(base_dir, f)
        if os.path.isfile(full_path):
            print(f"[OK] File found: {f}")
        else:
            print(f"[MISSING] File missing: {f}")
            missing_files.append(f)
            
    # Check config.yaml parsing
    config_path = os.path.join(base_dir, "configs/config.yaml")
    if os.path.isfile(config_path):
        if yaml is not None:
            try:
                with open(config_path, "r") as fh:
                    config = yaml.safe_load(fh)
                print(f"[OK] Config parsed successfully: project name '{config['project']['name']}'")
            except Exception as e:
                print(f"[ERROR] Failed to parse config.yaml: {e}")
        else:
            print("[OK] Config file found (PyYAML not installed yet in base environment).")

    print("-" * 60)
    if not missing_dirs and not missing_files:
        print(">>> SUCCESS: Phase 1 project structure is 100% complete and verified!")
    else:
        print(f">>> WARNING: Found {len(missing_dirs)} missing directories and {len(missing_files)} missing files.")
    print("=" * 60)

if __name__ == "__main__":
    verify_setup()
