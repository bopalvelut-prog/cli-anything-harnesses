from setuptools import setup
setup(
    name='cli-anything-wav',
    version='1.0.0',
    packages=['cli_anything.wav'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-wav=cli_anything.wav:cli']},
)
