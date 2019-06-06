# Sample task starter

Here you'll find a skeleton project for a simple Flask API.
To include private configuration, rename `config/private_RENAME_THIS.py` to `private.py`. Keep secret credentials there.

Build the docker image:  
`sudo docker build -t sampletask .`

Run the docker image:
`sudo docker run --net="host" sampletask`


The "Hello world!" can now be observed on   localhost at port 5000. 

### Explanations

I was trying to deal with this organization with flask and things I didn't know about python, like how to use C-pthread libraries like in python, or even if I had to do it.

Was I guess I had to do is to simulate the backbone of the system. And I did it.

I would just need more time to make it works properly.

### Plans
 - I will learn how to use and use python libraries to send any request to a free core in the processors. I heard about Hadoop in a database event one time, but I don't know if its fit, just has to seek a little bit more.
 - I have read a little bit of AWS lambda functions - Serverless backend, as I understood, maybe would help to minimize the costs of our hypothetical company, and could be as scalable as we want if we just use the horizontal scalability, sending requests to be requested by free cores. Supposing infinite cores at AWS we could have only the ping and the processing as response time, avoiding the problem with overload in the old approach.