import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('congress running')
@cli.command()
def start(): click.echo('congress started')
if __name__ == '__main__': cli()
