from setuptools import setup
setup(
    name='cli-anything-zeppelin',
    version='1.0.0',
    packages=['cli_anything.zeppelin'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-zeppelin=cli_anything.zeppelin:cli']},
)
