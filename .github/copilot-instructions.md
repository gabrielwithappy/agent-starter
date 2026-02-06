
# 에이전트 스킬 안내서

당신은 **스킬(Skills)** 이라는 특화된 기능 세트에 접근할 수 있습니다. 각 스킬은 `SKILL.md` 지침 파일, 스크립트, 리소스로 구성된 디렉터리입니다.

## 스킬 구조
각 스킬은 별도의 디렉터리(예: `.agent/skills/<skill-name>/` 또는 `obsidianKMS/.agent/skills/<skill-name>/`)에 위치하며 다음을 포함합니다:

1.  **`SKILL.md` (필수)**: 핵심 지침 파일
    *   **Frontmatter**: `name`, `description` 등 메타데이터 포함
    *   **Body**: 단계별 사용법, 예시, 엣지 케이스 등 상세 설명
2.  **`scripts/` (선택)**: 스킬 동작을 수행하는 실행 스크립트(Python, Bash, Node.js 등)
3.  **`references/` (선택)**: 문서, 템플릿(`FORMS.md`), 도메인 지식 등
4.  **`assets/` (선택)**: 템플릿 및 정적 리소스

## 스킬 사용 방법

1.  **탐색**: 사용자의 요청이 스킬로 처리 가능한 작업(예: "git 플러그인 관리", "Obsidian 노트 업데이트")일 경우, `.agent/skills` 또는 `obsidianKMS/.agent/skills` 디렉터리에서 관련 스킬을 찾으세요.
2.  **활성화**:
    *   관련 스킬의 `SKILL.md`를 `view_file` 도구로 읽으세요.
    *   **중요**: `SKILL.md` 전체 내용을 반드시 읽고, 특히 `scripts/`의 존재와 사용법 인자를 확인하세요.
3.  **실행**:
    *   `SKILL.md`의 "Instructions" 또는 "Workflow" 절차를 정확히 따르세요.
    *   `scripts/` 폴더에 스크립트가 있으면, 별도 지시가 없는 한 직접 단계보다 `run_command`로 실행하는 것을 우선하세요.
    *   frontmatter의 `compatibility` 요구사항을 반드시 확인하세요.

## 예시 워크플로우
사용자가 "새 플러그인 설치"를 요청한 경우:
1.  `plugin-manager/SKILL.md` 위치 확인
2.  설치 명령(예: `python scripts/install.py <url>`)을 찾기 위해 `plugin-manager/SKILL.md` 읽기
3.  `run_command`로 명령 실행

## 스킬 위치
- 기본: `.agent/skills/`

---
모든 답변과 안내는 반드시 한국어로 작성하세요.
