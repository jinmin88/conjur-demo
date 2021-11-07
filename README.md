# conjur-demo
demo the conjur server

## Pre-requiresite
```bash
# 1. install docker-compose
pip install docker-compose

# 2. pull cyberark conjur quick-start images
docker-compose pull

# 3. Create db folder for storing persistent state.
mkdir db

# 4. The data key will be used later to encrypt the database. In the working directory, generate the key and store it to a file
docker-compose run --no-deps --rm conjur data-key generate > data_key

# 5. load data_key file content as an environment variable
export CONJUR_DATA_KEY="$(< data_key)"

# 6. Start the Conjur Open Source environment
docker-compose up -d

# 7. Create a conjur account and initialize the built-in admin user.
docker-compose exec conjur conjurctl account create myorg > myorg_data

# 8. Initialize account (one-time action)
docker-compose exec client conjur init -u conjur -a myorg
```
## install 
