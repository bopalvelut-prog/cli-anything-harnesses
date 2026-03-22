from setuptools import setup
setup(
    name='cli-anything-wemix',
    version='1.0.0',
    packages=['cli_anything.wemix'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-wemix=cli_anything.wemix:cli']},
)
