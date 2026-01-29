---
description: 'GitHub Copilot용 사용자 지정 에이전트 파일을 생성하기 위한 지침'
applyTo: '**/*.agent.md'
---

# 사용자 지정 에이전트 파일 지침

GitHub Copilot에서 특정 개발 작업을 위한 전문적인 지식을 제공하는 효과적이고 유지 관리 가능한 사용자 지정 에이전트 파일을 생성하기 위한 지침입니다.

## 프로젝트 컨텍스트

- 타겟 독자: GitHub Copilot용 사용자 지정 에이전트를 생성하는 개발자
- 파일 형식: YAML frontmatter가 포함된 Markdown
- 파일 명명 규칙: 하이픈이 포함된 소문자 (예: `test-specialist.agent.md`)
- 위치: `.github/agents/` 디렉토리 (리포지토리 수준) 또는 `agents/` 디렉토리 (조직/엔터프라이즈 수준)
- 목적: 특정 작업에 대해 맞춤형 전문 지식, 도구 및 지침을 갖춘 전문 에이전트 정의
- 공식 문서: https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/create-custom-agents

## 필수 Frontmatter

모든 에이전트 파일에는 다음 필드가 포함된 YAML frontmatter가 있어야 합니다:

```yaml
---
description: '에이전트 목적 및 기능에 대한 간략한 설명'
name: '에이전트 표시 이름'
tools: ['read', 'edit', 'search']
model: 'Claude Sonnet 4.5'
target: 'vscode'
infer: true
---
```

### 핵심 Frontmatter 속성

#### **description** (필수)
- 작은따옴표로 묶인 문자열로, 에이전트의 목적과 도메인 전문 지식을 명확하게 명시
- 간결하고(50-150자) 실행 가능해야 함
- 예시: `'테스트 커버리지, 품질 및 테스트 모범 사례에 중점'`

#### **name** (선택 사항)
- UI에 표시될 에이전트 이름
- 생략 시, 파일 이름( `.md` 또는 `.agent.md` 제외)이 기본값이 됨
- 제목 표기법(Title Case)을 사용하고 설명적이어야 함
- 예시: `'Testing Specialist'`

#### **tools** (선택 사항)
- 에이전트가 사용할 수 있는 도구 이름 또는 별칭 목록
- 쉼표로 구분된 문자열 또는 YAML 배열 형식 지원
- 생략 시, 에이전트는 사용 가능한 모든 도구에 액세스 가능
- 자세한 내용은 아래 "도구 구성" 섹션 참조

#### **model** (강력 권장)
- 에이전트가 사용할 AI 모델 지정
- VS Code, JetBrains IDE, Eclipse, Xcode에서 지원됨
- 예시: `'Claude Sonnet 4.5'`, `'gpt-4'`, `'gpt-4o'`
- 에이전트 복잡성 및 필요한 기능에 따라 선택

#### **target** (선택 사항)
- 타겟 환경 지정: `'vscode'` 또는 `'github-copilot'`
- 생략 시, 두 환경 모두에서 에이전트 사용 가능
- 에이전트에 환경별 기능이 있는 경우 사용

#### **infer** (선택 사항)
- 컨텍스트에 따라 Copilot이 이 에이전트를 자동으로 사용할지 여부를 제어하는 부울 값
- 생략 시 기본값: `true`
- 수동 에이전트 선택이 필요한 경우 `false`로 설정

#### **metadata** (선택 사항, GitHub.com 전용)
- 에이전트 주석을 위한 이름-값 쌍이 있는 객체
- 예시: `metadata: { category: 'testing', version: '1.0' }`
- VS Code에서는 지원되지 않음

#### **mcp-servers** (선택 사항, 조직/엔터프라이즈 전용)
- 이 에이전트만 사용할 수 있는 MCP 서버 구성
- 조직/엔터프라이즈 수준 에이전트에서만 지원됨
- "MCP 서버 구성" 섹션 참조

#### **handoffs** (선택 사항, VS Code 전용)
- 제안된 다음 단계와 함께 에이전트 간 전환을 유도하는 가이드 순차 워크플로우 활성화
- 각 핸드오프 구성 목록에는 타겟 에이전트와 선택적 프롬프트 지정
- 채팅 응답 완료 후, 사용자가 다음 에이전트로 이동할 수 있는 핸드오프 버튼이 나타남
- VS Code에서만 지원됨 (버전 1.106+)
- 자세한 내용은 아래 "핸드오프 구성" 섹션 참조

## 핸드오프 구성

핸드오프를 사용하면 사용자 지정 에이전트 간에 원활하게 전환되는 가이드 순차 워크플로우를 만들 수 있습니다. 이는 사용자가 다음 단계로 이동하기 전에 각 단계를 검토하고 승인할 수 있는 다단계 개발 워크플로우를 조정하는 데 유용합니다.

### 일반적인 핸드오프 패턴

- **계획 → 구현**: 계획 에이전트에서 계획을 생성한 후, 코딩을 시작하기 위해 구현 에이전트로 핸드오프
- **구현 → 검토**: 구현 완료 후, 품질 및 보안 문제를 확인하기 위해 코드 검토 에이전트로 전환
- **실패하는 테스트 작성 → 통과하는 테스트 작성**: 실패하는 테스트를 생성한 후, 해당 테스트를 통과시키는 코드를 구현하기 위해 핸드오프
- **조사 → 문서화**: 주제를 조사한 후, 가이드를 작성하기 위해 문서화 에이전트로 전환

### 핸드오프 Frontmatter 구조

에이전트 파일의 YAML frontmatter에서 `handoffs` 필드를 사용하여 핸드오프를 정의합니다:

```yaml
---
description: '에이전트에 대한 간략한 설명'
name: '에이전트 이름'
tools: ['search', 'read']
handoffs:
  - label: 구현 시작
    agent: implementation
    prompt: '위에서 설명한 계획을 구현하세요.'
    send: false
  - label: 코드 검토
    agent: code-review
    prompt: '구현 내용의 품질과 보안 문제를 검토해 주세요.'
    send: false
---
```

