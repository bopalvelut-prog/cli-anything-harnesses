from setuptools import setup
setup(
    name='cli-anything-paint',
    version='1.0.0',
    packages=['cli_anything.paint'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-paint=cli_anything.paint:cli']},
)
