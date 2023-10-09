# Mac OS Initial setup

Open iTerm2 and change into your **Documents** directory

```bash
cd ~/Documents
```

## Clone the Data Driver GitHub repository

Inside this directory clone the Data Driver GitHub repository.

```git
git clone https://github.com/splunk/datadrivers
```

!!! info
    If the above `git` command can not be found you will have to install Xcode Command Line tools for Mac OS. This can be done by running the following:

    ```bash
    xcode-select –install
    ```

Next, change into the `f1_2023` directory:

```bash
cd datadrivers/f1-2023
```

## Create Python Virtual Environment

We now need to create a virtual Python environment and install the required Python modules:

```bash
python3 -m venv venv
. venv/bin/activate
pip3 install -r requirements.txt --upgrade
```

!!! info
    If you are using a Mac with an M1 chip you will need to install the following Python modules:

    ```bash
    pip3 install --upgrade --force --no-dependencies --no-cache-dir --no-binary :all: --compile numpy
    pip3 install --upgrade --force --no-dependencies --no-cache-dir --no-binary :all: --compile pandas
    ```

    You can then install the remaining Python modules:

    ```bash
    pip3 install -r requirements.txt --upgrade
    ```

## Start the Streamlit Web UI

```bash
```bash
streamlit run stream.py
```
