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

import os
from vanguard.module import (
    get_logger,
    get_database_client,
    get_openai_client,
    get_pagerduty_client,
    get_qdrant_client,
    get_file_system,
)
from vanguard.core import get_mind
from rich.console import Console


class LoadCommand:
    """
    Load Team Documentation into RAG Command
    """

    def __init__(self):
        self._mind = get_mind(
            get_database_client(os.getenv("SQLITE_DB_PATH")),
            get_qdrant_client(
                os.getenv("QDRANT_DB_URL"), os.getenv("QDRANT_DB_API_KEY")
            ),
            get_openai_client(os.getenv("OPENAI_API_KEY")),
            get_pagerduty_client(os.getenv("PAGERDUTY_INTEGRATION_KEY")),
            get_logger(),
            get_file_system(),
        )
        self._console = Console()

    def run(self, dir_path: str, team_name: str):
        try:
            self._mind.setup()
            self._mind.store_documents(dir_path, team_name, {})
            message = "Documentation loaded successfully!"
            self._console.print(f"[bold green][SUCCESS][/bold green] {message}")
        except Exception as e:
            message = f"raised error is {e}"
            self._console.print(f"[bold red][ERROR][/bold red] {message}")
