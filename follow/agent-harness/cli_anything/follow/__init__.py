import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('follow running')
@cli.command()
def start(): click.echo('follow started')
if __name__ == '__main__': cli()
