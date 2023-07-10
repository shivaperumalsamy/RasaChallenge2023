FROM rasa/rasa:2.8.25-full as rasa-core
WORKDIR /app
COPY . /app
COPY requirements.txt /app
USER root
RUN python -m pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
RUN rasa train
# Creates a non-root user and adds permission to access the /app folder
RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app
USER appuser
EXPOSE 5005
CMD [ "run", "--enable-api", "--cors", "'*'"]


FROM rasa/rasa-sdk:2.8.4 as rasa-actions
WORKDIR /app
COPY actions /app/actions
COPY actions/requirements-actions.txt /app
COPY constants /app/constants
COPY utils /app/utils
USER root
RUN pip install --no-cache-dir -r requirements-actions.txt
RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app
USER appuser
USER 1001
EXPOSE 5055
# CMD ["run", "actions"]
