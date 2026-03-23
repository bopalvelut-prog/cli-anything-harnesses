from setuptools import setup
setup(
    name='cli-anything-kid',
    version='1.0.0',
    packages=['cli_anything.kid'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-kid=cli_anything.kid:cli']},
)
