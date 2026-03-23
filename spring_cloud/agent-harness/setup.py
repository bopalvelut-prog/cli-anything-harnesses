from setuptools import setup
setup(
    name='cli-anything-spring_cloud',
    version='1.0.0',
    packages=['cli_anything.spring_cloud'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-spring_cloud=cli_anything.spring_cloud:cli']},
)
