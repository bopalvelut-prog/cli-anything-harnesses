from setuptools import setup
setup(
    name='cli-anything-overlook',
    version='1.0.0',
    packages=['cli_anything.overlook'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-overlook=cli_anything.overlook:cli']},
)
