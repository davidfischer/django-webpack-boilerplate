# Django Webpack Boilerplate

A sample Django project that uses Webpack to manage and bundle static assets.


## Prerequisites

* Node & NPM
* Python 2.7 or 3.6 (with Pip)


## Dependencies

    % npm install
    % pip install -r requirements.txt


## Running

    % npm run build
    % ./manage.py runserver

    # Open in your browser
    % open "http://localhost:8000"


## Why?

There are a number of advantages to using something to manage and bundle static
assets. 

* **minification** (smaller JS/CSS files) results in faster downloads and faster parsing of your static files
* **file combining** (combining multiple JS/CSS files) results in faster downloads although this is less of an advantage with HTTP2
* **dependency management** - rather than copying bootstrap or jquery into your source tree, there's simply an entry in `package.json`
* **caching** - having few static asset bundles with unique hashes allows setting very long expiry headers which results in faster sites
