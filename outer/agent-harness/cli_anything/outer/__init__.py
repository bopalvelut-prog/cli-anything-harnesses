import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('outer running')
@cli.command()
def start(): click.echo('outer started')
if __name__ == '__main__': cli()
