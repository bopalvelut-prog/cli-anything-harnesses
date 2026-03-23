import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('describe running')
@cli.command()
def start(): click.echo('describe started')
if __name__ == '__main__': cli()
