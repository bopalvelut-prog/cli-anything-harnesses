from setuptools import setup
setup(
    name='cli-anything-spideroak',
    version='1.0.0',
    packages=['cli_anything.spideroak'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-spideroak=cli_anything.spideroak:cli']},
)
