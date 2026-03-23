import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('content running')
@cli.command()
def start(): click.echo('content started')
if __name__ == '__main__': cli()
