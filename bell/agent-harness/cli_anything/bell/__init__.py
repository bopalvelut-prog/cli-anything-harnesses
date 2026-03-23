import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('bell running')
@cli.command()
def start(): click.echo('bell started')
if __name__ == '__main__': cli()
