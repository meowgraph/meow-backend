FROM python:3.10 AS builder

RUN pip install -U pip setuptools wheel
RUN pip install pdm

COPY pyproject.toml pdm.lock README.md /project/
COPY src/ /project/src

WORKDIR /project
RUN mkdir __pypackages__ && pdm install --prod --no-lock --no-editable

FROM python:3.10

ENV PYTHONPATH=/project/pkgs
COPY --from=builder /project/__pypackages__/3.10/lib /project/pkgs

CMD ["python", "-m", "project"]

