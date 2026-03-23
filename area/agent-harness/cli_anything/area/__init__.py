import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('area running')
@cli.command()
def start(): click.echo('area started')
if __name__ == '__main__': cli()
