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

import streamlit as st
import random


# PagerDuty alert simulation
def generate_alert():
    services = ["Database", "API", "Frontend", "Backend", "Network"]
    severities = ["Critical", "High", "Medium", "Low"]
    return {
        "service": random.choice(services),
        "severity": random.choice(severities),
        "message": f"Error in {random.choice(services)} service"
    }


# Streamlit app
st.title("OnCall Alert Dashboard")

# Main alert
main_alert = generate_alert()
st.error(f"🚨 ALERT: {main_alert['service']} - {main_alert['severity']}")
st.write(main_alert['message'])

# Documentation
st.header("How to Handle This Alert")
st.markdown("""
1. **Acknowledge the alert** in the PagerDuty system
2. **Investigate** the root cause of the issue
3. **Communicate** with the team using the incident communication channel
4. **Resolve** the issue or escalate if necessary
5. **Document** the incident and resolution in the post-mortem report
""")

# Related alerts
st.header("Related Alerts")
for _ in range(3):
    alert = generate_alert()
    st.warning(f"{alert['service']} - {alert['severity']}: {alert['message']}")

# Chat with bot
st.header("Chat with Support Bot")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("How can I help you with the alert?"):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Simple bot response
    response = f"I understand you're asking about '{prompt}'. For the current {main_alert['service']} alert, please follow the steps outlined in the 'How to Handle This Alert' section above. If you need more specific assistance, please provide more details about your concern."

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(response)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})
