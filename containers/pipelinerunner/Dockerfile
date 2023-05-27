FROM python:3.9.5

# set up location of code
WORKDIR /code
ENV PYTHONPATH=/code/src

# install python requirements
ADD ./containers/pipelinerunner/requirements.txt requirements.txt

RUN pip install --verbose -r requirements.txt

# copy repo
COPY ./ ./code/
