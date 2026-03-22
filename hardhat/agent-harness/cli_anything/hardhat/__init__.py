import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def compile(): subprocess.run(['npx', 'hardhat', 'compile'])
@cli.command()
def test(): subprocess.run(['npx', 'hardhat', 'test'])
@cli.command()
def deploy(): subprocess.run(['npx', 'hardhat', 'run', 'scripts/deploy.js'])
if __name__ == '__main__': cli()
