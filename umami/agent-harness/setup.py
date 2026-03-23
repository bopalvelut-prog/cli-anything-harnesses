from setuptools import setup
setup(
    name='cli-anything-umami',
    version='1.0.0',
    packages=['cli_anything.umami'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-umami=cli_anything.umami:cli']},
)
