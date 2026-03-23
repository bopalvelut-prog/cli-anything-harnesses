from setuptools import setup
setup(
    name='cli-anything-tonight',
    version='1.0.0',
    packages=['cli_anything.tonight'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-tonight=cli_anything.tonight:cli']},
)
