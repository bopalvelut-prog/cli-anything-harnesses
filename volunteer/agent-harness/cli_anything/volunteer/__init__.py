import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('volunteer running')
@cli.command()
def start(): click.echo('volunteer started')
if __name__ == '__main__': cli()
