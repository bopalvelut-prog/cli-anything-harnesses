from setuptools import setup
setup(
    name='cli-anything-restaurant',
    version='1.0.0',
    packages=['cli_anything.restaurant'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-restaurant=cli_anything.restaurant:cli']},
)
