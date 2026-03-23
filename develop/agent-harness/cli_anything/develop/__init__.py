import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('develop running')
@cli.command()
def start(): click.echo('develop started')
if __name__ == '__main__': cli()
