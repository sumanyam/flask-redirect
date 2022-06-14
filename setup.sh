#!/bin/bash
oc delete deploy flask-redirect
oc new-app --docker-image=quay.io/cpranava0/flask-redirect:main
oc set env deploy/flask-redirect BASE_URL=redhat.com
oc set env deploy/flash-redirect 
oc expose svc flask-redirect
