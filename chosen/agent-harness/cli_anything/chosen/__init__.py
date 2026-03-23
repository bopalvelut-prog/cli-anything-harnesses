import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('chosen running')
@cli.command()
def start(): click.echo('chosen started')
if __name__ == '__main__': cli()
