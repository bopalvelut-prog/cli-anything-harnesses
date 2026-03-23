from setuptools import setup
setup(
    name='cli-anything-hivemq',
    version='1.0.0',
    packages=['cli_anything.hivemq'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-hivemq=cli_anything.hivemq:cli']},
)
