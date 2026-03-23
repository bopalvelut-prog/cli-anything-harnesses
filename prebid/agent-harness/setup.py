from setuptools import setup
setup(
    name='cli-anything-prebid',
    version='1.0.0',
    packages=['cli_anything.prebid'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-prebid=cli_anything.prebid:cli']},
)
