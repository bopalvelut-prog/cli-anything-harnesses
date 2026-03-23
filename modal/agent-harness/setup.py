from setuptools import setup
setup(
    name='cli-anything-modal',
    version='1.0.0',
    packages=['cli_anything.modal'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-modal=cli_anything.modal:cli']},
)
