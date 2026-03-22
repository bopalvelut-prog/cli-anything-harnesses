from setuptools import setup
setup(
    name='cli-anything-nextjs',
    version='1.0.0',
    packages=['cli_anything.nextjs'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-nextjs=cli_anything.nextjs:cli']},
)
