from setuptools import setup
setup(
    name='cli-anything-peace',
    version='1.0.0',
    packages=['cli_anything.peace'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-peace=cli_anything.peace:cli']},
)
