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
   poetry update --lock
   docker-compose up -d
   ```
6. While editing Django endpoints, mark `django/src` folder as Sources root for correct resolving

7. available FastAPI endpoints:
    * http://localhost:8079/docs (Mock Services)
        - http://localhost:8079/
      
    * https://localhost/ (Main Gate - HAProxy) !! Self-signed certificate, you have to accept it in your browser !!
        -  Alpha Centauri routes https://localhost/alpha-centauri/*  
        -  Observer routes https://localhost/*
        -  Django routes https://localhost/django/*
   
    * http://localhost:8081/docs (Alpha Centauri)
        - http://localhost:8081/
        - http://localhost:8081/actuator/
        - http://localhost:8081/actuator/health
        - http://localhost:8081/common/
        - http://localhost:8081/common/some-common-resource (GET/PUT/POST/DELETE/OPTIONS/HEAD/PATCH/TRACE)
        - http://localhost:8081/toliman/
        - http://localhost:8081/toliman/common/
        - http://localhost:8081/rigil-kentaurus/ (with HTTP Basic auth)
        - http://localhost:8081/rigil-kentaurus/common/
        - http://localhost:8081/proxima-centauri/
        - http://localhost:8081/proxima-centauri/common/
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

8. available Flask endpoints:
    * http://localhost:8083/ (Mira)
        - http://localhost:8083/
        - http://localhost:8083/details/
        - http://localhost:8083/subcontext/details
        - http://localhost:8083/subcontext/view
        - http://localhost:8083/common/
        - http://localhost:8083/common/hello
        - http://localhost:8083/common/greet
        - http://localhost:8083/common/greet/YourName
        - http://localhost:8083/a
        - http://localhost:8083/a/details
        - http://localhost:8083/b
        - http://localhost:8083/b/details

9. available Django endpoints:
   * http://localhost:8084/ (Django)
        - http://localhost:8084/admin/* (lots of endpoints by Django admin)
        - http://localhost:8084/basic/function-view
        - http://localhost:8084/basic/function-view-with-if (post and get)
        - http://localhost:8084/basic/function-view-with-decorator
        - http://localhost:8084/basic/class-view
        - http://localhost:8084/basic/class-view-with-decorator
        - http://localhost:8084/basic/template-class-view
        - http://localhost:8084/basic/regexp-url/2024
        - http://localhost:8084/wrapped-view/cached-view
        - http://localhost:8084/wrapped-view/require-post
        - http://localhost:8084/wrapped-view/csrf_exempt
        - http://localhost:8084/wrapped-view/permission_required
        - http://localhost:8084/auth/token
        - http://localhost:8084/auth/token/refresh
        - http://localhost:8084/added-via-plus
        - http://localhost:8084/added-via-extend
        - http://localhost:8084/included_urls/function-1
        - http://localhost:8084/included_urls/function-2
        - http://localhost:8084/different_urls_file_name/function-3
        - http://localhost:8084/different_urls_file_name/function-4
        - http://localhost:8084/rest/viewset
        - http://localhost:8084/rest/custom-model
        - http://localhost:8084/rest/api-view
        - http://localhost:8084/rest-router/view-set
        - http://localhost:8084/rest-router/view-set-on-actions/set_password
        - http://localhost:8084/rest-router/view-set-on-actions/100500/set_password
        - http://localhost:8084/rest-router/view-set-on-actions/set-password-custom-path