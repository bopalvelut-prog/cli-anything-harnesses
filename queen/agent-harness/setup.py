from setuptools import setup
setup(
    name='cli-anything-queen',
    version='1.0.0',
    packages=['cli_anything.queen'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-queen=cli_anything.queen:cli']},
)
