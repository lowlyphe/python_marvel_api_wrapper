# How to use

# Prerequisites

- Navigate to the [Marvel Developer Portal](https://developer.marvel.com/)
- Create a developer account
- Obtain your personal public and private API keys

# Installation

            import Marvel from Marvel

# Main Usage

            instance = Marvel(YOUR_PUBLIC_KEY, YOUR_PRIVATE_KEY)
            # keys must be in correct order for api authentication to work
            print(instance.get_info())
            # the get info method runs the API call with all of the set options

# Main functions

## Set main endpoint

            instance.set_endpoint('endpoint[string]')

API Example: https://gateway.marvel.com/v1/public/'endpoint'

Endpoint options:

- characters - Fetches list of characters
- comics - Fetches list of comics
- creators - Fetches list of creators
- events - Fetches list of events
- series - Fetches list of series
- stories - Fetches list of stories

## Set Endpoint ID

Search for a particular 'endpoint' by id

            instance.set_id(id[int])

API example: https://gateway.marvel.com/v1/public/'endpoint'/'character/'id'
Fetches a list of (endpoint) filtered by id

## Set Sub Endpoint

Set a sub endpoint landing url under the desired endpoint. Character id must be set to use sub endpoint.

            instance.set_sub_endpoint('sub_endpoint[string]')

API example: https://gateway.marvel.com/v1/public/'endpoint'/'sub_endpoint'

Sub endpoint options:

- characters
  - comics - Fetches lists of comics filtered by a character id.
  - events - Fetches lists of events filtered by a character id
  - series - Fetches lists of series filtered by a character id
  - stories - Fetches lists of stories filtered by a character id.
- comics
  - characters - Fetches lists of characters filtered by a comic id
  - creators - Fetches lists of creators filtered by a comic id
  - events - Fetches lists of events filtered by a comic id
  - stories - Fetches lists of stories filtered by a comic id
- creators
  - comics - Fetches lists of comics filtered by a creator id
  - events - Fetches lists of events filtered by a creator id
  - series - Fetches lists of series filtered by a creator id
  - stories - Fetches lists of stories filtered by a creator id
- events
  - characters - Fetches lists of characters filtered by an event id
  - comics - Fetches lists of comics filtered by an event id
  - creators - Fetches lists of creators filtered by an event id
  - series - Fetches lists of series filtered by an event id
  - stories - Fetches lists of stories filtered by an event id
- series
  - characters - Fetches lists of characters filtered by a series id
  - comics - Fetches lists of comics filtered by a series id
  - creators - Fetches lists of creators filtered by a series id
  - events - Fetches lists of events filtered by a series id
  - stories - Fetches lists of stories filtered by a series id
- stories
  - characters - Fetches lists of characters filtered by a story id
  - comics - Fetches lists of comics filtered by a story id
  - creators - Fetches lists of creators filtered by a story id
  - events - Fetches lists of events filtered by a story id
  - series - Fetches lists of series filtered by a story id

## Modifiers

Modifiers may be used to modify the returned result by passing in optional parameters to the API call

- Modifiers may be used with any endpoint, id, and sub endpoint.

Code example with modifiers

            instance.set_modifier(modifier_name[string], modifier_value[string])
            instance.set_modifier('name', 'iron man')

- If a modifier is not correct, or the API does not support that combination of modifiers, printing the Marvel object will return the status code and message.

      instance.set_endpoint('comics')
      instance.set_modifier('name', 'storm')
      print(instance.get_info())
      # returns: {'code': 404, 'status': "We couldn't find that comic_issue"}

      instance.set_endpoint('comics')
      instance.set_modifier('title', 'storm')
      print(instance.get_info())
      # returns [{'id': 3627, 'digitalId': 0, 'title': 'Storm (2006)'...}]

For more information on all available modifiers visit the [Marvel API Documentation](https://developer.marvel.com/docs)
