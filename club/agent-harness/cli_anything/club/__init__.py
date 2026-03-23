import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('club running')
@cli.command()
def start(): click.echo('club started')
if __name__ == '__main__': cli()
