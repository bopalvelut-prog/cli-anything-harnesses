from setuptools import setup
setup(
    name='cli-anything-messagebird',
    version='1.0.0',
    packages=['cli_anything.messagebird'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-messagebird=cli_anything.messagebird:cli']},
)
