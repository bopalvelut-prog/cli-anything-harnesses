from setuptools import setup
setup(
    name='cli-anything-dovecot',
    version='1.0.0',
    packages=['cli_anything.dovecot'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-dovecot=cli_anything.dovecot:cli']},
)
