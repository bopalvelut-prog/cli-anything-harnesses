import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('marvin running')
@cli.command()
def start(): click.echo('marvin started')
if __name__ == '__main__': cli()
