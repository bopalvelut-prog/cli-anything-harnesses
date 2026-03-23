import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('carpet running')
@cli.command()
def start(): click.echo('carpet started')
if __name__ == '__main__': cli()
