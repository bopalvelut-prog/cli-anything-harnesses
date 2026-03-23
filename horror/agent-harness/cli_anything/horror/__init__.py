import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('horror running')
@cli.command()
def start(): click.echo('horror started')
if __name__ == '__main__': cli()
