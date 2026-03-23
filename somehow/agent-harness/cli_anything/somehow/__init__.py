import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('somehow running')
@cli.command()
def start(): click.echo('somehow started')
if __name__ == '__main__': cli()
