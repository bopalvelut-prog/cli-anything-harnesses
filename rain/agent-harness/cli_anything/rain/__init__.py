import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('rain running')
@cli.command()
def start(): click.echo('rain started')
if __name__ == '__main__': cli()
