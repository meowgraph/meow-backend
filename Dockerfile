FROM python:3.7

RUN pip install -U pip setuptools wheel -i https://pypi.tuna.tsinghua.edu.cn/simple && pip install pdm -i https://pypi.tuna.tsinghua.edu.cn/simple && git clone https://github.com/meowgraph/meow-backend.git

COPY data/ /meow-backend/data

WORKDIR /meow-backend
RUN mkdir __pypackages__ && pdm install --prod --no-lock --no-editable

ENV PYTHONPATH=/meow-backend/__pypackages__/3.7/lib

EXPOSE 8000

CMD ["pdm", "run", "start"]

