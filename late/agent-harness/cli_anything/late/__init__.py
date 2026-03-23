import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('late running')
@cli.command()
def start(): click.echo('late started')
if __name__ == '__main__': cli()
