# Number-Classification-API
# Number Classification API

The Number Classification API is a RESTful service that accepts a number as input and returns various mathematical properties of that number along with a fun fact fetched from an external API.

## Table of Contents

- [Overview](#overview)
- [Endpoint](#endpoint)
- [Request Parameters](#request-parameters)
- [Response Formats](#response-formats)
- [Successful Response (200 OK)](#successful-response-200-ok)
- [Error Response (400 Bad Request)](#error-response-400-bad-request)
- [Examples](#examples)
- [Getting Started Locally](#getting-started-locally)
- [Deployment](#deployment)
- [Additional Information](#additional-information)

## Overview

This API accepts GET requests with a query parameter `number` and returns a JSON response containing:
- The number provided.
- Whether the number is prime.
- Whether the number is perfect.
- A list of properties (e.g., `armstrong` and `odd` or `even`).
- The sum of its digits.
- A fun fact about the number retrieved from [Numbers API](http://numbersapi.com/).

## Endpoint


## Example on how to use the endpoint , 'replace the number 371 with any other number'
https://mysite-pwjz.onrender.com/api/classify-number?number=371
