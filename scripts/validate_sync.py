#!/usr/bin/env python3
from pathlib import Path
import hashlib
import sys

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skill"
PROJECT = ROOT / "project"

FILE_MAP = {
    "references/post-details.md": "来源/【差点后期】.md",
    "references/visual.md": "来源/【差点视觉】.md",
    "references/footage.md": "来源/【差点素材】.md",
    "references/elements.md": "来源/【差点元素】.md",
    "references/clips.md": "来源/【差点片段】.md",
    "references/motion.md": "来源/【差点动效】.md",
    "references/ai-motion-core.md": "来源/【AI动效开发核心经验】.md",
    "references/cover.md": "来源/【差点封面】.md",
    "references/assets.md": "来源/【差点资产】.md",
    "references/qa.md": "来源/【差点质检】.md",
    "references/parallel-execution.md": "来源/【差点并行】.md",
    "references/artifact-output.md": "来源/【差点交付】.md",
    "references/project-state.md": "来源/【差点状态】.md",
}

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

errors = []
for src_rel, dst_rel in FILE_MAP.items():
    src, dst = SKILL / src_rel, PROJECT / dst_rel
    if not src.exists() or not dst.exists():
        errors.append(f"missing: {src_rel} -> {dst_rel}")
    elif digest(src) != digest(dst):
        errors.append(f"mismatch: {src_rel} -> {dst_rel}")

for src in sorted((SKILL / "references" / "styles").glob("*.md")):
    dst = PROJECT / "来源" / "风格" / src.name
    if not dst.exists() or digest(src) != digest(dst):
        errors.append(f"style mismatch: {src.name}")

base = SKILL / "assets" / "workspace-template"
for src in sorted(base.rglob("*")):
    if src.is_file():
        dst = PROJECT / "模板" / src.relative_to(base)
        if not dst.exists() or digest(src) != digest(dst):
            errors.append(f"template mismatch: {src.relative_to(base)}")

if not (PROJECT / "01_项目指令.md").exists():
    errors.append("missing: project/01_项目指令.md")

if errors:
    print("Sync validation failed:")
    for error in errors:
        print(" -", error)
    sys.exit(1)

print("Skill ↔ Project mirror validation passed.")
