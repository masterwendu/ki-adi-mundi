#!/bin/bash
set -e

# start server
echo "[INFO] Run nginx"
exec nginx -c /etc/nginx.conf < /dev/null
