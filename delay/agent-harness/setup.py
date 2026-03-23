from setuptools import setup
setup(
    name='cli-anything-delay',
    version='1.0.0',
    packages=['cli_anything.delay'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-delay=cli_anything.delay:cli']},
)
