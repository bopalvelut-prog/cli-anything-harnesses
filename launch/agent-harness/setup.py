from setuptools import setup
setup(
    name='cli-anything-launch',
    version='1.0.0',
    packages=['cli_anything.launch'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-launch=cli_anything.launch:cli']},
)
