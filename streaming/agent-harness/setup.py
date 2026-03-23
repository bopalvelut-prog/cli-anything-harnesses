from setuptools import setup
setup(
    name='cli-anything-streaming',
    version='1.0.0',
    packages=['cli_anything.streaming'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-streaming=cli_anything.streaming:cli']},
)
