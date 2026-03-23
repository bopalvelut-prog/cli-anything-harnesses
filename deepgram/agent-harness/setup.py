from setuptools import setup
setup(
    name='cli-anything-deepgram',
    version='1.0.0',
    packages=['cli_anything.deepgram'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-deepgram=cli_anything.deepgram:cli']},
)
