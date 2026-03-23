import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('ntp running')
@cli.command()
def start(): click.echo('ntp started')
if __name__ == '__main__': cli()
