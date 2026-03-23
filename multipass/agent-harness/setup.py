from setuptools import setup
setup(
    name='cli-anything-multipass',
    version='1.0.0',
    packages=['cli_anything.multipass'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-multipass=cli_anything.multipass:cli']},
)
