from setuptools import setup
setup(
    name='cli-anything-thirdweb',
    version='1.0.0',
    packages=['cli_anything.thirdweb'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-thirdweb=cli_anything.thirdweb:cli']},
)
