FROM python:3.7

RUN pip install -U pip setuptools wheel -i https://pypi.tuna.tsinghua.edu.cn/simple && pip install pdm -i https://pypi.tuna.tsinghua.edu.cn/simple

WORKDIR /home/Library
COPY ./ ./
RUN mkdir __pypackages__ && pdm install --prod --no-lock --no-editable && mv data/words.vector.gz __pypackages__/3.7/lib/synonyms/data

ENV PYTHONPATH=/home/Library/__pypackages__/3.7/lib

EXPOSE 8000

