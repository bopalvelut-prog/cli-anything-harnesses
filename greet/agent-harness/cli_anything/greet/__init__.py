import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('greet running')
@cli.command()
def start(): click.echo('greet started')
if __name__ == '__main__': cli()
