from setuptools import setup
setup(
    name='cli-anything-telephone',
    version='1.0.0',
    packages=['cli_anything.telephone'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-telephone=cli_anything.telephone:cli']},
)
