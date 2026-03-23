from setuptools import setup
setup(
    name='cli-anything-create_react_app',
    version='1.0.0',
    packages=['cli_anything.create_react_app'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-create_react_app=cli_anything.create_react_app:cli']},
)
