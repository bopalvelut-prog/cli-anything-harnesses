from setuptools import setup
setup(
    name='cli-anything-licensor',
    version='1.0.0',
    packages=['cli_anything.licensor'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-licensor=cli_anything.licensor:cli']},
)
