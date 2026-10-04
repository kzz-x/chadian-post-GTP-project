#!/usr/bin/env python3
from pathlib import Path
import shutil

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

for src_rel, dst_rel in FILE_MAP.items():
    src = SKILL / src_rel
    dst = PROJECT / dst_rel
    dst.parent.mkdir(parents=True, exist_ok=True)
    dst.write_bytes(src.read_bytes())

style_src = SKILL / "references" / "styles"
style_dst = PROJECT / "来源" / "风格"
if style_dst.exists():
    shutil.rmtree(style_dst)
shutil.copytree(style_src, style_dst)

template_src = SKILL / "assets" / "workspace-template"
template_dst = PROJECT / "模板"
if template_dst.exists():
    shutil.rmtree(template_dst)
shutil.copytree(template_src, template_dst)

if not (PROJECT / "01_项目指令.md").exists():
    raise SystemExit("project/01_项目指令.md missing")

print(f"Synced {len(FILE_MAP)} references, split styles, and workspace templates.")
