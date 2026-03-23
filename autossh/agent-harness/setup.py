from setuptools import setup
setup(
    name='cli-anything-autossh',
    version='1.0.0',
    packages=['cli_anything.autossh'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-autossh=cli_anything.autossh:cli']},
)
