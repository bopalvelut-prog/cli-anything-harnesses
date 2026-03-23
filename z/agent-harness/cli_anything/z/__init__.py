import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('z running')
@cli.command()
def start(): click.echo('z started')
if __name__ == '__main__': cli()
