import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('secret running')
@cli.command()
def start(): click.echo('secret started')
if __name__ == '__main__': cli()
