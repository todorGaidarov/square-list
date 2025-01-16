# Simple square integer list app

This is a very simple Python CLI app that given a list of integers orders them in ascending order and produces an output of the squared integers.

The app tested with python version 3.12.

# Running the app

The app is intended to be run as a docker container and so it assumes that you have
have a running local Docker installation.
The image is not uploaded to an image registry so you first need to build it:

```shell
# run from the project's root dir
docker build -t square-list .
```

To start the app run the container in interactive mode:

```shell
docker run -i square-list:latest
```

# Using the app

After running the app it will wait for user input. The input should be integers separated by spaces.

Example input to the stdin: -9 1 2 3 -4 4 6 7

To give this input to the app just press Enter and it will produce the output to the stdout.

Example output to the stdout: 81 16 1 4 9 16 36 49

To stop the app simply give it an empty input (hit enter with no input characters).