### 핸드오프 속성

목록의 각 핸드오프에는 다음 속성이 포함되어야 합니다:

| 속성 | 유형 | 필수 | 설명 |
|------|------|------|------|
| `label` | string | 예 | 채팅 인터페이스의 핸드오프 버튼에 표시되는 텍스트 |
| `agent` | string | 예 | 전환할 타겟 에이전트 식별자 (이름 또는 `.agent.md` 없는 파일명) |
| `prompt` | string | 아니요 | 타겟 에이전트의 채팅 입력창에 미리 채워질 프롬프트 텍스트 |
| `send` | boolean | 아니요 | `true`인 경우, 프롬프트를 타겟 에이전트에게 자동으로 전송 (기본값: `false`) |

### 핸드오프 동작

- **버튼 표시**: 채팅 응답이 완료되면 핸드오프 버튼이 대화형 제안으로 나타납니다.
- **컨텍스트 보존**: 사용자가 핸드오프 버튼을 선택하면, 대화 컨텍스트가 유지된 채로 타겟 에이전트로 전환됩니다.
- **미리 채워진 프롬프트**: `prompt`가 지정된 경우, 타겟 에이전트의 채팅 입력창에 미리 채워져 나타납니다.
- **수동 vs 자동**: `send: false`인 경우 사용자가 미리 채워진 프롬프트를 검토하고 수동으로 전송해야 하며, `send: true`인 경우 자동으로 전송됩니다.

### 핸드오프 구성 지침

#### 핸드오프 사용 시기

- **다단계 워크플로우**: 복잡한 작업을 전문 에이전트 간에 분할할 때
- **품질 게이트**: 구현 단계 사이에 검토 단계를 보장할 때
- **가이드 프로세스**: 구조화된 개발 프로세스를 통해 사용자를 안내할 때
- **기술 전환**: 계획/설계에서 구현/테스트 전문가로 이동할 때

#### 모범 사례

- **명확한 레이블**: 다음 단계를 명확하게 나타내는 행동 지향적인 레이블 사용
  - ✅ 좋음: "구현 시작", "보안 검토", "테스트 작성"
  - ❌ 피할 것: "다음", "에이전트로 이동", "작업 수행"

- **관련성 있는 프롬프트**: 완료된 작업을 참조하는 컨텍스트 인식 프롬프트 제공
  - ✅ 좋음: `'위에서 설명한 계획을 구현하세요.'`
  - ❌ 피할 것: 컨텍스트 없는 일반적인 프롬프트

- **선별적 사용**: 가능한 모든 에이전트에 대한 핸드오프를 만들지 말고, 논리적 워크플로우 전환에 집중
  - 에이전트당 가장 관련성 높은 다음 단계 2~3개로 제한
  - 워크플로우 흐름상 자연스럽게 이어지는 에이전트에 대해서만 핸드오프 추가

- **에이전트 의존성**: 핸드오프 생성 전 타겟 에이전트가 존재하는지 확인
  - 존재하지 않는 에이전트로의 핸드오프는 조용히 무시됨
  - 핸드오프가 예상대로 작동하는지 테스트

- **프롬프트 내용**: 프롬프트는 간결하고 실행 가능하게 작성
  - 내용 중복 없이 현재 에이전트의 작업을 참조
  - 타겟 에이전트에 필요한 컨텍스트 제공

### 예시: 전체 워크플로우

다음은 핸드오프를 사용하여 전체 워크플로우를 생성하는 3개 에이전트의 예시입니다:

**계획 에이전트** (`planner.agent.md`):
```yaml
---
description: '새로운 기능 또는 리팩토링을 위한 구현 계획 생성'
name: 'Planner'
tools: ['search', 'read']
handoffs:
  - label: 계획 구현
    agent: implementer
    prompt: '위에서 설명한 계획을 구현하세요.'
    send: false
---
# Planner Agent
당신은 계획 전문가입니다. 당신의 작업은 다음과 같습니다:
1. 요구 사항 분석
2. 작업을 논리적 단계로 분할
3. 상세 구현 계획 생성
4. 테스트 요구 사항 식별

코드를 작성하지 마세요 - 계획 수립에만 집중하세요.
```

**구현 에이전트** (`implementer.agent.md`):
```yaml
---
description: '계획 또는 사양에 따라 코드 구현'
name: 'Implementer'
tools: ['read', 'edit', 'search', 'execute']
handoffs:
  - label: 구현 검토
    agent: reviewer
    prompt: '이 구현의 코드 품질, 보안 및 모범 사례 준수 여부를 검토해 주세요.'
    send: false
---
# Implementer Agent
당신은 구현 전문가입니다. 당신의 작업은 다음과 같습니다:
1. 제공된 계획 또는 사양을 따름
2. 깔끔하고 유지 관리 가능한 코드 작성
3. 적절한 주석 및 문서 포함
4. 프로젝트 코딩 표준 준수

솔루션을 완전하고 철저하게 구현하세요.
```

**검토 에이전트** (`reviewer.agent.md`):
```yaml
---
description: '품질, 보안 및 모범 사례에 대한 코드 검토'
name: 'Reviewer'
tools: ['read', 'search']
handoffs:
  - label: 계획으로 돌아가기
    agent: planner
    prompt: '위의 피드백을 검토하고 새로운 계획이 필요한지 결정하세요.'
    send: false
---
# Code Review Agent
당신은 코드 검토 전문가입니다. 당신의 작업은 다음과 같습니다:
1. 코드 품질 및 유지 관리 가능성 확인
2. 보안 문제 및 취약점 식별
3. 프로젝트 표준 준수 확인
4. 개선 사항 제안

구현에 대해 건설적인 피드백을 제공하세요.
```

