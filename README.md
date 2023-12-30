# Various microservice examples

1. git clone https://github.com/vlegchilkin/python-infra

2. follow https://github.com/vlegchilkin/python-infra/blob/main/README.md, as a result:
   - devpi & local docker registry should be up and running
   - localhost:5001/docker-python:3.12 have to be resolvable 
   - localhost:5001/docker-python:3.9 have to be resolvable 
   - http://127.0.0.1:3141/root (devpi) should be available and have 'root/local' index
   
3. run:
   ```shell
   docker-compose up -d
   ```

4. available FastAPI endpoints:
   - http://localhost:8079/
   - http://localhost:8081/
   - http://localhost:8081/toliman/
   - http://localhost:8081/rigil-kentaurus/
   - http://localhost:8081/proxima-centauri/
   - http://localhost:8081/proxima-centauri/details/
