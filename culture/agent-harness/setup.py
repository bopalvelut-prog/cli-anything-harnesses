from setuptools import setup
setup(
    name='cli-anything-culture',
    version='1.0.0',
    packages=['cli_anything.culture'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-culture=cli_anything.culture:cli']},
)
