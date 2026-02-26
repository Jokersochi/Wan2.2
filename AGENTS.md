# AGENTS.md

## Cursor Cloud specific instructions

### Project overview

Wan2.2 is an open-source AI video generation model suite (Python/PyTorch). It is a CLI-based inference tool (`generate.py`), not a web application or long-running service. See `README.md` for usage and `INSTALL.md` for installation options.

### CUDA / GPU requirement

All inference and module-level imports (`import wan`) require an NVIDIA GPU with CUDA. The `wan` package calls `torch.cuda.current_device()` at class-definition time in `wan/modules/t5.py`, so even `import wan` fails without CUDA-enabled PyTorch. On CPU-only environments, you can still run all lint/format tools and pytest (there are no pytest test files in the repo; tests are shell-based in `tests/test.sh` and require GPU + model checkpoints).

`flash_attn` also requires CUDA to install and is listed as a dependency. Skip it on CPU-only environments.

### Lint and format commands

- `black --check .` — format check
- `isort --check-only .` — import sort check
- `flake8 --max-line-length 120 wan/ generate.py` — lint
- `mypy --ignore-missing-imports wan/` — type check (many pre-existing strict-mode errors)
- `make format` — auto-format with isort + yapf (modifies files in-place)

### Testing

- `python -m pytest` — runs pytest (no pytest test files exist currently)
- `bash tests/test.sh <model_dir> <gpu_count>` — integration tests requiring GPU + downloaded model checkpoints

### Running inference

Requires downloaded model weights (multi-GB from HuggingFace/ModelScope) and NVIDIA GPU. See `README.md` for full commands. Example:

```bash
python generate.py --task t2v-A14B --size 1280*720 --ckpt_dir ./Wan2.2-T2V-A14B --offload_model True --convert_model_dtype --prompt "your prompt"
```
