# TensorFlow & scikit-learn with Python3.6
FROM ubuntu:18.04
LABEL maintainer "david lexuszhi1990@gmail.com"

# Install dependencies
RUN sed -i 's/archive.ubuntu.com/mirrors.aliyun.com/g' /etc/apt/sources.list

RUN apt-get update --fix-missing && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y \
    python-pip \
    python3-pip \
    python3-setuptools \
    libopencv-dev


# https://stackoverflow.com/questions/8671308/non-interactive-method-for-dpkg-reconfigure-tzdata
RUN echo "Asia/Hong_Kong" > /etc/timezone && dpkg-reconfigure -f noninteractive tzdata


# Install Python library for Data Science
RUN pip3 install --no-cache-dir -i https://mirrors.aliyun.com/pypi/simple/  \
        jupyter \
        ipykernel \
        scipy \
        matplotlib \
        numpy \
        Pillow \
        opencv-python \
        && \
    python3.6 -m ipykernel install --name python3.6


# Set up Jupyter Notebook config
ENV CONFIG /root/.jupyter/jupyter_notebook_config.py
ENV CONFIG_IPYTHON /root/.ipython/profile_default/ipython_config.py

RUN jupyter notebook --generate-config --allow-root && \
    ipython profile create

RUN echo "c.NotebookApp.ip = '0.0.0.0'" >>${CONFIG} && \
    echo "c.NotebookApp.open_browser = False" >>${CONFIG} && \
    echo "c.NotebookApp.iopub_data_rate_limit=10000000000" >>${CONFIG} && \
    echo "c.MultiKernelManager.default_kernel_name = 'python3'" >>${CONFIG}

RUN echo "c.InteractiveShellApp.exec_lines = ['%matplotlib inline']" >>${CONFIG_IPYTHON}

# port
EXPOSE 8888

# Run Jupyter Notebook
WORKDIR "/notebooks"
CMD ["jupyter", "notebook", "--port=8888", "--allow-root"]
