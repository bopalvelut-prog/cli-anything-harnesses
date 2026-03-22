import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def start(): subprocess.run(['anvil'])
@cli.command()
def status(): click.echo('Anvil running')
if __name__ == '__main__': cli()
