# Location Recognition Endpoint

This is only an endpoint for one of the pipeline to optimize Hotel Ranking.  

| Information  | Value                                  |
|--------------|----------------------------------------|
| Docker Image | kaenova/traveloka-location-recognition |
|   Port Open  |                  8001                  |


| Endpoint | Method |           Body Sent (JSON)          |                 Description                |
|:--------:|:------:|:-----------------------------------:|:------------------------------------------:|
|     /    |   GET  |                 None                |            Hello World Endpoint            |
|     /    |  POST  | {"text" : "Hotel in Bali"} | Will Return a List of Detected Location. If nothing detected will return empty array |

Checkout all our pre-trained model through this [link](https://drive.google.com/drive/folders/1oEOPHt71ow5FpPPttQMlDCs4OgZe9oAC?usp=sharing).  

CC22-HO01 ML Teams.