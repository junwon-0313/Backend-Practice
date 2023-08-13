# FastAPI를 학습합니다.

- boostcamp

    - [노션](https://www.notion.so/junwon-0313/FastAPI-7acc8b3061e14f1781b5cfa54a6d1c41): Private

    - [GCP](https://console.cloud.google.com/) : Logging with BigQuery

        1. 빅쿼리에 테이블을 세팅
        2. 빅쿼리에 적재하기 쉽게 JSON 형태로 로그를 정제
        3. python logging 모듈을 사용해, 빅쿼리에 실시간 로그 적재
        4. console과 file에도 기록이 남도록 handler를 지정

        서비스 계정을 적절한 권한을 부여해 생성하고 키를 다운 받아 사용해야한다!

    - [MLflow](https://mlflow.org/docs/latest/index.html)

        ``` bash
        mlflow experiments create --experiment-name my-first-experiment

        mlflow run logistic_regression --experiment-name my-first-experiment --no-conda
        ```
---

- tutorial

    - [FastAPI](https://fastapi.tiangolo.com/ko/tutorial/)

    - [Pydantic](https://docs.pydantic.dev/latest/)