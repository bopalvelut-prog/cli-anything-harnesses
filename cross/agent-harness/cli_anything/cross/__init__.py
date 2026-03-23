import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('cross running')
@cli.command()
def start(): click.echo('cross started')
if __name__ == '__main__': cli()
