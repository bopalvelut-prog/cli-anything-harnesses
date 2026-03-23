from setuptools import setup
setup(
    name='cli-anything-apisix',
    version='1.0.0',
    packages=['cli_anything.apisix'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-apisix=cli_anything.apisix:cli']},
)
