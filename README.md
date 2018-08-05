##Create account on the Dark Side app.
Link: https://darksky.net/dev/register

Generate to API key to fetch data

$export DARK_SKY_KEY={your Dark Sky API Key}

$python ezw_app.py  

## Docker deployment
$docker build -t ezw .

$docker run -d --name ezcon -p 8081:5000 -e DARK_SKY_KEY={your Dark Sky API Key} weatherApp:v01

##Push image to the docker hub.

First set ur docker credentials over the system

$docker login --username username --password password

$docker tag my-image username/my-repo

$docker push username/my-repo
