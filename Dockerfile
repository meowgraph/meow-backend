FROM python:3.7

RUN pip install -U pip setuptools wheel -i https://pypi.tuna.tsinghua.edu.cn/simple && pip install pdm -i https://pypi.tuna.tsinghua.edu.cn/simple && mkdir Library

COPY ./ /Library

WORKDIR /Library
RUN mkdir __pypackages__ && pdm install --prod --no-lock --no-editable

ENV PYTHONPATH=/Library/__pypackages__/3.7/lib

EXPOSE 8000

