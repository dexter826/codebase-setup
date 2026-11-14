<p align="center">
  <a href="skills/codebase-setup/SKILL.md"><img src="https://img.shields.io/badge/standard-AgentSkill-00cc5c?style=flat-square&labelColor=0a0a0a" alt="standard: AgentSkill" /></a>
  <a href="CHANGELOG.md"><img src="https://img.shields.io/badge/version-0.1.0-00cc5c?style=flat-square&labelColor=0a0a0a" alt="version: 0.1.0" /></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-00cc5c?style=flat-square&labelColor=0a0a0a" alt="license: MIT" /></a>
</p>

# codebase-setup

`codebase-setup` là Agent Skill đưa một repository — mới hoặc đã có — về baseline hoạt động được: source chạy được, quality gate, test, CI, cấu hình container/môi trường, tài liệu phát triển và ngữ cảnh cho AI agent.

Skill vận hành theo **trạng thái**, không theo từng loại input:

```text
Target Baseline = Archetype × Stack × Depth × Modules
Current State   = bằng chứng từ repo + môi trường
Gap             = Target − Current
Setup           = đóng Gap theo thứ tự, có consent
```

Prompt mơ hồ, hội thoại trước đó, PRD/SRD, repository có sẵn hay môi trường máy đều chỉ là nguồn bằng chứng để điền **Setup Brief**. Sau bước này, toàn bộ workflow chạy trên cùng một cấu trúc.

## Tính năng chính

- **Ba chế độ**: `scaffold` cho thư mục mới, `harden` cho repo đã có, `audit-only` cho đánh giá không ghi file.
- **Nhận diện theo archetype**: application, service/API, library/CLI, monorepo, skill package, docs/content và generic.
- **Stack-agnostic**: đọc manifest, lockfile và cấu hình hiện có; tra cứu tài liệu chính thức tại thời điểm chạy thay vì dùng recipe đóng băng.
- **Bốn consent gate riêng biệt**: toolchain, global tool, source init và dependency. Nhóm rỗng được bỏ qua, global install luôn cần phê duyệt riêng.
- **Additive by default**: merge cấu hình, thêm script, giữ nguyên convention; ghi đè file cần consent rõ ràng.
- **AGENTS.md & DESIGN.md có kiểm soát**: luôn preview nội dung và hỏi trước khi tạo (`AGENTS.md` cho ngữ cảnh agent, `DESIGN.md` theo chuẩn Google Stitch cho dự án frontend/UI).
- **Bộ file tiêu chuẩn công nghiệp**: hỗ trợ đầy đủ `README.md`, `LICENSE`, `CHANGELOG.md`, `.editorconfig`, `CONTRIBUTING.md`, `SECURITY.md` theo các chuẩn mở.
- **Báo cáo có bằng chứng**: chỉ báo `pass` cho lệnh thực sự đã chạy, tách lỗi do setup khỏi lỗi có sẵn.

## Chế độ làm việc

| Chế độ | Khi nào dùng | Ghi chú |
| :--- | :--- | :--- |
| **scaffold** | Thư mục đích trống hoặc dự án mới | Có source init qua scaffolder chính thức |
| **harden** | Repo đã có source/manifest nhưng thiếu quality gate, test, CI, docs | Không chạy lại source init |
| **audit-only** | Chỉ cần đánh giá khoảng trống | Không ghi file, không cài dependency |

## Phạm vi

| Trục | Giá trị |
| :--- | :--- |
| Archetype | application · service/API · library/CLI · monorepo · skill package · docs/content · generic |
| Stack | JavaScript/TypeScript · Python · Go · ecosystem khác · generic |
| Depth | minimal · standard (mặc định) · strict |
| Module | structure · quality · tests · delivery · docs · community · design · agent context |

Stack và công cụ cụ thể không được hardcode. Skill đọc repository trước, sau đó tra cứu command/flag hiện hành qua tài liệu chính thức hoặc `--help`, và ghi lại nguồn đã dùng trong báo cáo.

## Cài đặt

### Qua Plugin Marketplace (Claude Code, Codex, Antigravity)

Claude Code:

```text
/plugin marketplace add dexter826/codebase-setup
/plugin install codebase-setup@codebase-setup
```

Codex:

```bash
codex plugin marketplace add dexter826/codebase-setup
codex plugin add codebase-setup@codebase-setup
```

Antigravity:

```bash
agy plugin install https://github.com/dexter826/codebase-setup
```

### Qua Skills CLI (Khuyến dùng)

