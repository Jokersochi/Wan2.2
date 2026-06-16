## Cursor Cloud specific instructions

### Project overview

Wan2.2 is a Python-based AI video generation inference pipeline (no web server, no database). The entry point is `generate.py` which requires CUDA-capable GPUs and pre-downloaded model checkpoints. See `README.md` for full usage instructions.

### CUDA requirement

The `wan` package cannot be imported without CUDA — `wan/modules/t5.py` calls `torch.cuda.current_device()` at class definition time. On CPU-only environments, monkey-patch before importing: `import torch; torch.cuda.current_device = lambda: 0`. Development tool commands (lint, format, compile checks) work without GPU regardless.

### Development tools

- **Lint/format**: `black --check .`, `isort --check-only .`, `flake8 --max-line-length 120 wan/ generate.py`
- **Format in-place**: `black .` and `isort .` (also available via `make format` which uses `yapf` + `isort`)
- **Type check**: `mypy wan/` (strict mode configured in `pyproject.toml`)
- **Tests**: No pytest unit tests exist. The only test suite is `tests/test.sh <model_dir> <gpu_count>`, which requires GPUs + downloaded model checkpoints.
- **Syntax check**: `python3 -c "import py_compile, glob; [py_compile.compile(f, doraise=True) for f in glob.glob('wan/**/*.py', recursive=True) + ['generate.py']]"`

### Running inference

Requires NVIDIA GPU(s) with sufficient VRAM (24GB+ for 5B model, 80GB+ for 14B models) and pre-downloaded model checkpoints from HuggingFace or ModelScope. See `README.md` for CLI examples.

### Dependencies

Core deps in `requirements.txt`. Optional extras in `requirements_s2v.txt` and `requirements_animate.txt`. Dev tools in `pyproject.toml` under `[project.optional-dependencies] dev`. The `flash_attn` package requires CUDA hardware to build/install. The `pyworld` package (in `requirements_s2v.txt`) needs C++ build tools and may fail; it is only needed for CosyVoice TTS in S2V. Install order: PyTorch first, then remaining deps, then `flash_attn` last.
