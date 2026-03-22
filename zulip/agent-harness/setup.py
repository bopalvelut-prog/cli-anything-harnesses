from setuptools import setup
setup(
    name='cli-anything-zulip',
    version='1.0.0',
    packages=['cli_anything.zulip'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-zulip=cli_anything.zulip:cli']},
)
