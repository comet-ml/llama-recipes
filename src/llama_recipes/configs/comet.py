# Copyright (c) Meta Platforms, Inc. and affiliates.
# This software may be used and distributed according to the terms of the Llama 2 Community License Agreement.

from typing import List, Optional
from dataclasses import dataclass, field

@dataclass
class comet_config:
    api_key: Optional[str] = None
    workspace: Optional[str] = None
    project: Optional[str] = None
    project_name: Optional[str] = None
    experiment_key: Optional[str] = None
    mode: Optional[str] = None
    online: Optional[bool] = None
    source: Optional[str] = None
    # TODO: Support for experiment config?