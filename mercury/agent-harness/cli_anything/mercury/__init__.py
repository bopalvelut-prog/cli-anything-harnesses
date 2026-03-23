import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('mercury running')
@cli.command()
def start(): click.echo('mercury started')
if __name__ == '__main__': cli()
