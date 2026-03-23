import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('trainer running')
@cli.command()
def start(): click.echo('trainer started')
if __name__ == '__main__': cli()
