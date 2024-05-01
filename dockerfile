FROM python:3.10-slim

WORKDIR /app

# Poetry 설치 및 가상 환경 생성 비활성화
RUN pip install poetry
RUN poetry config virtualenvs.create false

# 의존성 파일 복사
COPY pyproject.toml poetry.lock* ./

# 의존성 설치
RUN poetry install --no-dev

# 애플리케이션 코드 복사
COPY . ./

ENV PYTHONUNBUFFERED=1

CMD ["sh", "run_script.sh"]
