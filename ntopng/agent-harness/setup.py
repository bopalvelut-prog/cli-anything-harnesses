from setuptools import setup
setup(
    name='cli-anything-ntopng',
    version='1.0.0',
    packages=['cli_anything.ntopng'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-ntopng=cli_anything.ntopng:cli']},
)
