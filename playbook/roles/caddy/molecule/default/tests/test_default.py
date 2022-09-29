"""Role testing files using testinfra."""
import pytest


def test_caddy_file(host):
    f = host.file("/etc/caddy/Caddyfile")
    assert f.exists


def test_caddy_service(host):
    service = host.service("caddy")
    assert service.is_running
    assert service.is_enabled
