import sys
from unittest.mock import MagicMock
import types

sys.modules['torch'] = types.ModuleType('torch')
sys.modules['torch.distributed'] = types.ModuleType('torch.distributed')
sys.modules['torch.nn'] = types.ModuleType('torch.nn')
sys.modules['torchvision'] = types.ModuleType('torchvision')
sys.modules['wan'] = types.ModuleType('wan')
sys.modules['PIL'] = types.ModuleType('PIL')
sys.modules['PIL.Image'] = types.ModuleType('PIL.Image')
sys.modules['wan.utils.prompt_expand'] = types.ModuleType('wan.utils.prompt_expand')
sys.modules['wan.utils.prompt_expand'].DashScopePromptExpander = MagicMock()
sys.modules['wan.utils.prompt_expand'].QwenPromptExpander = MagicMock()

import generate
import argparse

def test():
    parser = argparse.ArgumentParser()
    parser.add_argument("--task", type=str, default="t2v-A14B")
    parser.add_argument("--ckpt_dir", type=str, default=None)
    parser.add_argument("--image", type=str, default=None)
    parser.add_argument("--audio", type=str, default=None)
    parser.add_argument("--enable_tts", type=bool, default=False)
    parser.add_argument("--tts_prompt_audio", type=str, default=None)
    parser.add_argument("--tts_text", type=str, default=None)
    parser.add_argument("--sample_steps", type=int, default=None)
    parser.add_argument("--sample_shift", type=float, default=None)
    parser.add_argument("--sample_guide_scale", type=float, default=None)
    parser.add_argument("--frame_num", type=int, default=None)
    parser.add_argument("--base_seed", type=int, default=-1)
    parser.add_argument("--size", type=str, default="1280*720")
    parser.add_argument("--prompt", type=str, default=None)

    args = parser.parse_args([])
    try:
        generate._validate_args(args)
    except Exception as e:
        print("Caught Exception:", type(e), e)

if __name__ == "__main__":
    test()
