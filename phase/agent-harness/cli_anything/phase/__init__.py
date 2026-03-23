import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('phase running')
@cli.command()
def start(): click.echo('phase started')
if __name__ == '__main__': cli()
