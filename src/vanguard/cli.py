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

import click

from vanguard import __version__
from vanguard.command import LoadCommand, AlertCommand, AssistantCommand


@click.group(help="🐺 Oncall AI Assistant.")
@click.version_option(version=__version__, help="Show the current version")
def main():
    """Main command group for Vanguard CLI."""
    pass


@main.command(help="Load documentation into the RAG")
def load(name):
    LoadCommand().run(name)


@main.command(help="Run the AI Assistant")
def assistant():
    AssistantCommand().run()


@main.command(help="Send a PagerDuty Alert")
def alert():
    AlertCommand().run()


if __name__ == "__main__":
    main()
