# 执行步骤

1.添加APIKEY.env

DOUBAO_API_KEY=你的APIKEY

2.强制加载：

    export $(grep -v '^#' ./APIKEY.env | xargs)

3.确认末尾是否存在空格

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



