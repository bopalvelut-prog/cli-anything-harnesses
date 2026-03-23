import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('hardware running')
@cli.command()
def start(): click.echo('hardware started')
if __name__ == '__main__': cli()
