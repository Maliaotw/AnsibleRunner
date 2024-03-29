# AnsibleRunner

拷貝自jumpserver項目

# install 

```
pip install ansible==2.8.4
```


## Runner

**Ansible Command Runner**

simple runner

```
runner = CommandRunner()
runner.execute('ls')
```

inventory hosts

```

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
runner = CommandRunner(inventory=host_data)
runner.execute('ls')
```


**Ansible Playbook Runner**

simple runner

```
runner = PlayBookRunner(hostname='maliao-web1',path='test.yml')
runner.run()
```


option 

```
runner1 = PlayBookRunner(hostname='maliao-web1', path='test.yml',options={'memory_mb': 1024, 'size_gb': 30,'num_cpus': 2})
runner1.run()
```

inventory hosts


```
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

runner2 = PlayBookRunner(hostname='maliao-web1', path='test.yml', inventory=hosts)
runner2.run()
```


## Callback

gather_result


任務開始
v2_playbook_on_play_start

任務成功
v2_runner_on_ok 

無法連接
v2_runner_on_unreachable 

任務失敗
v2_runner_on_failed 









