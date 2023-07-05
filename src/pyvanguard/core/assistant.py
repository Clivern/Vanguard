# MIT License
#
# Copyright (c) 2025 Clivern
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

from pyvanguard.module.database import Database
from pyvanguard.module.qdrant import Qdrant
from pyvanguard.module.openai import OpenAIClient
from pyvanguard.module.pagerduty import PagerdutyClient
from pyvanguard.module.logger import Logger
from pyvanguard.module.file_system import FileSystem
from pyvanguard.module.jira import JiraClient


class Assistant:
    """
    Assistant Functionality of PyVanguard
    """

    def __init__(
        self,
        database_client: Database,
        qdrant_client: Qdrant,
        openai_client: OpenAIClient,
        pagerduty_client: PagerdutyClient,
        jira_client: JiraClient,
        logger: Logger,
        file_system: FileSystem,
    ):
        """
        Initialize the Mind class with the necessary clients and logger.

        Args:
            database_client (Database): An instance of the Database client for database operations.
            qdrant_client (Qdrant): An instance of the Qdrant client for vector database operations.
            openai_client (OpenAIClient): An instance of the OpenAI client for generating embeddings.
            pagerduty_client (PagerdutyClient): An instance of the PagerDuty client for alert management.
            logger (Logger): An instance of the Logger for logging operations.
            file_system (FileSystem): An instance of the FileSystem for reading documents from disk.
        """
        self._database_client = database_client
        self._qdrant_client = qdrant_client
        self._openai_client = openai_client
        self._pagerduty_client = pagerduty_client
        self._jira_client = jira_client
        self._logger = logger
        self._file_system = file_system

    def setup(self):
        """
        Setup dependencies by connecting to the database and ensuring the Qdrant collection exists.

        This method should be called before performing any other operations to ensure that all
        necessary connections are established and collections are available.
        """
        self._database_client.connect()
        self._database_client.migrate()
        self._qdrant_client.create_collection_if_not_exist("pyvanguard")

    def summarize_relevant_data(self, prompt: str, data: str) -> str:
        """
        Summarize relevant data using OpenAI's API based on a given prompt.

        Args:
            prompt (str): The prompt guiding how to summarize data.
            data (str): The data that needs summarization.

        Returns:
            str: The summarized version of the provided data or an empty string if an error occurs.

        This method should implement logic to summarize relevant data using
        OpenAI's API. Currently not implemented.
        """
        pass


def get_assistant(
    database_client: Database,
    qdrant_client: Qdrant,
    openai_client: OpenAIClient,
    pagerduty_client: PagerdutyClient,
    jira_client: JiraClient,
    logger: Logger,
    file_system: FileSystem,
) -> Assistant:
    """
    Get Assistant Class Instance
    """
    return Assistant(
        database_client,
        qdrant_client,
        openai_client,
        pagerduty_client,
        jira_client,
        logger,
        file_system,
    )