Cài theo dự án:

```bash
npx skills add dexter826/codebase-setup
```

Cài global (không hỏi xác nhận):

```bash
npx skills add dexter826/codebase-setup -g -y
```

### Cài thủ công bằng Git

Sao chép thư mục `skills/codebase-setup` vào thư mục skills của agent để chỉ cài phần runtime (`SKILL.md`, `references/`, `assets/`), không kéo theo `README.md` hay `evals/`.

Global trên Unix/macOS (`~/.agents/skills`):

```bash
tmp=$(mktemp -d) && git clone --depth 1 https://github.com/dexter826/codebase-setup.git "$tmp" && mkdir -p ~/.agents/skills && rm -rf ~/.agents/skills/codebase-setup && cp -R "$tmp/skills/codebase-setup" ~/.agents/skills/codebase-setup && rm -rf "$tmp"
```

Theo dự án trên Unix/macOS (`.agents/skills`):

```bash
tmp=$(mktemp -d) && git clone --depth 1 https://github.com/dexter826/codebase-setup.git "$tmp" && mkdir -p .agents/skills && rm -rf .agents/skills/codebase-setup && cp -R "$tmp/skills/codebase-setup" .agents/skills/codebase-setup && rm -rf "$tmp"
```

Global trên Windows PowerShell (`$HOME\.agents\skills`):

```powershell
$tmp = Join-Path $env:TEMP "codebase-setup-repo"
Remove-Item -Recurse -Force $tmp -ErrorAction SilentlyContinue
git clone --depth 1 https://github.com/dexter826/codebase-setup.git $tmp
New-Item -ItemType Directory -Force -Path "$HOME\.agents\skills" | Out-Null
Remove-Item -Recurse -Force "$HOME\.agents\skills\codebase-setup" -ErrorAction SilentlyContinue
Copy-Item -Recurse "$tmp\skills\codebase-setup" "$HOME\.agents\skills\codebase-setup"
Remove-Item -Recurse -Force $tmp
```

## Cách dùng

Skill tự kích hoạt khi bạn nhờ setup, khởi tạo, chuẩn hóa hoặc làm cứng một project/repository.

Ví dụ:

```text
Setup project web mới, React + TypeScript, có test và CI.
```

```text
Chuẩn hóa repo này: thêm lint, test, CI và AGENTS.md. Đừng đổi code trong src.
```

```text
Repo này thiếu Dockerfile với .env.example, bổ sung giúp tao.
```

```text
Đọc PRD trong docs/ và dựng khung project theo đó, nhưng đừng implement feature.
```

Trước khi thay đổi repository, skill trình bày kế hoạch gồm file sẽ tạo, file sẽ sửa, command sẽ chạy và vùng không đụng tới. Trong lúc thực thi, các nhóm hành động rủi ro được hỏi riêng. Kết thúc bằng báo cáo có consent log, command đã chạy và kết quả kiểm tra.

## Cấu trúc package

```text
codebase-setup/
├── plugin.json
├── .antigravity-plugin/
│   └── plugin.json
├── .claude-plugin/
│   ├── plugin.json
│   └── marketplace.json
├── .agents/plugins/
│   └── marketplace.json
├── assets/
│   ├── logo-dark.svg
│   ├── logo-light.svg
│   ├── logo-horizontal-dark.svg
│   └── logo-horizontal-light.svg
├── README.md
├── CHANGELOG.md
├── LICENSE
├── evals/
│   ├── evals.json
│   └── files/
└── skills/codebase-setup/
    ├── SKILL.md
    ├── assets/templates/
    │   ├── AGENTS.md
    │   ├── DESIGN.md
    │   ├── .editorconfig
    │   ├── CONTRIBUTING.md
    │   └── SECURITY.md
    └── references/
        ├── intake-and-brief.md
        ├── discovery-and-gap.md
        ├── baseline-and-depth.md
        ├── consent-and-safety.md
        └── verification-and-report.md
```

## Yêu cầu

- Một coding agent hỗ trợ chuẩn AgentSkills.
- Quyền đọc repository đích và quyền ghi vào thư mục sẽ setup.
- Kết nối mạng nếu cần cài dependency, chạy scaffolder hoặc tra cứu tài liệu chính thức.

Skill không tự cài global tool, không sửa `PATH`, không commit thay bạn và không đọc giá trị secret vào file sinh ra hoặc báo cáo.

## Giấy phép

MIT. Xem [LICENSE](LICENSE).
