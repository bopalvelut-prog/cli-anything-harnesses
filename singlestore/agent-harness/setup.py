from setuptools import setup
setup(
    name='cli-anything-singlestore',
    version='1.0.0',
    packages=['cli_anything.singlestore'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-singlestore=cli_anything.singlestore:cli']},
)
