from setuptools import setup
setup(
    name='cli-anything-pepper',
    version='1.0.0',
    packages=['cli_anything.pepper'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-pepper=cli_anything.pepper:cli']},
)
