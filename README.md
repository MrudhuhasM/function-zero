[![Python Application](https://github.com/MrudhuhasM/function-zero/actions/workflows/main.yml/badge.svg)](https://github.com/MrudhuhasM/function-zero/actions/workflows/main.yml)


## Build Container

`docker build .`

## Run conatainer

`docker run -p :8000:8000 imageid`

## Invoke

`invoke.sh`
`curl -X 'POST' \
  'http://0.0.0.0:8000/wiki/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "name": "Mumbai",
  "length": 2
}' `

run `bash invoke.sh`