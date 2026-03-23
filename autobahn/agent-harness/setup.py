from setuptools import setup
setup(
    name='cli-anything-autobahn',
    version='1.0.0',
    packages=['cli_anything.autobahn'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-autobahn=cli_anything.autobahn:cli']},
)
