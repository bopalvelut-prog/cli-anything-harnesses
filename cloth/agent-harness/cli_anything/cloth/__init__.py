import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('cloth running')
@cli.command()
def start(): click.echo('cloth started')
if __name__ == '__main__': cli()
