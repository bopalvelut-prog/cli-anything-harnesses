import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('zeal running')
@cli.command()
def start(): click.echo('zeal started')
if __name__ == '__main__': cli()
