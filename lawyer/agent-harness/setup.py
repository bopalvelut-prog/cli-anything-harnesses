from setuptools import setup
setup(
    name='cli-anything-lawyer',
    version='1.0.0',
    packages=['cli_anything.lawyer'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-lawyer=cli_anything.lawyer:cli']},
)
