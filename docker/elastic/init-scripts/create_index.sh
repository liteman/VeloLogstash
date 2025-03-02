#!/bin/bash

# Wait until Elasticsearch is up and running
until curl -s http://elasticsearch:9200 > /dev/null; do
  echo "Waiting for Elasticsearch to start..."
  sleep 5
done

# Create the index with the specified mapping
curl -X PUT "http://elasticsearch:9200/velocirpator-pipe" -H 'Content-Type: application/json' -d'
{
  "mappings": {
    "properties": {
      "EventTime": {
        "type": "date"
      },
      "otherField1": {
        "type": "keyword"
      },
      "otherField2": {
        "type": "text"
      }
    }
  }
}
'

echo "Index 'velocirpator-pipe' created successfully with EventTime as the timestamp field."
