from setuptools import setup
setup(
    name='cli-anything-gson',
    version='1.0.0',
    packages=['cli_anything.gson'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-gson=cli_anything.gson:cli']},
)
