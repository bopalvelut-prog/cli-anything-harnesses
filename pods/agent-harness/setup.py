from setuptools import setup
setup(
    name='cli-anything-pods',
    version='1.0.0',
    packages=['cli_anything.pods'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-pods=cli_anything.pods:cli']},
)
