import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('window running')
@cli.command()
def start(): click.echo('window started')
if __name__ == '__main__': cli()
