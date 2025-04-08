import subprocess  
import time  
from pathlib import Path  
  
from mcp.server.fastmcp import FastMCP  
  
# Initialize FastMCP server  
mcp = FastMCP("fscan_mcp-server", log_level="ERROR")  
  
@mcp.tool()  
#此参数ip为input大模型输入变量，后续可设定更多变量；如不启用漏洞扫描，仅扫描web，自动漏洞利用等
async def fscan_mcp_server(ip: str) -> dict:  
    """  
    执行端口扫描工具
  
    参数:  
        ip (str): 要扫描的ip 
    返回:  
        返回扫描结果，并对扫描结果中web服务进一步检测是否存在漏洞
        
    """  
    start_time = time.time()  
    result = {  
        "status": "pending",  
        "command": "",  
        "returncode": None,  
        "stdout": "",  
        "stderr": "",  
        "duration": 0.0  
    }  
    # 配置固定参数  
    target_dir = r"E:\\AI\\SecMate\\MCP\\fscan_MCP"
    exe_path = str(Path(target_dir) / "fscan.exe")    

    # go_cmd 为所执行的命令
    go_cmd = [exe_path, "-h", ip,"nopoc","np",'-p']         

    # 验证所配置的工具环境是否存在
    if not Path(exe_path).exists():  # 关键修改点3  
        raise FileNotFoundError(f"fscan.exe not found in {target_dir}")  

    # 记录完整命令  
    result["command"] = " ".join(go_cmd)  

    # 执行命令  
    process = subprocess.run(  
        go_cmd,  
        cwd=target_dir,  
        stdout=subprocess.PIPE,  
        stderr=subprocess.PIPE,  
        encoding='utf-8',  
        errors='replace'  
    )  

    # 记录结果  
    result.update({  
        "status": "success",  
        "returncode": process.returncode,  
        "stdout": process.stdout.strip(),  
        "stderr": process.stderr.strip(),  
        "duration": round(time.time() - start_time, 2)  
    })  
    return result  
  
if __name__ == "__main__":  
    mcp.run(transport="stdio")