from setuptools import setup
setup(
    name='cli-anything-amazonec2',
    version='1.0.0',
    packages=['cli_anything.amazonec2'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-amazonec2=cli_anything.amazonec2:cli']},
)
