FROM jupyter/scipy-notebook:latest
MAINTAINER david lexuszhi1990@gmail.com

RUN pip install -i https://mirrors.aliyun.com/pypi/simple/ opencv-python

RUN jupyter notebook --generate-config
RUN sed "s/#c.NotebookApp.token = '<generated>'/c.NotebookApp.token = 'your-token'/" /home/jovyan/.jupyter/jupyter_notebook_config.py -i

EXPOSE 8888
CMD jupyter notebook --port=8888 --ip 0.0.0.0 --no-browser --allow-root

