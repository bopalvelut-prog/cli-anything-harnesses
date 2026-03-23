import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('bfg running')
@cli.command()
def start(): click.echo('bfg started')
if __name__ == '__main__': cli()
