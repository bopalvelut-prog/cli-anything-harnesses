import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('dspace running')
@cli.command()
def start(): click.echo('dspace started')
if __name__ == '__main__': cli()
