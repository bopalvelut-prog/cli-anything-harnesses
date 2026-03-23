from setuptools import setup
setup(
    name='cli-anything-baget',
    version='1.0.0',
    packages=['cli_anything.baget'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-baget=cli_anything.baget:cli']},
)
