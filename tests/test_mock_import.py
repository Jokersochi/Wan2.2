import sys
from unittest.mock import MagicMock

class MockPackage(MagicMock):
    @classmethod
    def __getattr__(cls, name):
        return MagicMock()

# Deeply mock required external dependencies missing in testing environment
sys.modules['flash_attn'] = MockPackage()
sys.modules['transformers'] = MockPackage()
sys.modules['torchvision'] = MockPackage()
sys.modules['torchvision.transforms'] = MockPackage()
sys.modules['torchvision.transforms.functional'] = MockPackage()
sys.modules['safetensors'] = MockPackage()
sys.modules['peft'] = MockPackage()
sys.modules['cv2'] = MockPackage()
sys.modules['librosa'] = MockPackage()
sys.modules['diffusers'] = MockPackage()
sys.modules['diffusers.models'] = MockPackage()
sys.modules['diffusers.models.modeling_utils'] = MockPackage()
sys.modules['diffusers.configuration_utils'] = MockPackage()
sys.modules['diffusers.schedulers'] = MockPackage()
sys.modules['diffusers.schedulers.scheduling_utils'] = MockPackage()
sys.modules['diffusers.utils'] = MockPackage()
sys.modules['diffusers.utils.torch_utils'] = MockPackage()
sys.modules['diffusers.models.attention'] = MockPackage()
sys.modules['diffusers.loaders'] = MockPackage()
sys.modules['easydict'] = MockPackage()
sys.modules['numpy'] = MockPackage()
sys.modules['einops'] = MockPackage()
sys.modules['decord'] = MockPackage()
sys.modules['tqdm'] = MockPackage()
sys.modules['ftfy'] = MockPackage()
sys.modules['regex'] = MockPackage()
sys.modules['scipy'] = MockPackage()
sys.modules['scipy.stats'] = MockPackage()
sys.modules['PIL'] = MockPackage()
sys.modules['imageio'] = MockPackage()

import torch
# Make sure CUDA check passes in mock
torch.cuda.current_device = MagicMock(return_value='cpu')
torch.cuda.is_available = MagicMock(return_value=True)
torch.cuda.amp = MagicMock()

# Diffusers Mixin mock
class ModelMixinMock:
    pass
class ConfigMixinMock:
    pass
class SchedulerMixinMock:
    pass
class FromOriginalModelMixinMock:
    pass
class PeftAdapterMixinMock:
    pass
sys.modules['diffusers.models.modeling_utils'].ModelMixin = ModelMixinMock
sys.modules['diffusers.configuration_utils'].ConfigMixin = ConfigMixinMock
sys.modules['diffusers.schedulers.scheduling_utils'].SchedulerMixin = SchedulerMixinMock
sys.modules['diffusers.loaders'].FromOriginalModelMixin = FromOriginalModelMixinMock
sys.modules['diffusers.loaders'].PeftAdapterMixin = PeftAdapterMixinMock

def register_to_config_mock(func):
    return func
sys.modules['diffusers.configuration_utils'].register_to_config = register_to_config_mock

# Now we can try importing the module to ensure no syntax errors and verify usage of weights_only
try:
    from wan.modules.t5 import T5EncoderModel
    from wan.modules.animate.clip import CLIPModel
    from wan.modules.vae2_1 import _video_vae as video_vae_2_1
    from wan.modules.vae2_2 import _video_vae as video_vae_2_2
    from wan.animate import WanAnimate

    # Just checking we imported fine
    print("Imports successful!")
    print(f"t5 weights_only: {'weights_only' in open('wan/modules/t5.py').read()}")
    print(f"clip weights_only: {'weights_only' in open('wan/modules/animate/clip.py').read()}")
    print(f"vae2_1 weights_only: {'weights_only' in open('wan/modules/vae2_1.py').read()}")
    print(f"vae2_2 weights_only: {'weights_only' in open('wan/modules/vae2_2.py').read()}")
    print(f"animate weights_only: {'weights_only' in open('wan/animate.py').read()}")
except Exception as e:
    import traceback
    traceback.print_exc()
    print(f"Error: {e}")
    sys.exit(1)
