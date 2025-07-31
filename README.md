# AiValueInvesting Crew

使用 [crewai](https://crewai.com) 构建的

## Installation

支持的python版本 Python >=3.10 <3.14 
项目需要先安装crewai, crewai使用 [UV](https://docs.astral.sh/uv/)

First, if you haven't already, install uv:

```bash
pip install uv
uv tool install crewai

# 可选,安装本项目依赖
crewai install

# 项目运行
crewai run
```

### deepseek api key

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

## Support

- [crewAI](https://crewai.com)
- [ai-hedge-fund](https://github.com/virattt/ai-hedge-fund)
