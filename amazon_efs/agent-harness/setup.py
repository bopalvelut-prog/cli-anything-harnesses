from setuptools import setup
setup(
    name='cli-anything-amazon_efs',
    version='1.0.0',
    packages=['cli_anything.amazon_efs'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-amazon_efs=cli_anything.amazon_efs:cli']},
)
