from setuptools import setup
setup(
    name='cli-anything-easyeffects',
    version='1.0.0',
    packages=['cli_anything.easyeffects'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-easyeffects=cli_anything.easyeffects:cli']},
)
