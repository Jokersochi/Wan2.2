1. **Optimize `wan/modules/model.py`:** Use `replace_with_git_merge_diff` to replace `.chunk(N, dim=2)` + `.squeeze(2)` with `.unbind(dim=2)` in two places.
   ```
   <<<<<<< SEARCH
           assert e.dtype == torch.float32
           with torch.amp.autocast('cuda', dtype=torch.float32):
               e = (self.modulation.unsqueeze(0) + e).chunk(6, dim=2)
           assert e[0].dtype == torch.float32

           # self-attention
           y = self.self_attn(
               self.norm1(x).float() * (1 + e[1].squeeze(2)) + e[0].squeeze(2),
               seq_lens, grid_sizes, freqs)
           with torch.amp.autocast('cuda', dtype=torch.float32):
               x = x + y * e[2].squeeze(2)

           # cross-attention & ffn function
           def cross_attn_ffn(x, context, context_lens, e):
               x = x + self.cross_attn(self.norm3(x), context, context_lens)
               y = self.ffn(
                   self.norm2(x).float() * (1 + e[4].squeeze(2)) + e[3].squeeze(2))
               with torch.amp.autocast('cuda', dtype=torch.float32):
                   x = x + y * e[5].squeeze(2)
               return x
   =======
           assert e.dtype == torch.float32
           with torch.amp.autocast('cuda', dtype=torch.float32):
               e = (self.modulation.unsqueeze(0) + e).unbind(dim=2)
           assert e[0].dtype == torch.float32

           # self-attention
           y = self.self_attn(
               self.norm1(x).float() * (1 + e[1]) + e[0],
               seq_lens, grid_sizes, freqs)
           with torch.amp.autocast('cuda', dtype=torch.float32):
               x = x + y * e[2]

           # cross-attention & ffn function
           def cross_attn_ffn(x, context, context_lens, e):
               x = x + self.cross_attn(self.norm3(x), context, context_lens)
               y = self.ffn(
                   self.norm2(x).float() * (1 + e[4]) + e[3])
               with torch.amp.autocast('cuda', dtype=torch.float32):
                   x = x + y * e[5]
               return x
   >>>>>>> REPLACE
   ```
   and
   ```
   <<<<<<< SEARCH
           assert e.dtype == torch.float32
           with torch.amp.autocast('cuda', dtype=torch.float32):
               e = (self.modulation.unsqueeze(0) + e.unsqueeze(2)).chunk(2, dim=2)
               x = (
                   self.head(
                       self.norm(x) * (1 + e[1].squeeze(2)) + e[0].squeeze(2)))
           return x
   =======
           assert e.dtype == torch.float32
           with torch.amp.autocast('cuda', dtype=torch.float32):
               e = (self.modulation.unsqueeze(0) + e.unsqueeze(2)).unbind(dim=2)
               x = (
                   self.head(
                       self.norm(x) * (1 + e[1]) + e[0]))
           return x
   >>>>>>> REPLACE
   ```

2. **Verify `wan/modules/model.py`:** Run `grep -nC 2 "\.unbind(" wan/modules/model.py` to ensure modifications were applied.

3. **Optimize `wan/modules/s2v/model_s2v.py`:** Use `replace_with_git_merge_diff` to replace `.chunk(6, dim=1)` + `.squeeze(1)` with `.unbind(dim=1)`.
   ```
   <<<<<<< SEARCH
           modulation = self.modulation.unsqueeze(2)
           with amp.autocast(dtype=torch.float32):
               e = (modulation + e).chunk(6, dim=1)
           assert e[0].dtype == torch.float32

           e = [element.squeeze(1) for element in e]
           norm_x = self.norm1(x).float()
   =======
           modulation = self.modulation.unsqueeze(2)
           with amp.autocast(dtype=torch.float32):
               e = (modulation + e).unbind(dim=1)
           assert e[0].dtype == torch.float32

           norm_x = self.norm1(x).float()
   >>>>>>> REPLACE
   ```

4. **Verify `wan/modules/s2v/model_s2v.py`:** Run `grep -nC 2 "\.unbind(" wan/modules/s2v/model_s2v.py` to ensure modifications were applied.

5. Delete temporary files created during exploration by running `rm test_perf.py test_unbind.py plan.md`.

6. Run `python3 -m compileall .` to validate syntax.

7. Complete pre-commit steps to ensure proper testing, verification, review, and reflection are done.

8. Submit PR using `submit`:
   - Title: "⚡ Bolt: Replace PyTorch chunk+squeeze with unbind"
   - Description:
     💡 What: Replaced occurrences of `.chunk(N, dim=D)` followed by `.squeeze(D)` with `.unbind(dim=D)` in `wan/modules/model.py` and `wan/modules/s2v/model_s2v.py`.
     🎯 Why: PyTorch's `.chunk(N, dim=D)` followed by `.squeeze(D)` is a common anti-pattern that creates intermediate tensors and requires multiple Python function calls. Using `.unbind(dim=D)` achieves the same result (a tuple of tensors with the specified dimension removed) directly in C++, reducing memory allocations and Python overhead in hot loops like attention blocks.
     📊 Impact: Reduces intermediate tensor creation and Python function call overhead in highly-frequent model layers (like Attention Blocks), leading to minor measurable memory reductions and faster loop execution times.
     🔬 Measurement: Verified that there are no syntax errors via `compileall` and confirmed changes applied correctly via `grep`. Can be profiled via PyTorch Profiler or standard PyTorch forward-pass benchmarks to observe lower memory footprint.
