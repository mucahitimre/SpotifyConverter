import sys
import types
import os

# Ensure project root is on the path so Youtube module can be imported
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

# Stub out ytmusicapi module to avoid ImportError during import of Youtube
sys.modules.setdefault('ytmusicapi', types.ModuleType('ytmusicapi')).YTMusic = object

from Youtube import divide_list_into_chunks


def test_divide_list_into_chunks_basic():
    result = list(divide_list_into_chunks([1, 2, 3, 4, 5], 2))
    assert result == [[1, 2], [3, 4], [5]]
