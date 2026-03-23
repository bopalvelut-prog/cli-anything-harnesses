from setuptools import setup
setup(
    name='cli-anything-stop',
    version='1.0.0',
    packages=['cli_anything.stop'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-stop=cli_anything.stop:cli']},
)
