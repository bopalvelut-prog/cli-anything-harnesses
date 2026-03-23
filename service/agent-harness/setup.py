from setuptools import setup
setup(
    name='cli-anything-service',
    version='1.0.0',
    packages=['cli_anything.service'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-service=cli_anything.service:cli']},
)
