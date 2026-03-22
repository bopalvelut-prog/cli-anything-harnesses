from setuptools import setup
setup(
    name='cli-anything-django',
    version='1.0.0',
    packages=['cli_anything.django'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-django=cli_anything.django:cli']},
)
