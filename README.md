# A股价值投资AI Agent

使用 [crewai](https://crewai.com) 构建

## Installation

支持的python版本 Python >=3.10 <3.14 
项目需要先安装crewai, crewai使用 [UV](https://docs.astral.sh/uv/)


```bash
pip install crewai
# 或者
pip install uv
uv tool install crewai 

# 可选,安装本项目依赖
crewai install

# 项目运行
crewai run
```

### 设置环境变量 deepseek api key

**新增项目根目录.env,添加 `DEEPSEEK_API_KEY` 到文件中**
```
MODEL=deepseek/deepseek-chat
DEEPSEEK_API_KEY=your api key
```

### web ui

```
uv pip install gradio
# 进入项目根目录
python3 src/ai_value_investing/app.py
```

## 引用

- [crewAI](https://crewai.com)
- [ai-hedge-fund](https://github.com/virattt/ai-hedge-fund)
