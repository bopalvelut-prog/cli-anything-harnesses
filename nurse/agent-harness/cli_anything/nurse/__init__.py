import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('nurse running')
@cli.command()
def start(): click.echo('nurse started')
if __name__ == '__main__': cli()
