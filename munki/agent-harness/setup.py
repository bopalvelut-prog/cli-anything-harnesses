from setuptools import setup
setup(
    name='cli-anything-munki',
    version='1.0.0',
    packages=['cli_anything.munki'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-munki=cli_anything.munki:cli']},
)
