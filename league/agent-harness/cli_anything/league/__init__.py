import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('league running')
@cli.command()
def start(): click.echo('league started')
if __name__ == '__main__': cli()
