import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('apple running')
@cli.command()
def start(): click.echo('apple started')
if __name__ == '__main__': cli()
