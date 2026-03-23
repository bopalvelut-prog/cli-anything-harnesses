from setuptools import setup
setup(
    name='cli-anything-kiwi',
    version='1.0.0',
    packages=['cli_anything.kiwi'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-kiwi=cli_anything.kiwi:cli']},
)
