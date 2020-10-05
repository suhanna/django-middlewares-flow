# django-middlewares-flow
Sample django project to identify the middleware methods and their flow in request/response process flow.

## What are middlewares
* It is a python class hook in django's request response life cycle.
* Django inself create a set of middlewares when we create a django project with command
  > django-admin startproject my_project
* **ORDER** is very imported for middlewares, It works as a layers wrapped one over another.
* ie, when request came from browser to view, it will come through all middlewares as top to bottom and when it return back as response from view to browser it will go through middlewares in bottom to top order.

## Middleware methods to call on request/response cycle 
    * Called during request:
        1. process_request(request)
        2. process_view(request, view_func, view_args, view_kwargs)
    * Called during response:
        1. process_exception(request, exception) (only if the view raised an exception)
        2. process_template_response(request, response) (only for template responses)
        3. process_response(request, response)
        
## Workflow of middlewares
* Eventhough there are a total of five middleware methods in request/response cycle, It is difficult to find the order of their execution from some of the existing middleware docs.
* Hence I have done this project to find the work flow of each methods when the request came to view, and return back from the view. Hope it will be helpful for some of you.
* django-middlewares-flow contains two custom middlewares as below
  - FirstMiddleware
    > With methods process_request, process_view and process_response
  - SecondMiddleware
    > With methods process_request, process_view and process_response

## How to interactwith django-middlewares-flow
1. Download django-middlewares-flow
2. Open terminal
3. Create and activate a virtual env for django-middlewares-flow using python3
4. Install django using pip, with command `pip install django==2.2`
5. Run project with command `python manage.py runserver`
6. open http://localhost:8000 in browser
7. Check terminal

## Your terminal output will be like below,
    System check identified no issues (0 silenced).
    September 29, 2020 - 05:52:21
    Django version 2.2, using settings 'django_middleware.settings'
    Starting development server at http://127.0.0.1:8000/
    Quit the server with CONTROL-C.
    ----- process request M1 -----
    ----- process request M2 -----
    ----- process view M1 -----
    ----- Middleware view name : home   M1-----
    ----- process view M2 -----
    ----- Middleware view name : home   M2-----
    ----- Reached View -----
    ----- process response M2 -----
    ----- process response M1 -----
    [29/Sep/2020 05:52:23] "GET / HTTP/1.1" 200 20
    
## Conclusion
* Middleware mthods will execute in the order of 
   1. Execute process_request from top to bottom, 
   2. Execute process_view from top to bottom
   3. Execute process_response from bottom to top
