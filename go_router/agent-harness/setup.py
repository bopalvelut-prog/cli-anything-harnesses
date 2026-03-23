from setuptools import setup
setup(
    name='cli-anything-go_router',
    version='1.0.0',
    packages=['cli_anything.go_router'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-go_router=cli_anything.go_router:cli']},
)
