from setuptools import setup
setup(
    name='cli-anything-agent',
    version='1.0.0',
    packages=['cli_anything.agent'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-agent=cli_anything.agent:cli']},
)
