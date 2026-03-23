import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('finger running')
@cli.command()
def start(): click.echo('finger started')
if __name__ == '__main__': cli()
