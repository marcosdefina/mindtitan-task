# Sample task starter

Here you'll find a skeleton project for a simple Flask API.
To include private configuration, rename `config/private_RENAME_THIS.py` to `private.py`. Keep secret credentials there.

Build the docker image:  
`sudo docker build -t sampletask .`

Run the docker image:
`sudo docker run --net="host" sampletask`


The "Hello world!" can now be observed on   localhost at port 5000. 