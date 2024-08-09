# Key-Value Store HTTP API Service

This is a simple Django-based in-memory key-value store HTTP API service. The service allows users to set key-value pairs, retrieve them, and search for keys using prefix and suffix filters. The application has been containerized using Docker and deployed on a Kubernetes cluster.

## Features

- **Set Key-Value Pair:** Add a key-value pair to the store via a POST request.
- **Get Value by Key:** Retrieve the value associated with a specific key via a GET request.
- **Search Keys:** Search for keys based on prefix and suffix.

## API Endpoints

### 1. Set Key-Value Pair

- **Endpoint:** `/set`
- **Method:** POST
- **Description:** Sets a key-value pair in the store.

**Example Request:**

### Example Bash Command

To set a key-value pair, use the following command:


curl -X POST http://<your-domain-or-ip>/set -H "Content-Type: application/json" -d '{"key":"exampleKey", "value":"exampleValue"}'



 ### 2. Get Value by Key

   - **Endpoint: /get/<key>
   - **Method: GET
   -** Description: Retrieves the value associated with the specified key.

Example Request
  - ** curl http://127.0.0.1:8000/get/abc


### 3. Search Keys by Prefix or Suffix

  - ** Endpoint: /search
  - **Method: GET
  - **Description: Searches for keys using prefix and/or suffix filters.

Example Request (Prefix Search):
- ** curl "http://<your-domain-or-ip>/search?prefix=abc"


-** Response
{
    "keys": ["abc-1", "abc-2"]
}

### Docker setup 
clone repo : git clone -b master https://github.com/shivakumarvardhamana/HTTP-API-Service.git
cd HTTP-API-Service

- ** build the image
     docker build -t shiva2720/http-server-1 .
- ** run as docker container
  docker run -p 8000:8000 shiva2720/http-server-1
-** push image
   docker push shiva2720/http-server-1

### Kubernetes
in the Manifests folder i written deployment and service yaml to run application as pod
created cluster with kubeadm and ran the manifest file deployment and service and tested below scenarios like 
   - **curl <load-balancer>/get/abc-1
   - **curl <loadbalancer>/search?prefix=abc
   - **curl -X POST http://<loadbalancer>/set -H "Content-Type: application/json" -d '{"key":"exampleKey", "value":"exampleValue"}'

it's working as expected
 
