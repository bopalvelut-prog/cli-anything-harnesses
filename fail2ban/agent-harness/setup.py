from setuptools import setup
setup(
    name='cli-anything-fail2ban',
    version='1.0.0',
    packages=['cli_anything.fail2ban'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-fail2ban=cli_anything.fail2ban:cli']},
)
