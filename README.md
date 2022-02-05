# Redsift Python Engineering Test

## Goal

The purpose of this test is twofold in that it provides an example of the kind of tasks and tech stack this role involves, while assessing your thought process, technical capabilities and where your strengths might be. The expected time to be spent on the task is approximately 2 - 3 hours.

The things that we are looking to assess are:

- Decision making and project architecture
- Clean, maintainable code that is secure and scales well
- Experience building scalable projects using Python
- An understanding of data structures, algorithms and how databases work

Please provide some documentation about your thought process, an explanation of the decisions made, what you found challenging, and what futher considerations and improvements you would make if this was a 'real world' project that was going to be deployed into a high volume production environment.

Do not stress if you are unable to finish the entire task. If you're unable to complete some component, the most important thing is that you document what your approach was, what you tried, and what you would do further if provided more time.

## Task

> The expected time for this task is 2 to 3 hours. This isn't a lot of time, so focus on what you can achieve during this time to create a MVP solution and document the aspects that would need to be implemented at a later stage.

The specifications of this tech stack are as follows:

- Framework: Flask or FastAPI or Django
- Databases: MongoDB

The primary goal of the task is to test your experience with multi-threading on Python. Please focus on how you could make the request execute as quickly as you possibly can. The solution should be scalable and robust. Document any scaling considerations that you've addressed and what, if anything, would need to be implemented at a later stage.

1. Create a backend service and implement the following API:

- takes in a POST request containing a list of domains
- For each domain in the list, download the index file and extract the title of the page
- Return the titles as an array to the response of the API request
- Cap the execution time of the request to 10 seconds

2. Update the API that you have created to keep track of how many times it is invoked and the average response time of the API. Create an API that returns these stats.
