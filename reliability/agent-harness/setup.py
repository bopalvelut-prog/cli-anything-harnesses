from setuptools import setup
setup(
    name='cli-anything-reliability',
    version='1.0.0',
    packages=['cli_anything.reliability'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-reliability=cli_anything.reliability:cli']},
)
