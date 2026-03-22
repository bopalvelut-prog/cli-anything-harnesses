from setuptools import setup
setup(
    name='cli-anything-rspamd',
    version='1.0.0',
    packages=['cli_anything.rspamd'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-rspamd=cli_anything.rspamd:cli']},
)
