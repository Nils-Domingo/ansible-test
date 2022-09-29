# ansible-test

## First install

Ubuntu 20.04
```bash
sudo apt install -y python3-venv virtualbox virtualbox-dkms virtualbox-ext-pack vagrant
./bin/init.sh
```

MacOS
```bash
brew install python3
brew install virtualbox
brew install vagrant
./bin/init.sh
```

## day to day
```bash
# activate python virtual env
source venv/bin/activate

# test playbook
cd playbook
molecule converge -- --diff
molecule verify
molecule lint
curl localhost:40080

# log into the VM
molecule login

# cleanup
molecule destroy
```



## Intro
For now, we have a basic Caddy server running, with default ```/etc/caddy/Caddyfile``` content.

We want our ansible to be able to customize the ```/etc/caddy/Caddyfile``` file.


## Step1: static answer

* Add task ```playbook/roles/caddy/tasks/config.yml``` in caddy role to setup /etc/caddy/Caddyfile content to:
```
:80 {
        respond "Hello, I'm John!"
}
```

* Be sure caddy is reloaded when /etc/caddy/Caddyfile is changed

* Check curl http://localhost:40080 return "Hello, I'm John!"

* Create a Pull Request with this change

## Step2: Improve step1 by using an ansible var

We want Ansible to configure the Caddy config file ```/etc/caddy/Caddyfile```, so the server will return "Hello, I'm Jane!"

* Add a var in caddy role
    * name: ```caddy_who```
    * default value: "John"

* Configure ```caddy_who``` in playbook/group_vars/all.yml to value "Jane"

* Use this ```caddy_who``` var to update /etc/caddy/Caddyfile so result
of curl http://localhost:40080 **now** return "Hello, I'm Jane!"

* Create a **another** Pull Request with this change

## Doc
https://caddyserver.com/docs/caddyfile/directives/respond
https://caddyserver.com/docs/getting-started#reloading-config
