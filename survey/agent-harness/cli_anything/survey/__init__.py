import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('survey running')
@cli.command()
def start(): click.echo('survey started')
if __name__ == '__main__': cli()
