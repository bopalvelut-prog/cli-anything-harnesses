from setuptools import setup
setup(
    name='cli-anything-remoting',
    version='1.0.0',
    packages=['cli_anything.remoting'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-remoting=cli_anything.remoting:cli']},
)
