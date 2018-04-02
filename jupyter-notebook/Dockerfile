# TensorFlow & scikit-learn with Python3.6
FROM python:3.6.4-stretch
LABEL maintainer "david lexuszhi1990@gmail.com"


# Install dependencies
ADD sources/aliyun-debian-stretch.sources.list /etc/apt/sources.list
RUN apt-get update && apt-get install -y \
    libopenblas-dev \
    liblapack-dev \
    libgfortran3 \
    python3-setuptools \
    libopencv-dev


# Install Python library for Data Science
RUN pip install --no-cache-dir -i https://mirrors.aliyun.com/pypi/simple/  \
        jupyter \
        ipykernel \
        scipy \
        matplotlib \
        numpy \
        Pillow \
        opencv-python \
        && \
    python -m ipykernel install --name python3.6

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
EXPOSE 8888 8888

# Run Jupyter Notebook
WORKDIR "/notebooks"
CMD ["jupyter", "notebook", "--port=8888", "--allow-root"]