이 워크플로우를 통해 개발자는 다음을 수행할 수 있습니다:
1. Planner 에이전트로 시작하여 상세 계획 생성
2. Implementer 에이전트로 핸드오프하여 계획에 따른 코드 작성
3. Reviewer 에이전트로 핸드오프하여 구현 확인
4. 중대한 문제가 발견되면 선택적으로 다시 계획 단계로 핸드오프

### 버전 호환성

- **VS Code**: 핸드오프는 VS Code 1.106 이상에서 지원됨
- **GitHub.com**: 현재 지원되지 않음; 에이전트 전환 워크플로우는 다른 메커니즘 사용
- **기타 IDE**: 지원이 제한적이거나 없음; 최대 호환성을 위해 VS Code 구현에 집중

## 도구 구성

### 도구 사양 전략

**모든 도구 활성화** (기본값):
```yaml
# tools 속성을 완전히 생략하거나 다음을 사용:
tools: ['*']
```

**특정 도구 활성화**:
```yaml
tools: ['read', 'edit', 'search', 'execute']
```

**MCP 서버 도구 활성화**:
```yaml
tools: ['read', 'edit', 'github/*', 'playwright/navigate']
```

**모든 도구 비활성화**:
```yaml
tools: []
```

### 표준 도구 별칭

모든 별칭은 대소문자를 구분하지 않습니다:

| 별칭 | 대체 이름 | 카테고리 | 설명 |
|------|-----------|----------|------|
| `execute` | shell, Bash, powershell | 쉘 실행 | 적절한 쉘에서 명령 실행 |
| `read` | Read, NotebookRead, view | 파일 읽기 | 파일 내용 읽기 |
| `edit` | Edit, MultiEdit, Write, NotebookEdit | 파일 편집 | 파일 편집 및 수정 |
| `search` | Grep, Glob, search | 코드 검색 | 파일 또는 파일 내 텍스트 검색 |
| `agent` | custom-agent, Task | 에이전트 호출 | 다른 사용자 지정 에이전트 호출 |
| `web` | WebSearch, WebFetch | 웹 액세스 | 웹 콘텐츠 가져오기 및 검색 |
| `todo` | TodoWrite | 작업 관리 | 작업 목록 생성 및 관리 (VS Code 전용) |

### 기본 제공 MCP 서버 도구

**GitHub MCP Server**:
```yaml
tools: ['github/*']  # 모든 GitHub 도구
tools: ['github/get_file_contents', 'github/search_repositories']  # 특정 도구
```
- 기본적으로 모든 읽기 전용 도구 사용 가능
- 토큰 범위는 소스 리포지토리로 지정됨

**Playwright MCP Server**:
```yaml
tools: ['playwright/*']  # 모든 Playwright 도구
tools: ['playwright/navigate', 'playwright/screenshot']  # 특정 도구
```
- 로컬 호스트에만 액세스하도록 구성됨
- 브라우저 자동화 및 테스트에 유용

### 도구 선택 모범 사례

- **최소 권한의 원칙**: 에이전트 목적에 필요한 도구만 활성화
- **보안**: 명시적으로 필요한 경우가 아니면 `execute` 액세스 제한
- **집중**: 도구가 적을수록 에이전트 목적이 명확해지고 성능이 향상됨
- **문서화**: 복잡한 구성에 특정 도구가 필요한 이유를 주석으로 설명

## 서브 에이전트 호출 (에이전트 오케스트레이션)

에이전트는 **에이전트 호출 도구**(`agent` 도구)를 사용하여 다른 에이전트를 호출함으로써 다단계 워크플로우를 조정할 수 있습니다.

권장되는 접근 방식은 **프롬프트 기반 오케스트레이션**입니다:
- 오케스트레이터는 자연어로 단계별 워크플로우를 정의합니다.
- 각 단계는 전문 에이전트에게 위임됩니다.
- 오케스트레이터는 필수 컨텍스트(예: 기본 경로, 식별자)만 전달하며, 각 서브 에이전트는 도구/제약 조건을 위해 자체 `.agent.md` 사양을 읽어야 합니다.

### 작동 방식

1) 오케스트레이터의 도구 목록에 `agent`를 포함하여 에이전트 호출을 활성화합니다:

```yaml
tools: ['read', 'edit', 'search', 'agent']
```

2) 각 단계에서 다음을 제공하여 서브 에이전트를 호출합니다:
- **에이전트 이름** (사용자가 선택/호출하는 식별자)
- **에이전트 사양 경로** (읽고 따라야 할 `.agent.md` 파일)
- **최소 공유 컨텍스트** (예: `basePath`, `projectName`, `logFile`)

### 프롬프트 패턴 (권장)

서브 에이전트가 예측 가능하게 동작하도록 모든 단계에 일관된 "래퍼 프롬프트"를 사용하세요:

```text
이 단계는 "<AGENT_SPEC_PATH>"에 정의된 에이전트 "<AGENT_NAME>"으로 수행해야 합니다.

중요:
- 전체 .agent.md 사양(도구, 제약 조건, 품질 표준)을 읽고 적용하세요.
- 기본 경로 "<BASE_PATH>"에서 "<WORK_UNIT_NAME>" 작업을 수행하세요.
- 이 기본 경로 아래에서 필요한 읽기/쓰기를 수행하세요.
- 명확한 요약(수행한 작업 + 생성/수정된 파일 + 문제점)을 반환하세요.
```

선택 사항: 추적 가능성을 위해 경량의 구조화된 래퍼가 필요한 경우, 프롬프트에 작은 JSON 블록을 포함하세요(여전히 사람이 읽을 수 있고 도구에 구애받지 않음):

```text
{
  "step": "<STEP_ID>",
  "agent": "<AGENT_NAME>",
  "spec": "<AGENT_SPEC_PATH>",
  "basePath": "<BASE_PATH>"
}
```

### 오케스트레이터 구조 (일반적으로 유지)

유지 관리 가능한 오케스트레이터를 위해 다음 구조적 요소를 문서화하세요:

