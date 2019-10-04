# -*- coding: utf-8 -*-
#

import unittest
import sys

# sys.path.insert(0, "../..")

from runner import PlayBookRunner, AdHocRunner, CommandRunner
from inventory import BaseInventory


class TestPlaybookRunner(unittest.TestCase):
    def setUp(self):
        self.runner = PlayBookRunner(hostname='maliao-web1', path='test.yml')
        self.runner1 = PlayBookRunner(hostname='maliao-web1', path='test.yml',
                                      options={'newhost': 'maliao-web1', 'memory_mb': 1024, 'size_gb': 30,
                                               'num_cpus': 2})

        hosts = [
            {
                "hostname": 'maliao-web1',
                "ip": '192.168.1.1',
                "port": '22',
                "username": "root",
                "private_key": "/Users/maliao/.ssh/id_rsa"
            },
            {
                "hostname": 'maliao-web1',
                "ip": '192.168.1.1',
                "port": '22',
                "username": "root",
                "private_key": "/Users/maliao/.ssh/id_rsa"
            },
        ]

        self.runner2 = PlayBookRunner(hostname='maliao-web1', path='test.yml', inventory=hosts)
        # self.runner.playbook_path =

    def test_run(self):
        ret = self.runner.run()
        print(ret)
        # print(ret.results_summary)
        # print(ret.results_raw)


class TestAdHocRunner(unittest.TestCase):
    def setUp(self):
        host_data = [
            {
                "hostname": "testserver1",
                "ip": "192.168.33.101",
                "port": 22,
                "username": "maliao",
                "password": "123456",
            },
        ]
        inventory = BaseInventory(host_data)
        self.runner = AdHocRunner(inventory)

    def test_run(self):
        tasks = [
            {"action": {"module": "shell", "args": "ls"}, "name": "run_cmd"},
            {"action": {"module": "shell", "args": "whoami"}, "name": "run_whoami"},
        ]
        ret = self.runner.run(tasks, "all")
        print(ret.results_summary)
        print(ret.results_raw)


class TestPingRunner(unittest.TestCase):
    def setUp(self):
        host_data = [
            {
                "hostname": "demo-web1",
                "ip": "192.168.33.101",
                "port": 2222,
                "username": "root",
                "private_key": "/Users/maliao/.ssh/id_rsa",
            },
            {
                "hostname": "demo-web2",
                "ip": "192.168.33.102",
                "port": 2222,
                "username": "root",
                "private_key": "/Users/maliao/.ssh/id_rsa",
            },
            {
                "hostname": "demo-web3",
                "ip": "192.168.33.103",
                "port": 2222,
                "username": "root",
                "private_key": "/Users/maliao/.ssh/id_rsa",
            },
            {
                "hostname": "demo-web4",
                "ip": "192.168.33.104",
                "port": 2222,
                "username": "root",
                "private_key": "/Users/maliao/.ssh/id_rsa",
            },

        ]
        inventory = BaseInventory(host_data)
        self.runner = CommandRunner(inventory)

    def test_ping(self):
        tasks = [
            {"action": {"module": "ping", "data": "pong"}, "name": "check connect to host"},
        ]

        # ret = self.runner.run(tasks, "all")
        ret = self.runner.run(tasks, "demo*")
        print(ret.results_summary)
        print(ret.results_raw)

    def test_idrac(self):
        tasks = [
            {"action": {"module": "shell", "args": "racadm getsysinfo"}, "name": "check connect to host"},
        ]

        # ret = self.runner.run(tasks, "all")
        ret = self.runner.run(tasks, "esxi1*")
        print(ret.results_summary)
        print(ret.results_raw)


class TestCommandRunner(unittest.TestCase):
    def setUp(self):
        host_data = [
            {
                "hostname": "demo-web1",
                "ip": "192.168.33.101",
                "port": 2222,
                "username": "root",
                "private_key": "/Users/maliao/.ssh/id_rsa",
            },
            {
                "hostname": "demo-web2",
                "ip": "192.168.33.102",
                "port": 2222,
                "username": "root",
                "private_key": "/Users/maliao/.ssh/id_rsa",
            },
            {
                "hostname": "demo-web3",
                "ip": "192.168.33.103",
                "port": 2222,
                "username": "root",
                "private_key": "/Users/maliao/.ssh/id_rsa",
            },
            {
                "hostname": "demo-web4",
                "ip": "192.168.33.104",
                "port": 2222,
                "username": "root",
                "private_key": "/Users/maliao/.ssh/id_rsa",
            },
        ]
        # inventory = BaseInventory(host_data)
        self.runner = CommandRunner(inventory=host_data)

    def test_execute(self):
        # res = self.runner.execute('ls', 'all')
        res = self.runner.execute(cmd='ls', pattern='all')
        print(res.results_command)
        print(res.results_raw)


if __name__ == '__main__':
    unittest.main()
