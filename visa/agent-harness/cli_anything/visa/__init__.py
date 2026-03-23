import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('visa running')
@cli.command()
def start(): click.echo('visa started')
if __name__ == '__main__': cli()
