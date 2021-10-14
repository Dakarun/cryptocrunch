# Cryptocrunch
Cryptocrunch pulls cryptocurrency pricing data from APIs and stores them into a database. It (eventually) offers an API
to pull the pricing data from various exchanges and has endpoints which offer statistics such as standard deviation,
largest delta and largest percentage changes. It also offers a web ui to graph the pricing data on a pair level.

## Missing features
* RESTAPI
* UI
* Ranked statistics

## Running cryptocrunch
Cryptocrunch was tested on python 3.8, no guarentees are given for other versions. After cloning the repo to run crypto
follow these steps (I strongly recommend created a virtual enviornment).
```
# Install dependencies
python setup.py install

# Setup db
flask init-db

# Run the application
flask run
```

## Future plans
### Scalability
The current implementation would not scale at all for several reasons. First and foremost the datastore is local to the
process. Taking an AWS heavy approach you could replace the datastore with DynamoDB. Aggregations should be light enough
that they can be handled within the python process and the data has no relational model.

The second problem is that the UI and "backend" are coupled. By moving the data collection and storage components from
the flask app to lambda functions you can only pay for what you use and increase the amount of data collection separate
from servicing users in the UI. Optionally you can also have data aggregation be done by lambda functions, so whatever is hosting the UI only needs to
worry about handling requests and offloads compute elsewhere.

You could put a proxy in front of the webserver and redirect all API requests that hit lambda to an API gateway.

### Testing
Areas that need to be tested
* Data processing
* Handling of API error codes

### Feature requests
#### Push notifications
In order to notify users if there are large changes in pricing it would be nice to send notifications to them. Assuming
that there is a database that contains user information you could request information like phone number/email on sign up
and use those with AWS SNS to send text/email notifications when an alert needs to be triggered. It would be nice if
users could set alert parameters, so for that there would have to be an interface to set the exchange, pair, delta and 
alerting options. Calculating the delta's each time new data is written seems expensive, but perhaps there would be a
way to have a separate rollup table where records have a limited TTL off which this can be calculated.

#### Multiple API Clients
One feature that could be worth adding would be supporting pulling data from multiple sources. It is possible you'd run
out of credit on the current implementation, so by having a set of clients you can pull from you can essentially swap
between them when you see the credit getting too low and put a cooldown on them. You could define a separate lambda per
client, or supply and arg which determines which client is used.
