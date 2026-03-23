import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('shadow running')
@cli.command()
def start(): click.echo('shadow started')
if __name__ == '__main__': cli()
