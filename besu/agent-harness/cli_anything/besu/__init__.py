import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def start(): click.echo('Besu started')
if __name__ == '__main__': cli()
