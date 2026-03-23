import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('nearby running')
@cli.command()
def start(): click.echo('nearby started')
if __name__ == '__main__': cli()