- **동적 매개변수**: 사용자로부터 추출되는 값 (예: `projectName`, `fileName`, `basePath`).
- **서브 에이전트 레지스트리**: 각 단계를 `agentName` + `agentSpecPath`에 매핑하는 목록/테이블.
- **단계 순서**: 명시적 순서 (Step 1 → Step N).
- **트리거 조건** (선택 사항이지만 권장됨): 단계가 실행되는 시점과 건너뛰는 시점 정의.
- **로깅 전략** (선택 사항이지만 권장됨): 각 단계 후 업데이트되는 단일 로그/보고서 파일.

오케스트레이터 프롬프트 내에 오케스트레이션 "코드"(JavaScript, Python 등)를 포함하지 마세요. 결정론적이고 도구 주도적인 조정을 선호하세요.

### 기본 패턴

각 단계 호출을 다음과 같이 구조화하세요:

1. **단계 설명**: 명확한 한 줄 목적 (로그 및 추적용)
2. **에이전트 신원**: `agentName` + `agentSpecPath`
3. **컨텍스트**: 작고 명시적인 변수 집합 (경로, ID, 환경 이름)
4. **예상 출력**: 생성/업데이트할 파일 및 작성 위치
5. **반환 요약**: 서브 에이전트에게 짧고 구조화된 요약 반환 요청

### 예시: 다단계 처리

```text
Step 1: 원시 입력 데이터 변환
Agent: data-processor
Spec: .github/agents/data-processor.agent.md
Context: projectName=${projectName}, basePath=${basePath}
Input: ${basePath}/raw/
Output: ${basePath}/processed/
Expected: write ${basePath}/processed/summary.md

Step 2: 처리된 데이터 분석 (Step 1 출력에 의존)
Agent: data-analyst
Spec: .github/agents/data-analyst.agent.md
Context: projectName=${projectName}, basePath=${basePath}
Input: ${basePath}/processed/
Output: ${basePath}/analysis/
Expected: write ${basePath}/analysis/report.md
```

### 핵심 포인트

- **프롬프트에 변수 전달**: 모든 동적 값에 `${variableName}` 사용
- **프롬프트 집중**: 각 서브 에이전트에 대해 명확하고 구체적인 작업 지시
- **반환 요약**: 각 서브 에이전트는 수행한 작업을 보고해야 함
- **순차 실행**: 출력/입력 간에 의존성이 존재할 때 순서대로 단계 실행
- **오류 처리**: 종속 단계로 진행하기 전에 결과 확인

### ⚠️ 도구 가용성 요구 사항

**중요**: 서브 에이전트에 특정 도구(예: `edit`, `execute`, `search`)가 필요한 경우, 오케스트레이터는 자체 `tools` 목록에 해당 도구를 포함해야 합니다. 서브 에이전트는 상위 오케스트레이터가 사용할 수 없는 도구에 액세스할 수 없습니다.

**예시**:
```yaml
# 서브 에이전트가 파일 편집, 명령 실행 또는 코드 검색을 해야 하는 경우
tools: ['read', 'edit', 'search', 'execute', 'agent']
```

오케스트레이터의 도구 권한은 호출된 모든 서브 에이전트에 대한 상한선 역할을 합니다. 모든 서브 에이전트가 필요한 도구를 갖출 수 있도록 도구 목록을 신중하게 계획하세요.

### ⚠️ 중요한 제한 사항

**서브 에이전트 오케스트레이션은 대규모 데이터 처리에 적합하지 않습니다.** 다음과 같은 경우 다단계 서브 에이전트 파이프라인 사용을 피하세요:
- 수백 또는 수천 개의 파일 처리
- 대규모 데이터 세트 처리
- 대규모 코드베이스에 대한 일괄 변환 수행
- 5~10개 이상의 순차 단계 조정

각 서브 에이전트 호출은 지연 시간과 컨텍스트 오버헤드를 추가합니다. 대용량 처리의 경우, 단일 에이전트 내에 로직을 직접 구현하세요. 오케스트레이션은 집중적이고 관리 가능한 데이터 세트에 대한 전문 작업을 조정하는 데에만 사용하세요.

## 에이전트 프롬프트 구조

Frontmatter 아래의 Markdown 내용은 에이전트의 행동, 전문 지식 및 지침을 정의합니다. 잘 구조화된 프롬프트에는 일반적으로 다음이 포함됩니다:

1. **에이전트 정체성 및 역할**: 에이전트가 누구이며 주된 역할은 무엇인지
2. **핵심 책임**: 에이전트가 수행하는 특정 작업
3. **접근 방식 및 방법론**: 에이전트가 작업을 수행하는 방식
4. **지침 및 제약 조건**: 해야 할 일/피해야 할 일 및 품질 표준
5. **출력 기대치**: 예상되는 출력 형식 및 품질

### 프롬프트 작성 모범 사례

- **구체적이고 직접적으로**: 명령형("분석하라", "생성하라") 사용; 모호한 용어 피하기
- **경계 정의**: 범위 제한 및 제약 조건을 명확하게 명시
- **컨텍스트 포함**: 도메인 전문 지식 설명 및 관련 프레임워크 참조
- **행동에 집중**: 에이전트가 어떻게 생각하고 일해야 하는지 설명
- **구조화된 형식 사용**: 헤더, 글머리 기호 및 목록을 사용하여 프롬프트를 스캔하기 쉽게 만들기

## 변수 정의 및 추출

에이전트는 동적 매개변수를 정의하여 사용자 입력에서 값을 추출하고 에이전트의 행동 및 서브 에이전트 통신 전반에 걸쳐 사용할 수 있습니다. 이를 통해 사용자 제공 데이터에 적응하는 유연하고 상황 인식적인 에이전트가 가능해집니다.

### 변수 사용 시기

