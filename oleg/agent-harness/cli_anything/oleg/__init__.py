import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('oleg running')
@cli.command()
def start(): click.echo('oleg started')
if __name__ == '__main__': cli()
