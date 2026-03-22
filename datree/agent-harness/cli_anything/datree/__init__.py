import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def test(): subprocess.run(['datree', 'test', '.'])
@cli.command()
def publish(): subprocess.run(['datree', 'publish', 'policy.yaml'])
if __name__ == '__main__': cli()
