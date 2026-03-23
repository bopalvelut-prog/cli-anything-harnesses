from setuptools import setup
setup(
    name='cli-anything-pravega',
    version='1.0.0',
    packages=['cli_anything.pravega'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-pravega=cli_anything.pravega:cli']},
)
