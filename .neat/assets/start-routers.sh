#!/bin/bash
set -e

sudo clickos install -s mtv-$1-c1 ./switch.click
sudo clickos install -s mtv-$1-c2 ./switch.click

sleep 1
