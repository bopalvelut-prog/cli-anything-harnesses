import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('xcel running')
@cli.command()
def start(): click.echo('xcel started')
if __name__ == '__main__': cli()
