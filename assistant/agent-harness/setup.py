from setuptools import setup
setup(
    name='cli-anything-assistant',
    version='1.0.0',
    packages=['cli_anything.assistant'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-assistant=cli_anything.assistant:cli']},
)