**다음과 같은 경우 변수를 사용하세요**:
- 에이전트 행동이 사용자 입력에 의존할 때
- 동적 값을 서브 에이전트에 전달해야 할 때
- 다양한 컨텍스트에서 에이전트를 재사용하고 싶을 때
- 매개변수화된 워크플로우가 필요할 때
- 사용자 제공 컨텍스트를 추적하거나 참조해야 할 때

**예시**:
- 사용자 프롬프트에서 프로젝트 이름 추출
- 파이프라인 처리를 위한 인증 이름 캡처
- 파일 경로 또는 디렉토리 식별
- 구성 옵션 추출
- 기능 이름 또는 모듈 식별자 파싱

### 변수 선언 패턴

에이전트 프롬프트 초반에 변수 섹션을 정의하여 예상 매개변수를 문서화하세요:

```markdown
# Agent Name

## Dynamic Parameters

- **Parameter Name**: 설명 및 사용법
- **Another Parameter**: 추출 및 사용 방법

## Your Mission

[PARAMETER_NAME]을(를) 처리하여 [task]를 달성하세요.
```

### 변수 추출 방법

#### 1. **명시적 사용자 입력**
프롬프트에서 변수가 감지되지 않으면 사용자에게 제공하도록 요청하세요:

```markdown
## Your Mission

코드베이스를 분석하여 프로젝트를 처리하세요.

### Step 1: 프로젝트 식별
프로젝트 이름이 제공되지 않은 경우, **사용자에게 다음을 질문하세요**:
- 프로젝트 이름 또는 식별자
- 기본 경로 또는 디렉토리 위치
- 구성 유형 (해당되는 경우)

이 정보를 사용하여 모든 후속 작업을 맥락화하세요.
```

#### 2. **프롬프트에서 암시적 추출**
사용자의 자연어 입력에서 변수를 자동으로 추출하세요:

```javascript
// 예시: 사용자 입력에서 인증 이름 추출
const userInput = "내 인증 처리해줘";

// 핵심 정보 추출
const certificationName = extractCertificationName(userInput);
// 결과: "내 인증"

const basePath = `certifications/${certificationName}`;
// 결과: "certifications/내 인증"
```

#### 3. **컨텍스트 기반 변수 해결**
파일 컨텍스트 또는 워크스페이스 정보를 사용하여 변수를 도출하세요:

```markdown
## Variable Resolution Strategy

1. **사용자 프롬프트에서**: 먼저 사용자 입력에서 명시적인 언급을 찾습니다.
2. **파일 컨텍스트에서**: 현재 파일 이름 또는 경로를 확인합니다.
3. **워크스페이스에서**: 워크스페이스 폴더 또는 활성 프로젝트를 사용합니다.
4. **설정에서**: 구성 파일을 참조합니다.
5. **사용자에게 질문**: 다른 방법이 실패하면 누락된 정보를 요청합니다.
```

### 에이전트 프롬프트에서 변수 사용

#### 지침에서의 변수 대체

에이전트 프롬프트에 템플릿 변수를 사용하여 동적으로 만듭니다:

```markdown
# Agent Name

## Dynamic Parameters
- **Project Name**: ${projectName}
- **Base Path**: ${basePath}
- **Output Directory**: ${outputDir}

## Your Mission

`${basePath}`에 위치한 **${projectName}** 프로젝트를 처리하세요.

## Process Steps

1. 입력 읽기: `${basePath}/input/`
2. 프로젝트 구성에 따라 파일 처리
3. 결과 쓰기: `${outputDir}/`
4. 요약 보고서 생성

## Quality Standards

- **${projectName}**에 대한 프로젝트별 코딩 표준 유지
- 디렉토리 구조 준수: `${basePath}/[structure]`
```

#### 서브 에이전트에 변수 전달

서브 에이전트를 호출할 때, 프롬프트의 대체된 변수를 통해 모든 컨텍스트를 전달하세요. 전체 파일 내용이 아닌 **경로와 식별자**를 전달하는 것을 선호하세요.

예시 (프롬프트 템플릿):

```text
이 단계는 ".github/agents/documentation-writer.agent.md"에 정의된 에이전트 "documentation-writer"로 수행해야 합니다.

중요:
- 전체 .agent.md 사양을 읽고 적용하세요.
- 프로젝트: "${projectName}"
- 기본 경로: "projects/${projectName}"
- 입력: "projects/${projectName}/src/"
- 출력: "projects/${projectName}/docs/"

작업:
1. 입력 경로 아래의 소스 파일을 읽으세요.
2. 문서를 생성하세요.
3. 출력 경로 아래에 결과를 작성하세요.
4. 간결한 요약(생성/업데이트된 파일, 주요 결정 사항, 문제점)을 반환하세요.
```

서브 에이전트는 프롬프트에 포함된 필요한 모든 컨텍스트를 받습니다. 변수는 프롬프트를 보내기 전에 해결되므로, 서브 에이전트는 변수 자리 표시자가 아닌 구체적인 경로와 값으로 작업합니다.

### 실제 예시: 코드 검토 오케스트레이터

여러 전문 에이전트를 통해 코드를 검증하는 간단한 오케스트레이터의 예시입니다:

1) 공유 컨텍스트 결정:
- `repositoryName`, `prNumber`
- `basePath` (예: `projects/${repositoryName}/pr-${prNumber}`)

2) 전문 에이전트 순차 호출 (각 에이전트는 자체 `.agent.md` 사양을 읽음):

```text
Step 1: 보안 검토
Agent: security-reviewer
Spec: .github/agents/security-reviewer.agent.md
Context: repositoryName=${repositoryName}, prNumber=${prNumber}, basePath=projects/${repositoryName}/pr-${prNumber}
Output: projects/${repositoryName}/pr-${prNumber}/security-review.md

Step 2: 테스트 커버리지
Agent: test-coverage
Spec: .github/agents/test-coverage.agent.md
Context: repositoryName=${repositoryName}, prNumber=${prNumber}, basePath=projects/${repositoryName}/pr-${prNumber}
Output: projects/${repositoryName}/pr-${prNumber}/coverage-report.md

Step 3: 집계
Agent: review-aggregator
Spec: .github/agents/review-aggregator.agent.md
Context: repositoryName=${repositoryName}, prNumber=${prNumber}, basePath=projects/${repositoryName}/pr-${prNumber}
Output: projects/${repositoryName}/pr-${prNumber}/final-review.md
```

