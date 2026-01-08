# AnsibleRunner

AnsibleRunner 是一个基于 Ansible API 的 Python 封装库，旨在简化在 Python 项目中调用 Ansible 执行任务的过程。该项目代码参考并提取自 [Jumpserver](https://github.com/jumpserver/jumpserver) 项目。

它主要提供了 `CommandRunner` 和 `PlayBookRunner` 两个类，分别用于执行 Ad-hoc 命令和 Playbook 剧本。

## 环境要求

- Python 3.9
- Ansible == 2.8.4

## 开发与安装

本项目使用 [uv](https://github.com/astral-sh/uv) 进行 Python 版本管理和依赖管理。

### 初始化环境

确保已安装 `uv`，然后执行以下命令初始化环境并安装依赖：

```bash
uv sync
```

这将自动安装 Python 3.9 和所有必需的依赖项（包括 ansible 2.8.4）。

### 运行测试

使用 `uv run` 运行测试：

```bash
PYTHONPATH=ansiblerunner uv run pytest
```

### 手动安装 (不使用 uv)

你也可以通过 pip 手动安装所需的 Ansible 版本：

```bash
pip install ansible==2.8.4
```

## 快速开始

### 1. 定义主机清单 (Inventory)

在使用 Runner 之前，需要定义主机清单。清单是一个包含主机信息的字典列表。

```python
host_data = [
    {
        "hostname": "demo-web1",
        "ip": "192.168.33.101",
        "port": 2222,
        "username": "root",
        "private_key": "/Users/user/.ssh/id_rsa",
        # "password": "password", # 如果使用密码认证
    },
    {
        "hostname": "demo-web2",
        "ip": "192.168.33.102",
        "port": 2222,
        "username": "root",
        "private_key": "/Users/user/.ssh/id_rsa",
    },
]
```

### 2. 使用 CommandRunner 执行 Ad-hoc 命令

`CommandRunner` 用于执行简单的 Shell 命令或 Ansible 模块。

**示例：执行 `ls` 命令**

```python
from ansiblerunner import CommandRunner

# 使用上面定义的主机清单
runner = CommandRunner(inventory=host_data)

# 执行 ls 命令
# pattern: 匹配的主机模式，默认为 'all'
# module: 使用的 ansible 模块，默认为 'shell'
result = runner.execute('ls', pattern='all')

# 获取结果
print(result.results_command)
print(result.results_raw)
```

**示例：使用 `ping` 模块**

```python
tasks = [
    {"action": {"module": "ping", "args": ""}, "name": "check connect"}
]
runner.run(tasks, pattern='all')
```

### 3. 使用 PlayBookRunner 执行剧本

`PlayBookRunner` 用于执行 YAML 格式的 Ansible Playbook。

**示例：运行 Playbook**

```python
from ansiblerunner import PlayBookRunner

# 指定目标主机、Playbook 路径和清单
# 注意：PlayBookRunner 的构造函数参数稍有不同，通常针对单次运行或通过 inventory 对象
runner = PlayBookRunner(
    hostname='demo-web1',
    path='/path/to/playbook.yml',
    inventory=host_data
)

runner.run()
```

## 高级用法

### 传递选项 (Options)

你可以通过 `options` 参数传递 Ansible 的配置选项，例如并发数、超时时间等。

```python
options = {
    'forks': 10,
    'timeout': 60,
    'remote_user': 'root',
    # 其他 ansible.cfg 中的配置
}

runner = CommandRunner(inventory=host_data, options=options)
```

### 回调 (Callback) 结果说明

执行结果通常包含以下结构：

- `results_raw`: 原始的执行结果，包含 `ok`, `failed`, `unreachable`, `skipped` 等状态的详细信息。
- `results_summary`: 结果摘要，包含 `contacted` (成功连接), `dark` (无法连接), `success` (总体是否成功)。

**CommandRunner 特有结果:**
- `results_command`: 针对 shell/command 模块优化后的结果，包含 `cmd`, `stdout`, `stderr`, `rc` 等字段。

## 许可证

本项目遵循开源许可证。详情请参阅源代码。
