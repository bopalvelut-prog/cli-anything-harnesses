from setuptools import setup
setup(
    name='cli-anything-route',
    version='1.0.0',
    packages=['cli_anything.route'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-route=cli_anything.route:cli']},
)
