from setuptools import setup
setup(
    name='cli-anything-icingaweb2',
    version='1.0.0',
    packages=['cli_anything.icingaweb2'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-icingaweb2=cli_anything.icingaweb2:cli']},
)
