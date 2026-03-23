from setuptools import setup
setup(
    name='cli-anything-consumer',
    version='1.0.0',
    packages=['cli_anything.consumer'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-consumer=cli_anything.consumer:cli']},
)
