from setuptools import setup
setup(
    name='cli-anything-ohmyzsh',
    version='1.0.0',
    packages=['cli_anything.ohmyzsh'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-ohmyzsh=cli_anything.ohmyzsh:cli']},
)
