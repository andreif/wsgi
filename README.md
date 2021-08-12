# wsgi

Live https://wsgi2.herokuapp.com

```sh
# create a new app
heroku create myapp --buildpack https://github.com/andreif/wsgi.git

# or set for existing
heroku buildpacks:set https://github.com/andreif/wsgi.git -a myapp
```
See https://devcenter.heroku.com/articles/buildpacks#using-a-third-party-buildpack
