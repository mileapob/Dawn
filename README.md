# 执行步骤

1.安装依赖包

    pip install -r requirements.txt

    pip show fastapi uvicorn openai python-dotenv

2.添加APIKEY.env

ARK_API_KEY=你的APIKEY
ARK_MODEL=你的LLM

3.强制加载：

    export $(grep -v '^#' ./APIKEY.env | xargs)

4.确认末尾是否存在空格

    python -c "
    import os
    keys = ['DOUBAO_API_KEY']
    for k in keys:
        v = os.getenv(k, '')
        if not v:
            print(f'{k}: 空')
        else:
            print(f'{k}: OK，末尾={repr(v[-3:])}')
    "
    
5.执行app

    python3 -m uvicorn app:app --reload



