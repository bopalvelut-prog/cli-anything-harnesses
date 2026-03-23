import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('shot running')
@cli.command()
def start(): click.echo('shot started')
if __name__ == '__main__': cli()
