import os
import sys
from unittest.mock import MagicMock
import tempfile
from PIL import Image

sys.modules['torch'] = MagicMock()
sys.modules['torch.nn'] = MagicMock()
sys.modules['torch.nn.functional'] = MagicMock()
sys.modules['torchvision'] = MagicMock()
sys.modules['dashscope'] = MagicMock()
sys.modules['transformers'] = MagicMock()
class MockEasyDict(dict):
    def __getattr__(self, name): return self.get(name)
    def __setattr__(self, name, value): self[name] = value
mock_easydict = MagicMock()
mock_easydict.EasyDict = MockEasyDict
sys.modules['easydict'] = mock_easydict
sys.modules['huggingface_hub'] = MagicMock()
class MockMixin1: pass
class MockMixin2: pass
mock_diffusers = MagicMock()
mock_diffusers.configuration_utils = MagicMock()
mock_diffusers.configuration_utils.ConfigMixin = MockMixin1
mock_diffusers.models = MagicMock()
mock_diffusers.models.modeling_utils = MagicMock()
mock_diffusers.models.modeling_utils.ModelMixin = MockMixin2
sys.modules['diffusers'] = mock_diffusers
sys.modules['diffusers.configuration_utils'] = mock_diffusers.configuration_utils
sys.modules['diffusers.models'] = mock_diffusers.models
sys.modules['diffusers.models.modeling_utils'] = mock_diffusers.models.modeling_utils
sys.modules['peft'] = MagicMock()
sys.modules['xformers'] = MagicMock()
sys.modules['einops'] = MagicMock()

from wan.utils.prompt_extend import DashScopePromptExpander

class ExplodingImage(Image.Image):
    def save(self, *args, **kwargs):
        raise ValueError("Boom!")

expander = DashScopePromptExpander(model_name="test", task="i2v", is_vl=True)
expander.max_image_size = 100
expander.retry_times = 1
image = Image.new('RGB', (10, 10))
image.resize = MagicMock(return_value=ExplodingImage())

try:
    expander.extend_with_img("prompt", "system", image=image)
except ValueError:
    pass

# Check if there are any dangling .png files in tempdir
tempdir = tempfile.gettempdir()
png_files = [f for f in os.listdir(tempdir) if f.endswith('.png')]
for f in png_files:
    os.remove(os.path.join(tempdir, f))
if png_files:
    print(f"Failed: Temporary files leaked: {png_files}")
    sys.exit(1)
print("Success: Temporary files cleaned up!")
