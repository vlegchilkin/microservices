# Various microservice examples

1. git clone https://github.com/vlegchilkin/python-infra

2. follow https://github.com/vlegchilkin/python-infra/blob/main/README.md, as a result:
    - devpi & local docker registry should be up and running
    - localhost:5001/docker-python:3.12 have to be resolvable
    - localhost:5001/docker-python:3.9 have to be resolvable
    - http://127.0.0.1:3141/root (devpi) should be available and have 'root/local' index

3. git clone https://github.com/vlegchilkin/mscom

4. follow https://github.com/vlegchilkin/mscom/blob/main/README.md, as a result:
   - http://127.0.0.1:3141/root/local has 'mscom' package

5. run:
   ```shell
   docker-compose up -d
   ```

6. available FastAPI endpoints:
    * http://localhost:8079/docs
        - http://localhost:8079/

    * http://localhost:8081/docs
        - http://localhost:8081/
        - http://localhost:8081/actuator/
        - http://localhost:8081/actuator/health
        - http://localhost:8081/common/
        - http://localhost:8081/toliman/
        - http://localhost:8081/toliman/common/
        - http://localhost:8081/rigil-kentaurus/ (with HTTP Basic auth)
        - http://localhost:8081/rigil-kentaurus/common/
        - http://localhost:8081/proxima-centauri/
        - http://localhost:8081/proxima-centauri/common/
        - http://localhost:8081/proxima-centauri/details/
