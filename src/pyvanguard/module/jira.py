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

import requests
import base64
import json


class JiraClient:
    """
    A client for interacting with the Jira API.
    """

    def __init__(self, email: str, api_key: str, domain: str):
        """
        Initialize the Jira client with credentials.

        Args:
            email (str): Your Jira account email.
            api_key (str): Your Jira API token.
            domain (str): Your Jira domain (e.g., your-domain.atlassian.net).
        """
        self._email = email
        self._api_key = api_key
        self._domain = domain
        self._base_url = f"https://{domain}.atlassian.net/rest/api/3"

        # Encode the credentials
        credentials = base64.b64encode(f"{email}:{api_key}".encode("utf-8")).decode(
            "utf-8"
        )

        self._headers = {
            "Authorization": f"Basic {credentials}",
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

    def create_issue(
        self, project_id: str, issue_type_id: str, summary: str, description: str
    ):
        """
        Create a new issue in Jira.

        Args:
            project_id (str): ID of the project where the issue will be created.
            issue_type_id (str): ID of the issue type (e.g., Bug, Task).
            summary (str): Summary of the issue.
            description (str): Description of the issue.

        Returns:
            requests.Response: Response from the Jira API.
        """
        payload = {
            "fields": {
                "project": {"id": project_id},
                "summary": summary,
                "description": {
                    "type": "doc",
                    "version": 1,
                    "content": [
                        {
                            "type": "paragraph",
                            "content": [{"text": description, "type": "text"}],
                        }
                    ],
                },
                "issuetype": {"id": issue_type_id},
            }
        }

        payload_json = json.dumps(payload)
        url = f"{self._base_url}/issue"
        response = requests.post(url, headers=self._headers, data=payload_json)

        return response


def get_jira_client(email: str, api_key: str, domain: str) -> JiraClient:
    """
    Create and return a Jira client instance.

    Args:
        email (str): Your Jira account email.
        api_key (str): Your Jira API token.
        domain (str): Your Jira domain.

    Returns:
        JiraClient: An instance of JiraClient configured with the provided credentials.
    """
    return JiraClient(email, api_key, domain)
