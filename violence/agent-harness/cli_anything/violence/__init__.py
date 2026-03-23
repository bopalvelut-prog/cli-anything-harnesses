import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('violence running')
@cli.command()
def start(): click.echo('violence started')
if __name__ == '__main__': cli()
