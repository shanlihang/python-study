### 使用说明

##### 1. 创建虚拟环境

| 环境    | 命令                  |
| ------- | --------------------- |
| Linux   | python3 -m venv .venv |
| Windows | python -m venv venv   |

##### 2. 激活虚拟环境

| 环境    | 命令                      |
| ------- | ------------------------- |
| Linux   | source .venv/bin/activate |
| Windows | .\venv\Scripts\activate   |

##### 3. 下载全部依赖

```bash
pip install -r requirements.txt
```

#### 4. 依赖写入

```bash
pip freeze > requirements.txt
```

#### 5. 退出虚拟环境

```bash
deactivate
```
