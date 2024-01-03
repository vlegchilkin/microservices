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
    * http://localhost:8079/docs (Mock Services)
        - http://localhost:8079/
      
    * https://localhost/ (Main Gate - HAProxy) !! Self-signed certificate, you have to accept it in your browser !!
        -  Alpha Centauri routes https://localhost/alpha-centauri/*  
        -  Observer routes https://localhost/* 
   
    * http://localhost:8081/docs (Alpha Centauri)
        - http://localhost:8081/
        - http://localhost:8081/actuator/
        - http://localhost:8081/actuator/health
        - http://localhost:8081/common/
        - http://localhost:8081/common/some-common-resource (GET/PUT/POST/DELETE/OPTIONS/HEAD/PATCH/TRACE)
        - http://localhost:8081/toliman/
        - http://localhost:8081/toliman/common/
        - http://localhost:8081/toliman/common/some-common-resource (GET/PUT/POST/DELETE/OPTIONS/HEAD/PATCH/TRACE)
        - http://localhost:8081/rigil-kentaurus/ (with HTTP Basic auth)
        - http://localhost:8081/rigil-kentaurus/common/
        - http://localhost:8081/rigil-kentaurus/common/some-common-resource (GET/PUT/POST/DELETE/OPTIONS/HEAD/PATCH/TRACE)
        - http://localhost:8081/proxima-centauri/
        - http://localhost:8081/proxima-centauri/common/
        - http://localhost:8081/proxima-centauri/common/some-common-resource (GET/PUT/POST/DELETE/OPTIONS/HEAD/PATCH/TRACE)
        - http://localhost:8081/proxima-centauri/details/

    * http://localhost:8082/docs (Observer)
        - http://localhost:8082/
        - http://localhost:8082/actuator/
        - http://localhost:8082/actuator/health
        - http://localhost:8082/celestial_sphere/skies/south/constellations/centaurus/star_systems/Alpha%20Centauri
        - http://localhost:8082/celestial_sphere/skies/south/constellations/centaurus/star_systems/Alpha%20Centauri/stars/Proxima%20Centauri
        - http://localhost:8082/celestial_sphere/skies/south/constellations/centaurus/star_systems/Alpha%20Centauri/stars/Proxima%20Centauri/planets/b
        - http://localhost:8082/celestial_sphere/skies/south/constellations/centaurus/star_systems/Alpha%20Centauri/stars/Proxima%20Centauri/planets/b/oceans/awesome
        - http://localhost:8082/mira_shadow/* (Mira mounting point (Flask), see Mira microservice)

7. available Flask endpoints:
    * http://localhost:8083/ (Mira)
        - http://localhost:8082/
        - http://localhost:8082/details/
        - http://localhost:8082/subcontext/details
        - http://localhost:8082/subcontext/view
        - http://localhost:8082/common/
        - http://localhost:8082/common/hello
        - http://localhost:8082/common/greet
        - http://localhost:8082/common/greet/YourName
        - http://localhost:8082/a
        - http://localhost:8082/a/details
        - http://localhost:8082/b
        - http://localhost:8082/b/details

