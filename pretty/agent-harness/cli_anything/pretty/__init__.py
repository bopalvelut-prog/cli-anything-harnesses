import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('pretty running')
@cli.command()
def start(): click.echo('pretty started')
if __name__ == '__main__': cli()
