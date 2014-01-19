from path import path
import os
import doit.tools as dt
from doit.tools import create_folder

top_dir_path = path(os.getcwd())
app_name = 'quickcmd'
app_version = '1.0.0'
app_arch = 'all'

src_dp = path('src')
bin_dp = path('bin')
man_dp = path('man1')
deb_dp = path('deb')

app_fn = app_name
rst_fn = app_name + '.rst'
tgz_fn = app_name + '.1.gz'
deb_ctl_fn = app_name + '.ctl'
deb_fn = app_name + '_' + app_version + '_' + app_arch + '.deb'
deb_rdme_fn = 'README.Debian'

src_fp = src_dp/app_fn
bin_fp = bin_dp/app_fn
rst_fp = man_dp/rst_fn
tgz_fp = man_dp/tgz_fn
deb_ctl_fp = deb_dp/deb_ctl_fn
deb_fp = deb_dp/deb_fn
deb_ctl_fp = deb_dp/deb_ctl_fn
deb_rdme_fp = deb_dp/deb_rdme_fn


def chdir(dir_path='.'):
    top_dir_path.chdir()
    path(dir_path).chdir()

def task_export():
    return {
        'actions': [],
        'file_dep': [],
        'targets': [],
        'clean': True,
        }

def task_install():
    return {
        'actions': ['dpkg -i ' + deb_fp],
        'file_dep': [deb_fp],
        'targets': [],
        }
        
def task_uninstall():
    return {
        'actions': ['apt-get -y remove ' + app_name],
        'file_dep': [],
        'targets': [],
        }

def task_deb():
    return {
        'actions': [(chdir, [deb_dp]),
                    'equivs-build ' + deb_ctl_fn,
                    chdir,
                    'lintian ' + deb_fp],

        'file_dep': [deb_rdme_fp, deb_ctl_fp, tgz_fp, bin_fp],
        'targets': [deb_fp],
        'clean': True,
        'verbosity': 2,
        }

def task_manpage():
    return {
        'actions': ['rst2man ' + rst_fp + ' | gzip -9 - > ' + tgz_fp],
        'file_dep': [rst_fp],
        'targets': [tgz_fp],
        'clean': True,
        }
        
def task_make():
    return {
        'actions': [(create_folder, [bin_dp]),
                    'cp ' + src_fp + ' ' + bin_fp],
        'file_dep': [],
        'targets': [bin_fp, bin_dp],
        'clean': True,
        }

def task_dodo():
    return {
        'actions': [],
        'targets': ['dodo.pyc'],
        'clean': True,
        }



