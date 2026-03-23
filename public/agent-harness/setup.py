from setuptools import setup
setup(
    name='cli-anything-public',
    version='1.0.0',
    packages=['cli_anything.public'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-public=cli_anything.public:cli']},
)
