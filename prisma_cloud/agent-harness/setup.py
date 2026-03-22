from setuptools import setup
setup(
    name='cli-anything-prisma_cloud',
    version='1.0.0',
    packages=['cli_anything.prisma_cloud'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-prisma_cloud=cli_anything.prisma_cloud:cli']},
)
