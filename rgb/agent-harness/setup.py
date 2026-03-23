from setuptools import setup
setup(
    name='cli-anything-rgb',
    version='1.0.0',
    packages=['cli_anything.rgb'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-rgb=cli_anything.rgb:cli']},
)
