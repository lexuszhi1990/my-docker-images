FROM jupyter/scipy-notebook:latest
MAINTAINER david lexuszhi1990@gmail.com

RUN pip install -i https://mirrors.aliyun.com/pypi/simple/ opencv-python

RUN jupyter notebook --generate-config
RUN sed "s/#c.NotebookApp.token = '<generated>'/c.NotebookApp.token = 'your-token'/" /home/jovyan/.jupyter/jupyter_notebook_config.py -i

EXPOSE 8888
CMD jupyter notebook --port=8888 --ip 0.0.0.0 --no-browser --allow-root

ADD sources.list /etc/apt/sources.list
RUN apt-get update
RUN apt-get install python3-pip -y
RUN pip3 install mxnet-cu90mkl numpy -i https://pypi.douban.com/simple/


RUN apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Install TensorFlow CPU version
ENV TENSORFLOW_VERSION 1.5.0
RUN pip --no-cache-dir install \
    http://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-${TENSORFLOW_VERSION}-cp36-cp36m-linux_x86_64.whl


python -m ipykernel.kernelspec

[root@pydev pydev]# jupyter-kernelspec list
Available kernels:
  python2    /usr/lib/python2.7/site-packages/ipykernel/resources

pip3 install ipykernel

[root@pydev ~]# python3 -m ipykernel install --name python3 --display-name "Python3.5.2"
Installed kernelspec python3 in /usr/local/share/jupyter/kernels/python3
[root@pydev ~]# jupyter-kernelspec list
Available kernels:
  python2    /usr/lib/python2.7/site-packages/ipykernel/resources
  python3    /usr/local/share/jupyter/kernels/python3


RUN pip install --no-cache-dir -i https://mirrors.aliyun.com/pypi/simple/  \
        jupyter \
        ipykernel \
        scipy \
        matplotlib \
        numpy \
        Pillow \
        opencv-python \
        && \
    python -m ipykernel install --name python2.7
