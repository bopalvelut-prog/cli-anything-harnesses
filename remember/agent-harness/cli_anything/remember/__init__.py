import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('remember running')
@cli.command()
def start(): click.echo('remember started')
if __name__ == '__main__': cli()
