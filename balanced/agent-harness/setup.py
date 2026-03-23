from setuptools import setup
setup(
    name='cli-anything-balanced',
    version='1.0.0',
    packages=['cli_anything.balanced'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-balanced=cli_anything.balanced:cli']},
)
