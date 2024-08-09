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

```bash
curl -X POST http://<your-domain-or-ip>/set -H "Content-Type: application/json" -d '{"key":"exampleKey", "value":"exampleValue"}'


2. Get Value by Key

    Endpoint: /get/<key>
    Method: GET
    Description: Retrieves the value associated with the specified key.

Example Request:
