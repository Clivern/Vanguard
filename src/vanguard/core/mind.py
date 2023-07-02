# MIT License
#
# Copyright (c) 2025
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from typing import Dict, Any
from vanguard.module.database import Database
from vanguard.module.qdrant import Qdrant
from vanguard.module.openai import OpenAIClient
from vanguard.module.pagerduty import PagerdutyClient
from vanguard.module.logger import Logger


class Mind:
    def __init__(
        self,
        database_client: Database,
        qdrant_client: Qdrant,
        openai_client: OpenAIClient,
        pagerduty_client: PagerdutyClient,
        logger: Logger,
    ):
        self._database_client = database_client
        self._qdrant_client = qdrant_client
        self._openai_client = openai_client
        self._pagerduty_client = pagerduty_client
        self._logger = logger

    def store_documents(self, path: str, meta: Dict[str, Any], team: str) -> bool:
        pass

    def trigger_alert(
        self, id: str, alert: str, meta: Dict[str, Any], team: str
    ) -> bool:
        pass

    def get_relevant_data(self, text) -> str:
        pass

    def get_alert(self, id: str) -> Dict[str, Any]:
        return self._database_client.get_alert_by_id(id)

    def summarize_relevant_data(self, prompt: str, data: str) -> str:
        pass
