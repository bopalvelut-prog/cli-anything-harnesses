from setuptools import setup
setup(
    name='cli-anything-flask',
    version='1.0.0',
    packages=['cli_anything.flask'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-flask=cli_anything.flask:cli']},
)