#### 예시: 조건부 단계 오케스트레이션 (코드 검토)

이 예시는 **사전 확인**, **조건부 단계**, **필수 vs 선택** 동작을 포함한 보다 완전한 오케스트레이션을 보여줍니다.

**동적 매개변수 (입력):**
- `repositoryName`, `prNumber`
- `basePath` (예: `projects/${repositoryName}/pr-${prNumber}`)
- `logFile` (예: `${basePath}/.review-log.md`)

**사전 확인 (권장):**
- 예상 폴더/파일 존재 확인 (예: `${basePath}/changes/`, `${basePath}/reports/`).
- 단계 트리거에 영향을 미치는 상위 수준 특성 감지 (예: 리포지토리 언어, `package.json`, `pom.xml`, `requirements.txt`, 테스트 폴더 존재 여부).
- 시작 시 한 번 결과를 기록합니다.

**단계 트리거 조건:**

| 단계 | 상태 | 트리거 조건 | 실패 시 |
|------|------|-------------|---------|
| 1: 보안 검토 | **필수** | 항상 실행 | 파이프라인 중지 |
| 2: 의존성 감사 | 선택 | 의존성 매니페스트(`package.json`, `pom.xml` 등)가 존재하는 경우 | 계속 |
| 3: 테스트 커버리지 확인 | 선택 | 테스트 프로젝트/파일이 존재하는 경우 | 계속 |
| 4: 성능 확인 | 선택 | 성능에 민감한 코드가 변경되었거나 성능 구성이 존재하는 경우 | 계속 |
| 5: 집계 및 평결 | **필수** | 1단계가 완료되면 항상 실행 | 파이프라인 중지 |

**실행 흐름 (자연어):**
1. `basePath` 초기화 및 `logFile` 생성/업데이트.
2. 사전 확인 실행 및 기록.
3. 1단계 → N단계 순차 실행.
4. 각 단계에 대해:
  - 트리거 조건이 거짓이면: **SKIPPED**로 표시하고 계속.
  - 그렇지 않으면: 래퍼 프롬프트를 사용하여 서브 에이전트 호출 및 요약 캡처.
  - **SUCCESS** 또는 **FAILED**로 표시.
  - 단계가 **필수**이고 실패한 경우: 파이프라인을 중지하고 실패 요약 작성.
5. 최종 요약 섹션(전체 상태, 아티팩트, 다음 조치)으로 종료.

**서브 에이전트 호출 프롬프트 (예시):**

```text
이 단계는 ".github/agents/security-reviewer.agent.md"에 정의된 에이전트 "security-reviewer"로 수행해야 합니다.

중요:
- 전체 .agent.md 사양을 읽고 적용하세요.
- 리포지토리 "${repositoryName}" PR "${prNumber}"에 대해 작업하세요.
- 기본 경로: "${basePath}".

작업:
1. "${basePath}/changes/" 아래의 변경 사항을 검토하세요.
2. "${basePath}/reports/security-review.md"에 결과를 작성하세요.
3. 중요 발견 사항, 권장 수정 사항, 생성/수정된 파일이 포함된 짧은 요약을 반환하세요.
```

**로깅 형식 (예시):**

```markdown
## Step 2: Dependency Audit
**Status:** ✅ SUCCESS / ⚠️ SKIPPED / ❌ FAILED
**Trigger:** package.json present
**Started:** 2026-01-16T10:30:15Z
**Completed:** 2026-01-16T10:31:05Z
**Duration:** 00:00:50
**Artifacts:** reports/dependency-audit.md
**Summary:** [간략한 에이전트 요약]
```

이 패턴은 모든 오케스트레이션 시나리오에 적용됩니다: 변수 추출, 명확한 컨텍스트로 서브 에이전트 호출, 결과 대기.


### 변수 모범 사례

#### 1. **명확한 문서화**
항상 예상되는 변수를 문서화하세요:

```markdown
## Required Variables
- **projectName**: 프로젝트 이름 (문자열, 필수)
- **basePath**: 프로젝트 파일의 루트 디렉토리 (경로, 필수)

## Optional Variables
- **mode**: 처리 모드 - quick/standard/detailed (열거형, 기본값: standard)
- **outputFormat**: 출력 형식 - markdown/json/html (열거형, 기본값: markdown)

## Derived Variables
- **outputDir**: 자동으로 ${basePath}/output으로 설정됨
- **logFile**: 자동으로 ${basePath}/.log.md로 설정됨
```

#### 2. **일관된 명명**
일관된 변수 명명 규칙을 사용하세요:

```javascript
// 좋음: 명확하고 설명적인 명명
const variables = {
  projectName,          // 작업할 프로젝트
  basePath,            // 프로젝트 파일 위치
  outputDirectory,     // 결과 저장 위치
  processingMode,      // 처리 방법 (상세 수준)
  configurationPath    // 구성 파일 위치
};

// 피할 것: 모호하거나 일관성 없음
const bad_variables = {
  name,     // 너무 일반적임
  path,     // 어떤 경로인지 불분명함
  mode,     // 너무 짧음
  config    // 너무 모호함
};
```

#### 3. **유효성 검사 및 제약 조건**
유효한 값과 제약 조건을 문서화하세요:

```markdown
## Variable Constraints

**projectName**:
- Type: string (영숫자, 하이픈, 밑줄 허용)
- Length: 1-100자
- Required: 예
- Pattern: `/^[a-zA-Z0-9_-]+$/`

**processingMode**:
- Type: enum
- Valid values: "quick" (< 5분), "standard" (5-15분), "detailed" (15분 이상)
- Default: "standard"
- Required: 아니요
```

