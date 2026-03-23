import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('physical running')
@cli.command()
def start(): click.echo('physical started')
if __name__ == '__main__': cli()
