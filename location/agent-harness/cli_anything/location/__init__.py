import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('location running')
@cli.command()
def start(): click.echo('location started')
if __name__ == '__main__': cli()
