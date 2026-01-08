# Basic Usage Examples

## Simple GET request
```bash
http-analyze https://httpbin.org/get

Expected output shows:

Request sent
Response received
Timing information
Basic analysis


### **Task 4: CLI Skeleton Implementation (45 minutes)**

**Step 1: Choose CLI Framework**
Research and decide:
- **click** - Popular, decorator-based, easier for complex CLIs
- **typer** - Modern, type-hint based, from FastAPI creator

**Step 2: Implement Basic CLI Structure**
In `src/http_analyzer/cli.py`, implement:
1. **Version command** (`--version`) that reads from package
2. **Help command** (`--help`) showing your planned command structure
3. **Placeholder commands** for the main functionality

**Step 3: Create Entry Point**
Configure your package so `http-analyze` command works:
- Set up `pyproject.toml` entry points
- Create `__main__.py` if needed
- Test that `python -m http_analyzer --help` works

### **Task 5: Initial Test Setup (30 minutes)**

**Step 1: Configure Testing**
1. Create `pytest.ini` or `setup.cfg` for test configuration
2. Write first test in `tests/test_cli.py` - test `--version` flag
3. Write test in `tests/test_structure.py` - verify imports work

**Step 2: Create Mock Test Server**
Create `tests/fixtures/test_server.py` with a simple HTTP server for testing.

**Step 3: Set up CI/CD Foundation**
Create `.github/workflows/test.yml` with basic test workflow (optional but good practice).

## **🧠 DECISIONS YOU NEED TO MAKE**

Before writing code, decide:

### **1. Python Version Support**
- Will you support Python 3.8+? 3.9+? 3.10+?
- Document this in `pyproject.toml` and README

### **2. Dependency Strategy**
- **httpx** vs **requests** + **aiohttp**?
- **rich** for terminal formatting?
- **pydantic** for data validation?

### **3. CLI Framework Choice**
Consider:
- **Learning curve** - Which will you learn from most?
- **Future needs** - Will you need subcommands, autocompletion?
- **Community support** - Which has better documentation?

### **4. Testing Approach**
- **Unit test granularity** - Test each function or broader units?
- **Mocking strategy** - Use unittest.mock or pytest-mock?
- **Test data management** - Where to store test responses?

## **✅ PHASE 0 COMPLETION CHECKLIST**

You have successfully completed Phase 0 when:

### **Infrastructure:**
- [ ] Project directory structure exists
- [ ] Git repository initialized
- [ ] Virtual environment created and activated
- [ ] All configuration files created

### **Code Structure:**
- [ ] All placeholder Python files exist
- [ ] Basic `__init__.py` files set up
- [ ] Imports between modules can work

### **Documentation:**
- [ ] README.md written with project vision
- [ ] docs/design.md with architecture decisions
- [ ] examples/ with planned usage

### **Development Environment:**
- [ ] Dependencies specified in pyproject.toml
- [ ] Development tools configured (formatter, linter)
- [ ] Test framework configured

### **Basic Functionality:**
- [ ] `http-analyze --version` works
- [ ] `http-analyze --help` shows command structure
- [ ] Can run tests with `pytest`

## **🚨 COMMON PITFALLS TO AVOID**

1. **Don't skip virtual environment** - It's crucial for dependency isolation
2. **Don't commit sensitive data** - Double-check .gitignore
3. **Don't over-engineer initially** - Start minimal, expand as needed
4. **Don't ignore error handling** - Plan it from the start
5. **Don't forget about Windows** - If supporting Windows, test path handling

## **📝 PROGRESS TRACKING**

As you complete each task, update this checklist:

**Phase 0 Progress:**
- [ ] Task 1: Project Structure (0/3)
  - [ ] Directories created
  - [ ] Placeholder files created
  - [ ] Git initialized
- [ ] Task 2: Development Environment (0/4)
  - [ ] Virtual environment created
  - [ ] Configuration files created
  - [ ] Dependencies specified
  - [ ] Tools configured
- [ ] Task 3: Documentation (0/3)
  - [ ] README.md complete
  - [ ] Design documentation
  - [ ] Examples documented
- [ ] Task 4: CLI Skeleton (0/3)
  - [ ] Framework chosen
  - [ ] Basic commands implemented
  - [ ] Entry point working
- [ ] Task 5: Test Setup (0/3)
  - [ ] Test framework configured
  - [ ] First tests written
  - [ ] Mock server created

## **🔍 WHAT TO DO WHEN STUCK**

1. **Research decision points** - Read documentation for each option
2. **Look at similar projects** - Check how popular CLI tools are structured
3. **Write down questions** - Document what you're uncertain about
4. **Make a choice and proceed** - You can always refactor later

## **⏭️ NEXT STEPS AFTER PHASE 0**

Once Phase 0 is complete, we'll:
1. Review your architecture decisions
2. Plan Phase 1 implementation details
3. Set up the manual HTTP client
4. Begin with core HTTP protocol implementation

---

**Start with Task 1 now.** Create the directory structure first - this gives you tangible progress immediately. 

When you complete Task 1 or have questions about any specific part, let me know and we'll proceed step by step.

**Remember:** The goal of Phase 0 is not to write application code, but to create a professional foundation that makes writing application code easier and more organized.

Ready? Begin with:
```bash
mkdir http-analyzer
cd http-analyzer
# ... continue with Task 1