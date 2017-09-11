Kubernetes 101
==============

This directory contains a series of examples used for a small introduction to
kubernetes presentation. They demonstrate basic Kubernetes concepts including:

1. Pods
2. ReplicaSets
3. Deployments
4. Services
5. Routes/Ingress
6. Probes
6. Volumes, Persistent Volumes, and Persistent Volume Claims

Also provided is a basic, no doubt terribly written, application. The
application includes:

1. A basic python HTTP server as a "frontend" that serves up HTML.
2. A basic python HTTP server as a "backend" that serves up images of cats.

The separation between the two is intentionally arbitrary but serves the person
of demonstrating a common pattern where an application may be made up of one or
more front end services and a backend intentionally inaccessible to consumers of
the application.

Pre-requisites
==============

Docker
------

You will need Docker locally if you want to build/push the example application
containers. You can however skip this and just use the prebuilt images from
Docker Hub as the focus of the material is on using Kubernetes, not building
Docker images.

Minishift/Minikube
------------------

You will need a Kubernetes installation, the easiest way to obtain one for
local development purposes is to install and use Minishift or Minikube.

Kubectl/oc
----------

As part of the Minishift or Minikube installation you should be directed to
install kubectl or oc. This is required to interact with your Kubernetes
deployment and use the examples.

Examples
========

001-hello-catz-httpd-pod.yaml
-----------------------------

Deploy the **python-imaged** HTTPD server in a single Kubernetes Pod labelled
with **app: hello-catz** and **service: httpd**. This uses v1 of the application
which simply prints "Helloworld!".

002-hello-catz-httpd-service.yaml
---------------------------------

Define a Kubernetes Service of type **NodePort** to facilitate demonstrating connectivity
so that we can show the service is really operational. The services accepts
inbound traffic on the HTTP port (80) and directs it to pods labelled **app:
hello-catz** and **service-httpd**.

003-hello-catz-route.yaml
-------------------------

004-hello-catz-httpd-config.yaml
--------------------------------

Define a Kubernetes ConfigMap. We will use this to tell our application the name
of the imaged service. The application will use this name for DNS lookups to
access images.

005-hello-catz-httpd-deployment.yaml
------------------------------------

Thus far we have been using a single pod to define and deploy the application.
This example defines a Kubernetes Deployment and can be used to demonstrate
scaling up/down the underlying ReplicaSet as well as rolling out a new version
of the app (v2, and ultimately v3).

006-hello-catz-httpd-liveness-probe.yaml
----------------------------------------

007-hello-catz-imaged-deployment.yaml
-------------------------------------

008-hello-catz-imaged-service.yaml
----------------------------------

009-hello-catz-volume.yaml
--------------------------

010-hello-catz-peristent-volume-claim.yaml
------------------------------------------

011-hello-catz-imaged-deployment.yaml
-------------------------------------
