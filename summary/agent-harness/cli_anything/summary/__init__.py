import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('summary running')
@cli.command()
def start(): click.echo('summary started')
if __name__ == '__main__': cli()
