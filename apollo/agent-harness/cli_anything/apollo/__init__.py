import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def dev(): subprocess.run(['rover', 'dev'])
@cli.command()
def schema(): subprocess.run(['rover', 'subgraph', 'check'])
if __name__ == '__main__': cli()
