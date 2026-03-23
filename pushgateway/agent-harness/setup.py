from setuptools import setup
setup(
    name='cli-anything-pushgateway',
    version='1.0.0',
    packages=['cli_anything.pushgateway'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-pushgateway=cli_anything.pushgateway:cli']},
)
