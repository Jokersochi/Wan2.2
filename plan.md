1. Modify `wan/modules/t5.py` to replace the `torch.einsum` operations with `F.scaled_dot_product_attention` (SDPA). This is standard in PyTorch 2 and provides a significant speed up and memory footprint reduction.
2. Update `.jules/bolt.md` to include a learning about SDPA and its benefits replacing `einsum`.
3. Verify tests and linting are passing using `python3 -m compileall .` (we don't have a test suite readily runnable).
4. Run pre-commit instructions.
5. Create a PR to share this performance improvement.
