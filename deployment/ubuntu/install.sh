#!/bin/bash

function deps {
    echo "Installing dependencies ..."

    apt-get update
    apt-get upgrade -y

    echo "Installing dependencies done!"
}

function sloth {
    echo "Installing sloth ..."

    mkdir -p /etc/sloth
    cd /etc/sloth
    LATEST_VERSION=$(curl --silent "https://api.github.com/repos/norwik/sloth/releases/latest" | jq '.tag_name' | sed -E 's/.*"([^"]+)".*/\1/' | tr -d v)
    curl -sL https://github.com/norwik/sloth/releases/download/v{$LATEST_VERSION}/sloth_{$LATEST_VERSION}_Linux_x86_64.tar.gz | tar xz

    echo "[Unit]
Description=sloth
Documentation=https://github.com/norwik/sloth

[Service]
ExecStart=/etc/sloth/sloth server -c /etc/sloth/config.prod.yml
Restart=on-failure
RestartSec=2

[Install]
WantedBy=multi-user.target" > /etc/systemd/system/sloth.service

    systemctl daemon-reload
    systemctl enable sloth.service
    systemctl start sloth.service

    echo "Sloth installation done!"
}

deps
sloth