## MCP 서버 구성 (조직/엔터프라이즈 전용)

MCP 서버는 추가 도구로 에이전트 기능을 확장합니다. 조직 및 엔터프라이즈 수준 에이전트에서만 지원됩니다.

### 구성 형식

```yaml
---
name: my-custom-agent
description: 'MCP 통합이 포함된 에이전트'
tools: ['read', 'edit', 'custom-mcp/tool-1']
mcp-servers:
  custom-mcp:
    type: 'local'
    command: 'some-command'
    args: ['--arg1', '--arg2']
    tools: ["*"]
    env:
      ENV_VAR_NAME: ${{ secrets.API_KEY }}
---
```

### MCP 서버 속성

- **type**: 서버 유형 (`'local'` 또는 `'stdio'`)
- **command**: MCP 서버를 시작하는 명령
- **args**: 명령 인수 배열
- **tools**: 이 서버에서 활성화할 도구 (모두 활성화하려면 `["*"]`)
- **env**: 환경 변수 (secrets 지원)

### 환경 변수 및 시크릿

시크릿은 "copilot" 환경 아래의 리포지토리 설정에서 구성해야 합니다.

**지원되는 구문**:
```yaml
env:
  # 환경 변수 전용
  VAR_NAME: COPILOT_MCP_ENV_VAR_VALUE

  # 헤더가 있는 변수
  VAR_NAME: $COPILOT_MCP_ENV_VAR_VALUE
  VAR_NAME: ${COPILOT_MCP_ENV_VAR_VALUE}

  # GitHub Actions 스타일 (YAML 전용)
  VAR_NAME: ${{ secrets.COPILOT_MCP_ENV_VAR_VALUE }}
  VAR_NAME: ${{ var.COPILOT_MCP_ENV_VAR_VALUE }}
```

## 파일 구성 및 명명

### 리포지토리 수준 에이전트
- 위치: `.github/agents/`
- 범위: 특정 리포지토리에서만 사용 가능
- 액세스: 리포지토리에 구성된 MCP 서버 사용

### 조직/엔터프라이즈 수준 에이전트
- 위치: `.github-private/agents/` (이후 `agents/` 루트로 이동)
- 범위: 조직/엔터프라이즈 내 모든 리포지토리에서 사용 가능
- 액세스: 전용 MCP 서버 구성 가능

### 명명 규칙
- 하이픈이 포함된 소문자 사용: `test-specialist.agent.md`
- 이름은 에이전트 목적을 반영해야 함
- 파일명은 기본 에이전트 이름이 됨 (`name`이 지정되지 않은 경우)
- 허용되는 문자: `.`, `-`, `_`, `a-z`, `A-Z`, `0-9`

## 에이전트 처리 및 동작

### 버전 관리
- 에이전트 파일의 Git 커밋 SHA 기반
- 다른 에이전트 버전에 대한 브랜치/태그 생성
- 리포지토리/브랜치에 대한 최신 버전을 사용하여 인스턴스화
- PR 상호 작용은 일관성을 위해 동일한 에이전트 버전 사용

### 이름 충돌
우선순위 (높음에서 낮음):
1. 리포지토리 수준 에이전트
2. 조직 수준 에이전트
3. 엔터프라이즈 수준 에이전트

하위 수준 구성은 동일한 이름을 가진 상위 수준 구성을 재정의합니다.

### 도구 처리
- `tools` 목록은 사용 가능한 도구(기본 제공 및 MCP)를 필터링
- 도구가 지정되지 않음 = 모든 도구 활성화
- 빈 목록 (`[]`) = 모든 도구 비활성화
- 특정 목록 = 해당 도구만 활성화
- 인식되지 않는 도구 이름은 무시됨 (환경별 도구 허용)

### MCP 서버 처리 순서
1. 기본 제공 MCP 서버 (예: GitHub MCP)
2. 사용자 지정 에이전트 MCP 구성 (조직/엔터프라이즈 전용)
3. 리포지토리 수준 MCP 구성

각 수준은 이전 수준의 설정을 재정의할 수 있습니다.

## 에이전트 생성 체크리스트

### Frontmatter
- [ ] `description` 필드가 존재하며 설명적임 (50-150자)
- [ ] `description`이 작은따옴표로 감싸져 있음
- [ ] `name` 지정됨 (선택 사항이지만 권장됨)
- [ ] `tools`가 적절하게 구성됨 (또는 의도적으로 생략됨)
- [ ] `model`이 최적의 성능을 위해 지정됨
- [ ] 환경별인 경우 `target` 설정됨
- [ ] 수동 선택이 필요한 경우 `infer`가 `false`로 설정됨

### 프롬프트 내용
- [ ] 명확한 에이전트 정체성 및 역할 정의됨
- [ ] 핵심 책임이 명시적으로 나열됨
- [ ] 접근 방식 및 방법론 설명됨
- [ ] 지침 및 제약 조건 지정됨
- [ ] 출력 기대치 문서화됨
- [ ] 도움이 되는 경우 예시 제공됨
- [ ] 지침이 구체적이고 실행 가능함
- [ ] 범위 및 경계가 명확하게 정의됨
- [ ] 총 콘텐츠 30,000자 미만

### 파일 구조
- [ ] 파일명이 하이픈 포함 소문자 규칙을 따름
- [ ] 파일이 올바른 디렉토리(`.github/agents/` 또는 `agents/`)에 위치함
- [ ] 파일명이 허용된 문자만 사용함
- [ ] 파일 확장자가 `.agent.md`임

### 품질 보증
- [ ] 에이전트 목적이 고유하며 중복되지 않음
- [ ] 도구가 최소한으로 필요함
- [ ] 지침이 명확하고 모호하지 않음
- [ ] 대표적인 작업으로 에이전트가 테스트됨
- [ ] 문서 참조가 최신임
- [ ] 보안 고려 사항이 해결됨 (해당되는 경우)

