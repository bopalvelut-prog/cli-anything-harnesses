from setuptools import setup
setup(
    name='cli-anything-google_chat',
    version='1.0.0',
    packages=['cli_anything.google_chat'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-google_chat=cli_anything.google_chat:cli']},
)
