# Tasks: Calculator Web Application

**Input**: Design documents from `/specs/1-calculator-app/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: The examples below include test tasks. Tests are OPTIONAL - only include them if explicitly requested in the feature specification.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- **Web app**: `backend/src/`, `frontend/src/`
- **Mobile**: `api/src/`, `ios/src/` or `android/src/`
- Paths shown below assume single project - adjust based on plan.md structure

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [x] T001 Create root project directory `calculator_app/`
- [x] T002 Create `calculator_app/requirements.txt` and add `streamlit`
- [x] T003 Create empty Streamlit application entry point `calculator_app/main.py`
- [x] T004 Create empty core calculation logic file `calculator_app/calculator.py`
- [x] T005 Create `tests/unit/` directory
- [x] T006 Create empty unit test file `tests/unit/test_calculator.py`

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [x] T007 Define `ALLOWED_OPERATORS` in `calculator_app/calculator.py` (e.g., `'+', '-', '*', '/'`)
- [x] T008 Define `ALLOWED_CHARACTERS` in `calculator_app/calculator.py` (digits, operators, decimal point, whitespace)

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Basic Arithmetic Calculation (Priority: P1) 🎯 MVP

**Goal**: Implement the core calculation logic, UI for input/output, and handle valid expressions.

**Independent Test**: Enter various valid arithmetic expressions and verify that the correct result is displayed.

### Tests for User Story 1 ⚠️

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [x] T009 [P] [US1] Unit test for `validate_expression` with valid inputs in `tests/unit/test_calculator.py`
- [x] T010 [P] [US1] Unit test for `calculate_expression` with basic valid operations in `tests/unit/test_calculator.py`

### Implementation for User Story 1

- [x] T011 [US1] Implement `validate_expression` function to check `ALLOWED_CHARACTERS` in `calculator_app/calculator.py`
- [x] T012 [US1] Implement `calculate_expression` function using a safe evaluation method (e.g., `ast.literal_eval` or custom parsing) for valid arithmetic expressions in `calculator_app/calculator.py`
- [x] T013 [US1] Implement the basic Streamlit app structure (title, text input for expression, 'Calculate' button) in `calculator_app/main.py`
- [x] T014 [US1] Connect UI elements to calculation logic for valid inputs in `calculator_app/main.py`
- [x] T015 [US1] Display the calculated result using `st.success` or `st.metric` in `calculator_app/main.py`

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - Error Handling for Invalid Expressions (Priority: P1)

**Goal**: Display clear error messages for invalid inputs and edge cases.

**Independent Test**: Enter various invalid expressions (e.g., "10 / 0", "5 + *", "abc") and verify that appropriate error messages are displayed without application crash.

### Implementation for User Story 2

- [x] T016 [US2] Extend `validate_expression` to check for syntactical validity of the expression in `calculator_app/calculator.py`
- [x] T017 [US2] Implement error display for `validate_expression` failures using `st.error` in `calculator_app/main.py`
- [x] T018 [US2] Implement specific error handling for division by zero within `calculate_expression` in `calculator_app/calculator.py`
- [x] T019 [US2] Integrate error display for division by zero using `st.error` in `calculator_app/main.py`
- [x] T020 [US2] Implement error handling for unsupported operations/characters (if not covered by `validate_expression`) in `calculator_app/calculator.py`
- [x] T021 [US2] Integrate error display for unsupported operations/characters using `st.error` in `calculator_app/main.py`
- [x] T022 [US2] Handle empty input field, displaying an appropriate error message using `st.error` in `calculator_app/main.py`

**Checkpoint**: All user stories should now be independently functional

---

## Phase 5: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [x] T023 Add comprehensive comments and docstrings to functions in `calculator_app/calculator.py` and `calculator_app/main.py`
- [x] T024 Refactor code for improved readability and adherence to PEP 8 standards in `calculator_app/`
- [x] T025 Validate quickstart guide by following steps in `specs/1-calculator-app/quickstart.md`
- [x] T026 Update `README.md` with instructions on how to run the application

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P1)**: Can start after Foundational (Phase 2) - Depends on US1's calculation and validation framework to integrate error handling.

### Within Each User Story

- Tests (if included) MUST be written and FAIL before implementation
- Core logic implementation before UI integration.
- Story complete before moving to next priority.

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel.
- Tests within a user story can run in parallel.

---

## Parallel Example: User Story 1

```bash
# Launch all tests for User Story 1 together:
# (Note: In a real scenario, these would be run by a test runner)
python -m pytest tests/unit/test_calculator.py::test_validate_expression_valid
python -m pytest tests/unit/test_calculator.py::test_calculate_expression_basic
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test User Story 1 independently
5. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (MVP!)
3. Add User Story 2 → Test independently → Deploy/Demo
4. Add Polish → Deploy/Demo
5. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1 (Core Calculation)
   - Developer B: User Story 2 (Error Handling)
3. Stories complete and integrate independently

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Verify tests fail before implementing
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence
