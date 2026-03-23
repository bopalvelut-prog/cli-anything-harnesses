import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('rock running')
@cli.command()
def start(): click.echo('rock started')
if __name__ == '__main__': cli()
