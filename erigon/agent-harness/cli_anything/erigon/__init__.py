import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def start(): click.echo('Erigon started')
if __name__ == '__main__': cli()
