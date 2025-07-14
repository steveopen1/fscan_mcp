# fscan MCP 项目指南

## 项目概述
fscan MCP 是一个基于 fscan 工具的端口扫描和漏洞检测的 MCP 服务封装。项目通过 FastMCP 框架提供标准化的接口，便于集成到其他系统中。

## 项目结构
```
├── brute-passwd/       # 爆破字典目录
├── .trae/              # 项目规则配置
├── config.py           # 配置文件
├── fscan.exe           # fscan 可执行文件
├── fscan_mcp_server.py # 主服务文件
├── logger.py           # 日志模块
├── pyproject.toml      # 项目配置文件
└── README.md           # 项目说明文档
```

## 使用流程
1. **初始化环境**
   - 确保系统已安装 Python 3.12+ 环境
   - 安装项目依赖：`pip install -r requirements.txt`

2. **启动服务**
   - 运行主服务：`uv --directory /path/to/fscan_mcp --with mcp mcp run fscan_mcp_server.py`

3. **调用服务**
   - 通过 MCP 协议调用 fscan_mcp_server 工具
   - 支持参数：
     - `ip` (str): 目标 IP 地址，必填参数
     - `port_range` (str): 端口范围，默认 1-65535
     - `proxy` (str): 代理地址，可选
     - `output_path` (str): 输出文件路径，可选
     - `input_file` (str): 输入文件路径，可选
     - `report` (bool): 是否生成报告，默认 False
     - `vuln_scan` (bool): 是否进行漏洞扫描，默认 False

4. **结果处理**
   - 扫描结果通过 stdout 返回
   - 报告文件保存在指定路径

## 关键模块
- **fscan_mcp_server.py**: 主服务模块，封装 fscan 工具的 MCP 接口
- **config.py**: 配置文件，包含扫描参数和漏洞检测配置
- **logger.py**: 日志模块，记录服务运行状态

## 注意事项
- 确保 fscan.exe 文件存在于项目根目录
- 扫描前请确认目标系统是否允许进行端口扫描


# 提示词:
// 提示词部分:用户可设定在server内部也可设定在客户端，为了更好的体验建议设定在server内部,避免调用时出现问题,默认未添加
## 语言设定
	使用中文进行交互与输出。
## 触发机制与操作流程（调用fscan_mcp）
	当系统接收到用户输入的 IP 地址时，需立即调用 fscan_mcp 工具对该 IP 地址进行全面扫描。扫描任务完成后，按照以下逻辑进行后续操作：
## 报告生成要求（调用工具阶段）
 所有生成的结果都存放在/fscan_result目录下
	2.**可视化内容**：依据(逻辑处理)的结果进行生成,使用工具生成标准化、格式化的端口检测报告.html文件
	3.将所有web资产进行收集保存为result_url.txt(基础写入至txt)
