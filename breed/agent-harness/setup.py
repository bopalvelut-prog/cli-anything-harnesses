from setuptools import setup
setup(
    name='cli-anything-breed',
    version='1.0.0',
    packages=['cli_anything.breed'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-breed=cli_anything.breed:cli']},
)
