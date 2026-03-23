from setuptools import setup
setup(
    name='cli-anything-pjsua',
    version='1.0.0',
    packages=['cli_anything.pjsua'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-pjsua=cli_anything.pjsua:cli']},
)
