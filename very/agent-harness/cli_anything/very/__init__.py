import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('very running')
@cli.command()
def start(): click.echo('very started')
if __name__ == '__main__': cli()
