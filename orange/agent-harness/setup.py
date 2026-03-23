from setuptools import setup
setup(
    name='cli-anything-orange',
    version='1.0.0',
    packages=['cli_anything.orange'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-orange=cli_anything.orange:cli']},
)
