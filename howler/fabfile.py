from fabric.api import local, settings, abort, run, cd, env, prefix
from fabric.contrib.files import sed
from fabric.contrib.console import confirm
import os

env.hosts = ['lukas@10.0.10.180']  # Passphrase private key: hogehoge
env.project_root = '/var/www/howler'
code_dir = '/var/git/lukas-sandbox'
python3_dir = '/home/lukas/.pyenv/versions/howler/bin'


def deploy():
    """[Main] Deploy on server: Git Pull, Bower Install, Serve statics, Disable Debug, Restart app"""
    pull_copy()
    bower_install()
    deploy_static()
    disable_debug_remote()
    inform_webserver()


def pull_copy():
    """Git pull and copy to server place"""
    with cd(code_dir):
        run("git pull")
        run("cp -r /var/git/lukas-sandbox/howler/ /var/www/")


def bower_install():
    """Django bower install"""
    with cd(env.project_root):
        run(os.path.join(python3_dir, 'python') + ' ./manage.py bower install')


def deploy_static():
    """Django collect/deploy static files"""
    with cd(env.project_root):
        run(os.path.join(python3_dir, 'python') + ' ./manage.py collectstatic -v0 --noinput')


def l_deploy_static():
    """[Local] Django collect/deploy static files"""
    with cd(env.project_root):
        local('python ./manage.py collectstatic -v0 --noinput')


def disable_debug_remote():
    """Disable debug mode in settings.py"""
    settings_path = os.path.join(env.project_root, 'howler', 'settings.py')
    sed(settings_path, "DEBUG = True", "DEBUG = False")


def l_genmsg():
    """[Local] Generate .po file locally (gettext required)"""
    # local('pyenv shell howler')
    local('django-admin makemessages -l ja --ignore=components')


def l_compmsg():
    """[Local] Generate .mo file locally (gettext required)"""
    # local('pyenv shell howler')
    local('django-admin compilemessages')


def inform_webserver():
    """trigger restart app (touch wsgi)"""
    with cd(env.project_root):
        run("touch wsgi.py")


def l_test():
    """[Local] Run Tests locally"""
    with settings(warn_only=True):
        result = local('./manage.py test my_app', capture=True)
    if result.failed and not confirm("Tests failed. Continue anyway?"):
        abort("Aborting at user request.")
