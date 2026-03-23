import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('fund running')
@cli.command()
def start(): click.echo('fund started')
if __name__ == '__main__': cli()
