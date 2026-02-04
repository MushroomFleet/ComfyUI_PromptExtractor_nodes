"""
ComfyUI Prompt Extractor Nodes
Custom nodes for extracting text prompts from PNG image metadata.

Author: Drift Johnson
Repository: https://github.com/MushroomFleet/ComfyUI_PromptExtractor_nodes
"""

from .DJZ_PromptExtractor import (
    DJZ_PromptExtractor,
    DJZ_PromptExtractorFromPath,
    DJZ_PromptExtractorBatch,
)

from .DJZ_PromptExtractorV2 import (
    DJZ_PromptExtractorV2,
    DJZ_PromptExtractorV2_Batch,
    DJZ_PromptExtractorV2_StringNavigator,
)

NODE_CLASS_MAPPINGS = {
    "DJZ_PromptExtractor": DJZ_PromptExtractor,
    "DJZ_PromptExtractorFromPath": DJZ_PromptExtractorFromPath,
    "DJZ_PromptExtractorBatch": DJZ_PromptExtractorBatch,
    "DJZ_PromptExtractorV2": DJZ_PromptExtractorV2,
    "DJZ_PromptExtractorV2_Batch": DJZ_PromptExtractorV2_Batch,
    "DJZ_PromptExtractorV2_StringNavigator": DJZ_PromptExtractorV2_StringNavigator,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "DJZ_PromptExtractor": "DJZ Prompt Extractor",
    "DJZ_PromptExtractorFromPath": "DJZ Prompt Extractor (Path)",
    "DJZ_PromptExtractorBatch": "DJZ Prompt Extractor (Batch)",
    "DJZ_PromptExtractorV2": "DJZ Prompt Extractor V2",
    "DJZ_PromptExtractorV2_Batch": "DJZ Prompt Extractor V2 (Batch)",
    "DJZ_PromptExtractorV2_StringNavigator": "DJZ String Navigator V2",
}

__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS"]

WEB_DIRECTORY = "./web"
