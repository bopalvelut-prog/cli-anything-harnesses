import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('rubber running')
@cli.command()
def start(): click.echo('rubber started')
if __name__ == '__main__': cli()
