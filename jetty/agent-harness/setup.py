from setuptools import setup
setup(
    name='cli-anything-jetty',
    version='1.0.0',
    packages=['cli_anything.jetty'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-jetty=cli_anything.jetty:cli']},
)
