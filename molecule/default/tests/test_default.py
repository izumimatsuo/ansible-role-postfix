import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_postfix_is_installed(host):
    package = host.package("postfix")
    assert package.is_installed
    assert package.version.startswith("2.10")


def test_postfix_running_and_enabled(host):
    service = host.service("postfix")
    assert service.is_running
    assert service.is_enabled


def test_postfix_listen(host):
    assert host.socket('tcp://0.0.0.0:25').is_listening
