from typing import Dict, Any
from beaker_kernel.lib.context import BeakerContext

from .agent import BDIKitAgent

class BDIKitContext(BeakerContext):

    enabled_subkernels = ["python3"]

    SLUG = "bdikit_context"

    def __init__(self, beaker_kernel: "BeakerKernel", config: Dict[str, Any]):
        super().__init__(beaker_kernel, BDIKitAgent, config)

    async def setup(self, context_info=None, parent_header=None):
        super().setup(context_info, parent_header)

    async def auto_context(self):
            return f"""
            You are an assistant helping biomedical researchers harmonize their data. If you are asked to perform a Pandas operation
            you should NOT print the results by default. Instead, acknowledge that the operation has been performed. The user can print
            the head of the dataframe if they so choose.

            You are an expert in the use of NYU's BDIKit library. You have access to the following functions:
                - match_schema: This function performs schema mapping between the source table and the given target schema. 
            """.strip()