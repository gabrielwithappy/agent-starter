# 에이전트 설정 및 커스터마이징 가이드

이 디렉토리는 GitHub Copilot과 VS Code의 에이전트 동작을 커스터마이징하기 위한 설정 파일들을 관리합니다. 공식 문서에 기반하여 각 구성 요소(Agents, Instructions, Skills)의 역할과 차이점을 설명합니다.

참고 문서:
- [Custom Agents](https://code.visualstudio.com/docs/copilot/customization/custom-agents)
- [Agent Skills](https://code.visualstudio.com/docs/copilot/customization/agent-skills)
- [Custom Instructions](https://code.visualstudio.com/docs/copilot/customization/custom-instructions)

---

## 1. Custom Agents (`agents/`)

**특화된 페르소나 및 작업 모드**

Custom Agent는 특정 작업에 최적화된 "채팅 모드"를 정의합니다. 각 에이전트는 고유한 지침(Instructions)과 사용할 수 있는 도구(Tools) 집합을 가집니다.

- **목적**: 특정 작업(기획, 디버깅, 코드 리뷰 등)에 맞춰 AI의 동작과 권한을 제어합니다.
- **주요 기능**:
  - **도구 제한**: 예를 들어 'Planning Agent'는 코드를 실수로 수정하지 않도록 'read-only' 도구만 사용하게 설정할 수 있습니다.
  - **Handoffs (핸드오프)**: 에이전트 간의 순차적인 워크플로우를 정의합니다. (예: 기획 → 구현 → 리뷰)
- **파일 위치**: `.github/agents/*.agent.md`
- **파일 형식**:
  ```yaml
  ---
  name: planning-agent
  description: 프로젝트 기획 및 설계 전문 에이전트
  tools: ['read', 'search'] 
  handoffs:
    - label: 구현 시작
      agent: implementation-agent
  ---
  ```

## 2. Agent Skills (`skills/`)

**재사용 가능한 기능 및 워크플로우 번들**

Skill은 에이전트에게 "새로운 능력"을 가르치는 것입니다. 단순한 지침을 넘어, 실행 가능한 스크립트, 문서, 템플릿 등을 포함하는 독립적인 패키지입니다.

- **목적**: 테스트, 배포, 다이어그램 생성 등 구체적이고 복잡한 작업을 수행하는 능력을 추가합니다.
- **Instructions와의 차이점**:
  - **Instructions**: "코드를 어떻게 짜야 하는가" (스타일, 규칙)
  - **Skills**: "이 작업을 어떻게 수행하는가" (스크립트 실행, 복잡한 절차)
- **구조**: 각 스킬은 독립된 폴더를 가지며, 그 안에 `SKILL.md`와 리소스(scripts, templates)가 포함됩니다.
- **파일 위치**: `.github/skills/<skill-name>/SKILL.md`
- **예시**: `webapp-testing` 스킬은 Playwright 스크립트와 테스트 절차 문서를 포함하여 에이전트가 브라우저 테스트를 수행할 수 있게 합니다.

## 3. Custom Instructions (`instructions/` or root)

**행동 지침 및 코딩 표준**

Custom Instructions는 에이전트가 코드를 생성하거나 질문에 답할 때 **항상 따 르거나 조건부로 따라야 하는 규칙**을 정의합니다.

- **목적**: 프로젝트의 코딩 스타일, 네이밍 컨벤션, 프레임워크 규칙 등을 준수하도록 합니다.
- **유형**:
  1. **`.github/copilot-instructions.md`**: 워크스페이스 내의 **모든** 채팅 요청에 전역적으로 적용됩니다.
  2. **`*.instructions.md`**: 파일 경로 패턴(glob pattern)에 따라 **조건부**로 적용됩니다. (예: `test/*.ts` 파일에만 적용되는 테스트 규칙)
- **파일 위치**: `.github/copilot-instructions.md` 또는 `.github/instructions/*.instructions.md`
- **파일 형식 (조건부 지침)**:
  ```markdown
  ---
  applyTo: "**/*.test.ts"
  ---
  # 테스트 코드 작성 규칙
  - 모든 테스트는 given-when-then 패턴을 따를 것
  ```

## 4. Workflows (`workflows/`)

**표준 운영 절차 (SOP)**

(Antigravity 프로젝트 컨텍스트) 복잡한 다단계 작업을 일관되게 수행하기 위한 절차서입니다.

- **목적**: 배포, 마이그레이션 등 실수가 없어야 하는 일련의 과정을 단계별로 정의합니다.
- **파일 위치**: `.agent/workflows/*.md`

---

## 요약: 언제 무엇을 사용해야 하나요?

| 구성 요소 | 언제 사용하나요? | 예시 |
|:---:|---|---|
| **Agents** | **"나는 [역활]로서 일하고 싶어"**<br>특정 모드나 페르소나가 필요할 때 | 기획자 모드, 보안 감사관 모드, 디버깅 모드 |
| **Skills** | **"나는 [능력]을 사용하고 싶어"**<br>실행 가능한 도구나 리소스가 포함된 기능이 필요할 때 | Git 관리 도구, 다이어그램 생성기, API 테스터 |
| **Instructions** | **"항상 [규칙]을 지켜줘"**<br>코딩 스타일이나 프로젝트 전반의 규칙이 필요할 때 | 타입스크립트 스타일 가이드, 커밋 메시지 규칙 |

