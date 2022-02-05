
## Installing

1. Install dependencies

```
npm i && cd client && npm i && cd ..
```

2. Create variables.env file and replace values with yours

```
NODE_ENV=development
DATABASE="Mongodb Connection String"
JWT_KEY="secretkey"
EMAILUSER="example@gmail.com"
EMAILPASS="example"
HOST="your ip eg. http://192.168.0.14:5000"
ENABLE_SEND_EMAIL="true or false" // false if you don't want to set it up
TEST_DATABASE="testing db"
```

3. Go into `client/src/_services/socketService.js` and replace

```
window.location.hostname
```

with your local IP address on port 5000 eg.

```
192.168.0.14:5000
```

4. Run project

```
npm run dev
```

## Contribute

Show your support by ⭐ the project.
