import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('strategy running')
@cli.command()
def start(): click.echo('strategy started')
if __name__ == '__main__': cli()
