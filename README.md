# wsgi

See https://devcenter.heroku.com/articles/buildpacks
```sh
# create a new app
heroku create myapp --buildpack https://github.com/andreif/heroku-buildpack-py.git

# or set for existing
heroku buildpacks:set https://github.com/andreif/heroku-buildpack-py.git -a myapp
```
