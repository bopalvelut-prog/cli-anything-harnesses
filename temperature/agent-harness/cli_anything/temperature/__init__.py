import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('temperature running')
@cli.command()
def start(): click.echo('temperature started')
if __name__ == '__main__': cli()
