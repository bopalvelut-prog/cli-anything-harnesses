from setuptools import setup
setup(
    name='cli-anything-react_router',
    version='1.0.0',
    packages=['cli_anything.react_router'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-react_router=cli_anything.react_router:cli']},
)
