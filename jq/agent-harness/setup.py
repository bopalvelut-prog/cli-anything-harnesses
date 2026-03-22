from setuptools import setup
setup(
    name='cli-anything-jq',
    version='1.0.0',
    packages=['cli_anything.jq'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-jq=cli_anything.jq:cli']},
)
