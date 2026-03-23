import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('execute running')
@cli.command()
def start(): click.echo('execute started')
if __name__ == '__main__': cli()
