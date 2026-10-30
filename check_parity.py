#!/usr/bin/env python3
"""Check that a translated content file has the same structure as the Italian one.

Usage: python3 check_parity.py <module>     e.g.  python3 check_parity.py team
Compares content/it/<module>.py with content/en/<module>.py.
"""
import os
import re
import sys

BASE = os.path.dirname(os.path.abspath(__file__))
FIXED_KEYS = {"id", "slug", "name", "photo", "html_lang", "og_locale", "map_hl"}
TAG = re.compile(r"</?[a-zA-Z][^>]*>")
PLACEHOLDER = re.compile(r"\{[a-z_]+\}")
ENTITY = re.compile(r"&[a-z]+;")


def load(lang, mod):
  ns = {}
  path = os.path.join(BASE, "content", lang, mod + ".py")
  with open(path, encoding="utf-8") as f:
    exec(compile(f.read(), path, "exec"), ns)
  return {k: v for k, v in ns.items() if k.isupper()}


def compare(a, b, path, errors, key=None):
  if type(a) is not type(b):
    errors.append(f"{path}: type {type(a).__name__} vs {type(b).__name__}")
    return
  if isinstance(a, dict):
    if list(a) != list(b):
      errors.append(f"{path}: keys differ {sorted(set(a) ^ set(b))}")
      return
    for k in a:
      compare(a[k], b[k], f"{path}.{k}", errors, k)
  elif isinstance(a, (list, tuple)):
    if len(a) != len(b):
      errors.append(f"{path}: length {len(a)} vs {len(b)}")
      return
    for i, (x, y) in enumerate(zip(a, b)):
      compare(x, y, f"{path}[{i}]", errors)
  elif isinstance(a, str):
    if key in FIXED_KEYS and key not in ("html_lang", "og_locale", "map_hl") and a != b:
      errors.append(f"{path}: must stay identical ({a!r} vs {b!r})")
    for name, rx in (("HTML tags", TAG), ("placeholders", PLACEHOLDER),
                     ("entities", ENTITY)):
      if sorted(rx.findall(a)) != sorted(rx.findall(b)):
        errors.append(f"{path}: {name} differ: {rx.findall(a)} vs {rx.findall(b)}")


def main(mod):
  it, en = load("it", mod), load("en", mod)
  errors = []
  if list(it) != list(en):
    errors.append(f"top-level names differ: {list(it)} vs {list(en)}")
  else:
    for k in it:
      compare(it[k], en[k], k, errors)
  if errors:
    print("\n".join(errors))
    sys.exit(1)
  print(f"OK: content/en/{mod}.py matches the structure of content/it/{mod}.py")


if __name__ == "__main__":
  main(sys.argv[1])
