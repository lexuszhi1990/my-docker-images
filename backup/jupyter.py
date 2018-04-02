FROM jupyter/scipy-notebook:latest
MAINTAINER david lexuszhi1990@gmail.com

RUN pip install -i https://mirrors.aliyun.com/pypi/simple/ opencv-python

RUN jupyter notebook --generate-config
RUN sed "s/#c.NotebookApp.token = '<generated>'/c.NotebookApp.token = 'your-token'/" /home/jovyan/.jupyter/jupyter_notebook_config.py -i

EXPOSE 8888
CMD jupyter notebook --port=8888 --ip 0.0.0.0 --no-browser --allow-root



RUN apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Install TensorFlow CPU version
ENV TENSORFLOW_VERSION 1.5.0
RUN pip --no-cache-dir install \
    http://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-${TENSORFLOW_VERSION}-cp36-cp36m-linux_x86_64.whl
