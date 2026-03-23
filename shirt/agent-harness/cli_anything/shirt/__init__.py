import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('shirt running')
@cli.command()
def start(): click.echo('shirt started')
if __name__ == '__main__': cli()
