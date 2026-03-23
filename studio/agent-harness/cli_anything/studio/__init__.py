import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('studio running')
@cli.command()
def start(): click.echo('studio started')
if __name__ == '__main__': cli()
