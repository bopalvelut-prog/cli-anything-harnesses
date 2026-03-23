from setuptools import setup
setup(
    name='cli-anything-amazon_robomaker',
    version='1.0.0',
    packages=['cli_anything.amazon_robomaker'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-amazon_robomaker=cli_anything.amazon_robomaker:cli']},
)
