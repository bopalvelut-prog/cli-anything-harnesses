from setuptools import setup
setup(
    name='cli-anything-amplify',
    version='1.0.0',
    packages=['cli_anything.amplify'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-amplify=cli_anything.amplify:cli']},
)
