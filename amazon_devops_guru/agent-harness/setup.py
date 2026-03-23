from setuptools import setup
setup(
    name='cli-anything-amazon_devops_guru',
    version='1.0.0',
    packages=['cli_anything.amazon_devops_guru'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-amazon_devops_guru=cli_anything.amazon_devops_guru:cli']},
)
