import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('mention running')
@cli.command()
def start(): click.echo('mention started')
if __name__ == '__main__': cli()