## 일반적인 에이전트 패턴

### 테스팅 전문가 (Testing Specialist)
**목적**: 테스트 커버리지 및 품질에 집중
**도구**: 모든 도구 (포괄적인 테스트 생성용)
**접근 방식**: 분석, 격차 식별, 테스트 작성, 프로덕션 코드 변경 방지

### 구현 설계자 (Implementation Planner)
**목적**: 상세한 기술 계획 및 사양 작성
**도구**: `['read', 'search', 'edit']`로 제한
**접근 방식**: 요구 사항 분석, 문서 작성, 구현 방지

### 코드 검토자 (Code Reviewer)
**목적**: 코드 품질 검토 및 피드백 제공
**도구**: `['read', 'search']` 전용
**접근 방식**: 분석, 개선 사항 제안, 직접 수정 없음

### 리팩토링 전문가 (Refactoring Specialist)
**목적**: 코드 구조 및 유지 관리 가능성 개선
**도구**: `['read', 'search', 'edit']`
**접근 방식**: 패턴 분석, 리팩토링 제안, 안전하게 구현

### 보안 감사자 (Security Auditor)
**목적**: 보안 문제 및 취약점 식별
**도구**: `['read', 'search', 'web']`
**접근 방식**: 코드 스캔, OWASP 대조 확인, 결과 보고

## 피해야 할 흔한 실수

### Frontmatter 오류
- ❌ `description` 필드 누락
- ❌ 설명이 따옴표로 감싸지지 않음
- ❌ 문서 확인 없이 유효하지 않은 도구 이름 사용
- ❌ 잘못된 YAML 구문 (들여쓰기, 따옴표)

### 도구 구성 문제
- ❌ 불필요하게 과도한 도구 액세스 권한 부여
- ❌ 에이전트 목적에 필요한 필수 도구 누락
- ❌ 도구 별칭을 일관되게 사용하지 않음
- ❌ MCP 서버 네임스페이스(`server-name/tool`) 누락

### 프롬프트 내용 문제
- ❌ 모호하고 불분명한 지침
- ❌ 상충되거나 모순되는 가이드라인
- ❌ 명확한 범위 정의 부족
- ❌ 출력 기대치 누락
- ❌ 지나치게 장황한 지침 (문자 제한 초과)
- ❌ 복잡한 작업에 대한 예시 또는 컨텍스트 없음

### 조직적 문제
- ❌ 파일명이 에이전트 목적을 반영하지 않음
- ❌ 잘못된 디렉토리 (리포지토리 vs 조직 수준 혼동)
- ❌ 파일명에 공백이나 특수 문자 사용
- ❌ 중복된 에이전트 이름으로 인한 충돌

## 테스트 및 검증

### 수동 테스트
1. 올바른 frontmatter로 에이전트 파일 생성
2. VS Code 다시 로드 또는 GitHub.com 새로 고침
3. Copilot Chat의 드롭다운에서 에이전트 선택
4. 대표적인 사용자 쿼리로 테스트
5. 도구 액세스가 예상대로 작동하는지 확인
6. 출력이 기대치를 충족하는지 확인

### 통합 테스트
- 범위 내의 다양한 파일 유형으로 에이전트 테스트
- MCP 서버 연결 확인 (구성된 경우)
- 누락된 컨텍스트에 대한 에이전트 동작 확인
- 오류 처리 및 엣지 케이스 테스트
- 에이전트 전환 및 핸드오프 검증

### 품질 확인
- 에이전트 생성 체크리스트 실행
- 일반적인 실수 목록과 대조 검토
- 리포지토리의 예시 에이전트와 비교
- 복잡한 에이전트에 대한 동료 검토
- 특별한 구성 요구 사항 문서화

## 추가 리소스

### 공식 문서
- [사용자 지정 에이전트 생성](https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/create-custom-agents)
- [사용자 지정 에이전트 구성](https://docs.github.com/en/copilot/reference/custom-agents-configuration)
- [VS Code의 사용자 지정 에이전트](https://code.visualstudio.com/docs/copilot/customization/custom-agents)
- [MCP 통합](https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/extend-coding-agent-with-mcp)

### 커뮤니티 리소스
- [Awesome Copilot Agents 컬렉션](https://github.com/github/awesome-copilot/tree/main/agents)
- [사용자 지정 라이브러리 예시](https://docs.github.com/en/copilot/tutorials/customization-library/custom-agents)
- [첫 번째 사용자 지정 에이전트 튜토리얼](https://docs.github.com/en/copilot/tutorials/customization-library/custom-agents/your-first-custom-agent)

### 관련 파일
- [프롬프트 파일 지침](./prompt.instructions.md) - 프롬프트 파일 생성용
- [지침 파일 가이드라인](./instructions.instructions.md) - 지침 파일 생성용

## 버전 호환성 참고 사항

### GitHub.com (Coding Agent)
- ✅ 모든 표준 frontmatter 속성 완벽 지원
- ✅ 리포지토리 및 조직/엔터프라이즈 수준 에이전트
- ✅ MCP 서버 구성 (조직/엔터프라이즈)
- ❌ `model`, `argument-hint`, `handoffs` 속성 미지원

### VS Code / JetBrains / Eclipse / Xcode
- ✅ AI 모델 선택을 위한 `model` 속성 지원
- ✅ `argument-hint` 및 `handoffs` 속성 지원
- ✅ 사용자 프로필 및 워크스페이스 수준 에이전트
- ❌ 리포지토리 수준에서 MCP 서버 구성 불가능 (사용자/워크스페이스 설정 필요)
- ⚠️ 일부 속성은 다르게 동작할 수 있음

여러 환경을 위한 에이전트를 생성할 때는 공통 속성에 집중하고 모든 타겟 환경에서 테스트하세요. 필요시 `target` 속성을 사용하여 환경별 에이전트를 생성하세요.