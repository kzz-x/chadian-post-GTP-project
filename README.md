# 差点后期 Project

当前版本：**v2.0.0 · 分阶段逐镜头版**。

GitHub：[kzz-x/chadian-post-GTP-project](https://github.com/kzz-x/chadian-post-GTP-project)

Google Drive：[差点后期_Project_版本管理](https://drive.google.com/drive/folders/1DKHPS34vwImUaJQ76d8_sgqCKySu1Br7)
这是用户已反馈“刚刚测试了一下还行”的归档版本；该反馈不等同于全部回归用例或工程功能已验收。

## 使用

1. 将 `project/01_项目指令.md` 正文粘贴到 Project Instructions。
2. 仅将 `project/来源/` 内10个Markdown上传为项目来源，并移除该Project内旧活动版本。
3. 新聊天输入文案，先得到全文逻辑、镜头总览与逐镜头分析卡。
4. “展开03”进入设计，“按确认方案制作03”才制作指定镜头。

`project/02_使用说明与验收.md` 包含完整安装说明、分析示例和实测清单；其未运行标记保留原归档时状态。README、CHANGELOG、VERSION及历史归档均不用上传为Project来源。

## 版本管理

- `main`：当前文件；`VERSION`：明确版本号；`CHANGELOG.md`：每次变化及验证范围。
- GitHub `versions/v1.0.0`：修改前历史快照，仅供对比，含已知问题。
- GitHub `versions/v2.0.0`：本次逐镜头流程快照，12个Project文档与用户收到的v2逐字一致。
- 后续只修措辞或小问题升级补丁号，例如2.0.1；新增能力升级次版本；改变核心交互或不兼容流程升级主版本。
- 每次修改独立提交；经过约定检查后新增版本快照；版本分支按归档约定不移动，不覆盖历史ZIP。GitHub快照分支不是受平台锁定的标签。
- 需要回退：从对应版本分支/提交取文件，或创建revert提交保留修改历史，不以强制推送重写历史。

历史由实际保留的v1、v2文件建立，不伪造早期提交日期。由于当前连接不提供标签创建及原生Git推送，GitHub提交由文件快照重建，提交SHA与原本地记录不同；原始两个提交及 `v1.0.0`、`v2.0.0` 注释标签完整保存在 `archives/chadian-post-project.bundle`，网盘也有备份。GitHub的Tags/Releases尚未创建，版本入口使用上述快照分支。

`archives/` 保存v1/v2安装包、原始Git bundle及校验清单；`project/SHA256SUMS.txt` 校验当前12份Project文档。恢复原始带标签历史可运行：

```bash
git clone archives/chadian-post-project.bundle restored-project
```

README中的仓库归档方式、链接更新不改变v2的Project指令和10份来源。

## 验证与范围

本版本已通过16项文件结构、内容保留及归档检查；18张风格卡专业正文保留。2026-09-05收到用户初步实测反馈“还行”，未提供逐项验收记录，因此12个行为回归用例仍待逐项记录。没有声称图像生成质量或HTML编辑功能已全面验收。

本仓库用于个人工作资料归档；不附加开源许可证。建议GitHub使用Private。仓库已由用户创建为Private；本次上传保持此可见性。
