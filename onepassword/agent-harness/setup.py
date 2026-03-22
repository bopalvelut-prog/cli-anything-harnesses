from setuptools import setup
setup(
    name='cli-anything-onepassword',
    version='1.0.0',
    packages=['cli_anything.onepassword'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-onepassword=cli_anything.onepassword:cli']},
)
