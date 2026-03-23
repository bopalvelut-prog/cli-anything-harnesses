import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('yell running')
@cli.command()
def start(): click.echo('yell started')
if __name__ == '__main__': cli()
