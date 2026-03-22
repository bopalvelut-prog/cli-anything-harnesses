from setuptools import setup
setup(
    name='cli-anything-vercel',
    version='1.0.0',
    packages=['cli_anything.vercel'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-vercel=cli_anything.vercel:cli']},
)
